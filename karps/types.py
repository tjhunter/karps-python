from .proto import types_pb2 as pb

__all__ = ['DataType', 'IntegerType']

class DataType(object):

  def __init__(self, _proto):
    # The underlying representation uses the proto interface.
    self._proto = _proto

  def __repr__(self):
    return _repr_proto(self._proto)

  def __eq__(self, other):
    return self._proto == other._proto

  def __ne__(self, other):
    return self._proto != other._proto

  @property
  def strict(self):
    return not self._proto.nullable

  @property
  def nullable(self):
    return self._proto.nullable

def IntegerType(strict=True):
  return DataType(pb.SQLType(basic_type=pb.SQLType.INT, nullable=not strict))

def merge_types(tp1, tp2):
  """ Attempts to merge two types
  """

def _repr_proto(p):
  x = None
  if p.basic_type == pb.SQLType.INT:
    x = "int" 
  if p.basic_type == pb.SQLType.DOUBLE:
    x = "double"
  assert x, p
  if p.nullable:
    x = x + "?"
  return x
