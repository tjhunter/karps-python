""" The standard library of dataframe functions in Karps.
"""

from .column import Observable
from .types import ArrayType, IntegerType, DoubleType, BooleanType
from .functions_std.utils import *
from .functions_std.error import *
import builtins as _b

#__all__ = ['as_double', 'collect', 'count', 'inv', 'max']

def _check_same_2(dt1, dt2):
  # TODO: take nullability into account
  if dt1 != dt2:
    raise CreationError("Types %s and %s are not compatible" %(dt1, dt2))
  return dt1

def _check_cmp(dt1, dt2):
  """ Comparison check.
  """
  _check_same_2(dt1, dt2)
  return BooleanType()

collect = make_aggregator_sql("collect_list", ArrayType, _b.list)

max = make_aggregator_sql("max", check_type_number, _b.max)

count = make_aggregator_sql("count", lambda x: IntegerType(), _b.len)

sum = make_aggregator_sql("sum", check_type_number, _b.sum)

inv = make_transform_sql1("inv", check_type_number, lambda x: 1/x)

plus = make_transform_sql("plus", _check_same_2, 2, lambda x1, x2: x1+x2)

minus = make_transform_sql("minus", _check_same_2, 2, lambda x1, x2: x1-x2)

multiply = make_transform_sql("mulitply", _check_same_2, 2, lambda x1, x2: x1*x2)

divide = make_transform_sql("divide", _check_same_2, 2, lambda x1, x2: x1/x2)

def _cast_double(dt):
  if dt == DoubleType() or dt == IntegerType():
    return DoubleType()
  raise CreationError("Cannot cast type {} to double".format(dt))

as_double = make_transform_sql("cast_double", _cast_double, 1, float)

greater_equal = make_transform_sql("greater_equal", _check_cmp, 2, lambda x1, x2: x1==x2)


########### FUNCTIONS ON DATASETS #########
# These functions only operate on datasets.

def autocache(df, name=None):
  # The autocache function.
  df = check_df(df)
  return build_dataframe(
    op_name="org.spark.Autocache",
    type_p=df.type,
    parents=[df],
    name_hint="autocache",
    path_extra=name)

def filter(filter_col, col, name=None):
  """ Returns a dataframe with all the values from `col` subject to 
  a predicate that is verified in `filter_col`.
  """
  df = check_df(struct([("filter", filter_col), ("value", col)]))
  return build_dataframe(
    op_name="org.spark.Filter",
    type_p=col.type,
    parents=[df],
    name_hint="filter",
    path_extra=name)

