""" The standard library of dataframe functions in Karps.
"""

from .column import Observable
from .types import ArrayType
from .functions_std.utils import make_aggregator_sql, check_type_number
import builtins as _b

__all__ = ['collect', 'max']

collect = make_aggregator_sql("collect_list", ArrayType, _b.list)

max = make_aggregator_sql("max", check_type_number, _b.max)

# def collect(c, name=None):
#   return Observable("org.spark.Collect",
#     ArrayType(c.type),
#     parents=[c],
#     path_extra=name)

# def max(c, name=None):
#   return Observable("org.spark.Max", c.type,
#     parents=[c],
#     path_extra=name)

