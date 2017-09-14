""" Some standard utiltilies for defining functions.

These are developer functions that are not covered by API guarantees.
"""


from karps.column import Observable, DataFrame, Column
from karps.types import ArrayType
from karps.proto import types_pb2
from karps.proto import structured_transform_pb2 as st_pb2
from karps.proto import std_pb2 as std_pb2

class CreationError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(ValidationError, self).__init__(message)

def check_df(df):
  """ Checks if the input is a dataframe, or turns it into a dataframe
  if necessary (if it is a column).
  """
  if isinstance(df, DataFrame):
    return df
  if isinstance(df, Column):
    return df.as_dataframe()
  raise CreationError("Trying to cast %s as a dataframe, which is of type %s" % (df, type(df)))

def check_type_number(dt):
  p = dt.to_proto
  if p.HasField("basic_type") and p.basic_type in [types_pb2.SQLType.DOUBLE, types_pb2.SQLType.INT]:
    return dt
  raise CreationError("Expected type to be a type number: %s" % dt)

def make_aggregator_sql(sqlname, typefun, pyfun=None, spfun=None):
  """
  sqlname: the name of the sql function
  typefun: datatype -> datatype

  Returns a function of type (df-like, name: string) -> observable
  """
  def function_karps(df, name):
    df = check_df(df)
    type_out = typefun(df.type)
    # the proto that defines the aggregation.
    p = std_pb2.StructuredReduce(agg_op=st_pb2.Aggregation(
      op=st_pb2.AggregationFunction(
        function_name=sqlname,
        inputs=[st_pb2.ColumnExtraction(path=[])]
        ),
      field_name=name))
    return Observable("org.spark.StructuredReduce", type_out,
      parents=[df],
      op_extra_p=p,
      op_name_hint=sqlname,
      path_extra=name)
  def function(df, name=None):
    if isinstance(df, (DataFrame, Column)):
      return function_karps(df, name)
    # TODO: check for Spark
    # Assume this is a python object, pass it to python:
    return pyfun(df)
  return function
