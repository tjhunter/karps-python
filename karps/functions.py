""" The standard library of dataframe functions in Karps.
"""

from .column import Observable
from .types import ArrayType
from .functions_std.utils import *
from .functions_std.error import *
import builtins as _b

__all__ = ['collect', 'max', 'inv']

def _check_same_2(dt1, dt2):
  # TODO: take nullability into account
  if dt1 != dt2:
    raise CreationError("Types %s and %s are not compatible" %(dt1, dt2))
  return dt1

collect = make_aggregator_sql("collect_list", ArrayType, _b.list)

max = make_aggregator_sql("max", check_type_number, _b.max)

inv = make_transform_sql1("inv", check_type_number, lambda x: 1/x)

plus = make_transform_sql("plus", _check_same_2, 2, lambda x1, x2: x1+x2)

minus = make_transform_sql("minus", _check_same_2, 2, lambda x1, x2: x1-x2)

multiply = make_transform_sql("mulitply", _check_same_2, 2, lambda x1, x2: x1*x2)

divide = make_transform_sql("divide", _check_same_2, 2, lambda x1, x2: x1/x2)
