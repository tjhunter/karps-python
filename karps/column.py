""" The expression of a column or a dataframe (unbounded lists of values).
"""

#from pyrsistent import m as PMap
import re

from .proto import types_pb2
from .row import as_cell
from .utils import current_path, get_and_increment_counter
from .types import DataType

__all__ = ['Column', 'DataFrame', 'dataframe']

class AbstractColumn(object):
  """ A column of data.

  This is an abstraction for a potentially unbounded list of cells, all of the same types.

  The difference between columns and dataframes is that dataframes can exist on their own,
  while columns have a refering dataframe.

  Users should never have to create manually columns or dataframes, but rely on the framework
  for doing so.
  """

  @property
  def type(self):
    """ The data type of this column """
    return DataType(self._type_p)

  def __getattr__(self, name):
    return self[name]

  def __getitem__(self, name):
    if isinstance(name, str):
      # Assuming to accessing a field in a struct
      assert self.type.is_struct_type, self.type
      fnames = [f.name for f in self.type.struct_fields]
      assert name in fnames, (name, fnames)
      return None
    assert False, type(name)

class AbstractNode(object):
  """ The base class for observables or dataframes.
  """

  @property
  def path(self):
    return self._path

  @property
  def op_name(self):
    return self._op_name

  @property
  def type(self):
    """ The data type of this column """
    return DataType(self._type_p)

  def __repr__(self):
    return "{p}@{o}:{dt}".format(
      p=str(self.path),
      o=self.op_name,
      dt=str(self.type))


class Column(AbstractColumn):
  """ A column of data isolated from a dataframe.
  """

  def __init__(self,
      ref, # Dataframe
      type_p, # SQLType
      field_name=None,
      struct=None, # List of cols (with field names)
      function_name=None, # String
      function_deps=None, # List of cols or observables.
      extraction=None): # list of strings
    AbstractColumn.__init__(self)
    assert ref # DataFrame
    assert struct or function_name or extraction # One of the protos
    self._ref = ref
    self._type_p = _type_as_proto(type_p)
    self._field_name = field_name
    self._struct = struct
    self._function_name = function_name
    self._function_deps = function_deps
    self._extraction = extraction

  @property
  def reference(self):
    """ The referring dataframe """
    return self._ref

  def as_column(self):
    """ A column, seen as a column.
    """
    return self

  def as_dataframe(self):
    """ A column, seen as a dataframe (referring to itself).

    This causes all the columns to be resolved and coalesced. Intermediary dataframes may
    also be created if some broadcasts need to happen. The current resolution is rather inefficient.
    """
    assert False


class DataFrame(AbstractColumn, AbstractNode):
  """ A dataframe.
  """

  def __init__(self,
      op_name, # String
      type_p, # SQLType
      op_extra_p=None, # proto for extra of the op
      parents=None, # List of nodes
      deps=None, # List of nodes
      path=None,
      path_extra=None): # Path
    AbstractColumn.__init__(self)
    AbstractNode.__init__(self)
    self._op_name = op_name
    self._type_p = _type_as_proto(type_p)
    if path is None:
      path = _build_path(path_extra, op_name, current_path())
    self._path = path
    self._op_extra_p = op_extra_p
    self._parents = _as_nodes(parents)
    self._deps = _as_nodes(deps)


  def as_column(self):
    """ A dataframe, seen as a column.
    """
    assert False 

  def as_dataframe(self):
    """ A dataframe, seen as a dataframe. """
    return self


class Observable(AbstractNode):
  """ An observable.
  """

  def __init__(self,
      op_name, # String
      type_p, # SQLType
      op_extra_p=None, # proto for extra of the op
      parents=None, # List of nodes
      deps=None, # List of nodes
      path=None,
      path_extra=None): # Path
    AbstractNode.__init__(self)
    self._op_name = op_name
    self._type_p = _type_as_proto(type_p)
    if path is None:
      path = _build_path(path_extra, op_name, current_path())
    self._path = path
    self._op_extra_p = op_extra_p
    self._parents = _as_nodes(parents)
    self._deps = _as_nodes(deps)

def dataframe(obj, schema=None, name=None):
  """ Constructs a dataframe from a python object.

  This object can be:
   - a list or tuple of PySpark rows
   - a list of tuple of other Python objects
   - a pandas dataframe
   - a numpy array

  The schema can be:
   - nothing (it will be inferred if possible)
   - a string (the name of the column if there is a single column)
   - a list or tuple of strings (the names of the top-level columns)
   - a PySpark data type
   - a Kaprs data type

  If a schema is provided, the data will be checked for matching the types.
  """
  # If we are provided a schema, lists will be interpreted as tuples:
  if isinstance(obj, list) and schema is not None:
    obj = [tuple(z) if isinstance(z, list) else z for z in obj]
  if isinstance(schema, str):
    schema = [schema]
  if isinstance(schema, DataType):
    cwt = as_cell(obj, schema=schema)
  else:
    # Use full inference
    cwt = as_cell(obj, schema=None)
  assert cwt.type.is_array_type, cwt.type
  ct_proto = cwt.type.inner_type._proto
  # Try to get nicer names for the columns
  if isinstance(schema, list):
    assert ct_proto.HasField('struct_type'), ct_proto
    assert len(schema) == len(ct_proto.struct_type.fields), (schema, ct_proto)
    for (fname, f) in zip(schema, ct_proto.struct_type.fields):
      f.field_name = fname
  return DataFrame(
    op_name="org.spark.DistributedLiteral",
    op_extra_p=cwt._proto,
    type_p=ct_proto,
    path_extra=name)

def _type_as_proto(tpe):
  if isinstance(tpe, DataType):
    return tpe._proto
  elif isinstance(tpe, types_pb2.SQLType):
    return tpe
  assert False, type(tpe)

def _as_nodes(l):
  if not l:
    return []
  res = []
  for x in l:
    if isinstance(x, AbstractNode):
      res.append(x)
    elif isinstance(x, Column):
      res.append(x.as_dataframe())
    else:
      assert False, (type(x), x)
  return res

def _convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def _build_path(requested_name, op_name, curr_path):
  if not requested_name:
    counter = get_and_increment_counter()
    requested_name = _convert(op_name.split(".")[-1]) + "_" + str(counter)
  requested_path = curr_path.push(requested_name)
  return requested_path
