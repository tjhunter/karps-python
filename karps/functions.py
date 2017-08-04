""" The standard library of dataframe functions in Karps.
"""

from .column import Observable
from .types import ArrayType

def collect(c, name=None):
  return Observable("org.spark.Collect",
    ArrayType(c.type),
    parents=[c],
    path_extra=name)
