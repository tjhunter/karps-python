""" Utilities to express rows of data with Karps.
"""

from .proto import types_pb2
from .proto import row_pb2

from .types import *

__all__ = ['CellWithType', 'as_cell', 'as_python_object']

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

def as_cell(obj, schema=None):
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
  cwt_proto = _as_cell(obj, schema._proto if schema else None)
  return CellWithType(cwt_proto)

def as_python_object(cwt):
  """ Converts a CellWithType object to a python object (best effort).
  """
  return _as_python(cwt._proto.cell, cwt._proto.cell_type)

def _as_python(c_proto, tpe_proto):
  # The type is still required for dictionaries.
  if c_proto.HasField('int_value'):
    return int(c_proto.int_value)
  if c_proto.HasField('string_value'):
    return str(c_proto.string_value)
  if c_proto.HasField('double_value'):
    return float(c_proto.double_value)
  if c_proto.HasField('array_value'):
    return [_as_python(x, tpe_proto.array_type) for x in c_proto.array_value.values]
  if c_proto.HasField('struct_value'):
    fields = tpe_proto.struct_type.fields
    field_names = [f.field_name for f in fields]
    field_types = [f.field_type for f in fields]
    values = [_as_python(x, t) for (x, t) in zip(c_proto.struct_value, field_types)]
    return dict(zip(field_names, values))

def _as_cell(obj, tpe_proto):
  # This is one of the most complex functions, because it tries to do the 'right' thing from
  # the perspective of the user, which is not a fuzzy concept.
  if obj is None:
    assert tpe_proto is None or tpe_proto.nullable, (obj, tpe)
    return row_pb2.CellWithType(cell_type=tpe_proto)
  if isinstance(obj, int):
    # Strict int
    tpe_proto = tpe_proto or types_pb2.SQLType(basic_type=types_pb2.SQLType.INT, nullable=False)
    assert tpe_proto.basic_type == types_pb2.SQLType.INT, tpe_proto
    return row_pb2.CellWithType(
      cell=row_pb2.Cell(int_value=int(obj)),
      cell_type=tpe_proto)
  # Something that looks like a list
  if isinstance(obj, (list, tuple)):
    is_tuple = isinstance(obj, tuple)
    obj = list(obj)
    if tpe_proto is None:
      # Infer the type
      if is_tuple:
        # Interpret as a structure
        field_names = ["_" + str(idx+1) for idx in range(len(obj))]
        return _as_cell(dict(zip(field_names, obj)), None)
      else:
        # Interpret as an array cell
        cells = [_as_cell(x, None) for x in obj]
        # Merge all the cells into a cell array.
        inner_type = None
        if cells:
          inner_type = cells[0].cell_type
          for cwt in cells[1:]:
            inner_type = merge_proto_types(inner_type, cwt.cell_type)
        tpe_proto = types_pb2.SQLType(array_type=inner_type, nullable=False)
    elif tpe_proto.HasField("array_type"):
      # It is an array
      cells = [_as_cell(x, tpe_proto.array_type) for x in obj]
    elif tpe_proto.HasField("struct_type"):
      # It is a struct, which is represented as an array.
      field_types = [f.field_type for f in tpe_proto.struct_type.fields]
      assert len(field_types) == len(obj), (field_types, obj)
      cells = [_as_cell(x, ftype) for (x, ftype) in zip(obj, field_types)]
      return row_pb2.CellWithType(
        cell=row_pb2.Cell(struct_value=row_pb2.Row(values=cs)),
        cell_type=tpe_proto)
    else:
      assert False, (tpe_proto, type(obj))
    cs = [cwt_proto.cell for cwt_proto in cells]
    return row_pb2.CellWithType(
      cell=row_pb2.Cell(array_value=row_pb2.ArrayCell(values=cs)),
      cell_type=tpe_proto)
  if isinstance(obj, dict):
    if tpe_proto is None:
      # use the keys as proxies for the names, and sort alphabetically.
      cells = [_as_cell(x, None) for (_, x) in obj.items()]
      keys = [k for (k, _) in obj.items()]
      return _struct(cells, keys, sort=True)
    else:
      assert tpe_proto.HasField('struct_type'), tpe_proto
      # Use the structure
      # Exact structural matching for now.
      fields = tpe_proto.struct_type.fields
      assert len(obj) == len(fields), (tpe_proto, obj)
      cells = []
      for field in fields:
        assert field.field_name in obj, (field, obj)
        f_cwt = _as_cell(obj[field.field_name], field.field_type)
        cells.append(f_cwt.cell)
      return row_pb2.CellWithType(
        cell=row_pb2.Cell(struct_value=row_pb2.Row(values=cells)),
        cell_type=tpe_proto)


def _struct(cwts, field_names, sort=False):
  assert len(cwts) == len(field_names)
  if sort:
    z = sorted(zip(field_names, cwts), key=lambda k: k[0])
    return _struct([c for (_, c) in z], [k for (k, _) in z])
  sfields = [types_pb2.StructField(
    field_name=fname,
    field_type=cwt.cell_type) for (cwt, fname) in zip(cwts, field_names)]
  vals = [cwt.cell for cwt in cwts]
  return row_pb2.CellWithType(
    cell=row_pb2.Cell(array_value=row_pb2.ArrayCell(values=vals)),
    cell_type = types_pb2.SQLType(
      struct_type=types_pb2.StructType(
        fields=sfields)
      )
    )
