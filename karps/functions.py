""" The standard library of dataframe functions in Karps.
"""

from .column import Observable
from .types import ArrayType
from .functions_std.utils import *
import builtins as _b

__all__ = ['collect', 'max', 'inv']

collect = make_aggregator_sql("collect_list", ArrayType, _b.list)

max = make_aggregator_sql("max", check_type_number, _b.max)

inv = make_transform_sql1("inv", check_type_number, lambda x: 1/x)

