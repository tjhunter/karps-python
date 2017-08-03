""" Utilities to express rows of data with Karps.
"""

from .proto import types_pb2
from .proto import row_pb2

from .types import *

__all__ = ['CellWithType', 'as_cell']

class CellWithType(object):
  """ A cell of data, with its type information.

  This is usually constructed with one of the helper functions.
  """

  def __init__(self, proto):
    assert proto
    self._proto = proto # A CellWithType proto

  def __repr__(self):
    # TODO: this could be better.
    return repr((self.type, self._proto.cell))

  def __eq__(self, other):
    return self._proto == other._proto

  def __ne__(self, other):
    return self._proto != other._proto

  @property
  def type(self):
    """ The data type associated to this cell.
    """
    if self._proto.cell_type:
      return DataType(self._proto.cell_type)
    return None

def as_cell(obj, tpe=None):
  """ Converts a python object as a cell, potentially with the help of extra type hints.

  If the type is not provided, it will be inferred 
  The object can be any of the following:
   - None
   - a primitive
   - an iterable or a tuple. They are considered array types, unless a struct type is provided as a
     hint
   - a dictionary. It is considered a struct, with all the fields sorted in alphabetical order.
   - a pandas type
   - a Spark row
   - a numpy row
  """
  # TODO: it should return value errors instead of assertions.
  tpe_proto = None if tpe is None else tpe._proto
  tpe = None if tpe_proto is None else DataType(tpe_proto)
  if obj is None:
    assert tpe is None or tpe.nullable, (obj, tpe)
    return CellWithType(row_pb2.CellWithType(cell=None, cell_type=tpe_proto))
  if isinstance(obj, int):
    # Strict int
    tpe = tpe or IntegerType()
    assert tpe == IntegerType(), (tpe)
    return CellWithType(row_pb2.CellWithType(
      cell=row_pb2.Cell(int_value=int(obj)),
      cell_type=tpe._proto))

def _merge_array(cwts):
  """ Merges the cells of arrays, checking that the types are all compatible.
  """
  assert False