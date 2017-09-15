""" Some standard utiltilies for defining functions.

These are developer functions that are not covered by API guarantees.
"""


from karps.column import Observable, DataFrame, Column
from karps.types import ArrayType
from karps.proto import types_pb2
from karps.proto import structured_transform_pb2 as st_pb2
from karps.proto import std_pb2 as std_pb2
from .base import *
from .error import *



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
    return build_observable("org.spark.StructuredReduce", type_out,
      parents=[df],
      op_extra=p,
      name_hint=sqlname,
      path_extra=name)
  def function(df, name=None):
    if isinstance(df, (DataFrame, Column)):
      return function_karps(df, name)
    # TODO: check for Spark
    # Assume this is a python object, pass it to python:
    return pyfun(df)
  return function

def make_transform_sql1(sqlname, typefun, pyfun=None, spfun=None):
  """ Makes a sql transformer that accepts only one argument.

  sqlname: the name of the sql function.
  typefun: a function that accepts one datatype and returns a datatype.

  Returns a function of type (input: col-like, name: string) -> col-like, with the following rules:
   - observable -> observable
   - column -> column
   - dataframe -> dataframe
   - python object -> python object
  """
  def function_karps(obj1, name):
    type_in = obj1.type
    type_out = typefun(type_in)
    # Get the column input for the data.
    if isinstance(obj1, Column):
      return Column(
        ref = obj1.reference,
        type_p = type_out,
        function_name=sqlname,
        function_deps=[obj1])
    elif isinstance(obj1, (DataFrame, Observable)):
      proto_in = st_pb2.Column(
        extraction=st_pb2.ColumnExtraction(path=[]))
      proto_out = st_pb2.Column(
        function=st_pb2.ColumnFunction(
          function_name=sqlname,
          inputs=[proto_in]),
        field_name="%s()" % sqlname) # TODO: fix the name
    else:
      raise CreationError("Does not understand object of type %s" % (type(obj1)))
    if isinstance(obj1, DataFrame):
      p = std_pb2.StructuredTransform(
        col_op=proto_out)
      return build_dataframe(
        op_namp="org.spark.StructuredTransform",
        type_p=type_out,
        op_extra=p,
        parents=[obj1],
        oname_hint=sqlname,
        path_extra=name)
    if isinstance(obj1, Observable):
      p = st_pb2.LocalStructuredTransform(
        col_op=proto_out)
      return build_observable(
        op_namp="org.spark.LocalStructuredTransform",
        type_p=type_out,
        op_extra=p,
        parents=[obj1],
        oname_hint=sqlname,
        path_extra=name)
  def function(df, name=None):
    if isinstance(df, (DataFrame, Column, Observable)):
      return function_karps(df, name)
    # TODO: check for Spark
    # Assume this is a python object, pass it to python:
    return pyfun(df)
  return function



