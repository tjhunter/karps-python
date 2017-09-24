""" A general notion of data grouped by key.

This module generally mimics the pandas API.
"""

from .functions_std.base import placeholder_like, struct
from .functions_std.error import *
from .column import build_dataframe, AbstractColumn
from .types import StructField, StructType

__all__ = ['KeyedGroup', 'groupby']

class KeyedGroup(object):
  """ A dataset, grouped by some key.

  Users should not have to create this object directly.
  """

  def __init__(self, ref, key_col, value_col):
    self._ref = ref # The referring dataframe.
    self._key_col = key_col # A column of data with the same ref
    self._value_col = value_col # A column with the same ref

  def agg(self, aggobj, name=None):
    """ Performs an aggregation on the given dataframe.
    
    agg_obj: an object that describes some aggregation. It can be one of the 
    following:
     - a string that contains a known aggregation function or UDAF, such as 'min', 'sum', 'count', ...
     - a python function that accepts a column or dataframe and returns an 
       observable. Some restrictions apply, but a lot of things are tolerated.
     - a non-empty list or tuple of accepted aggregation objects. In this case, 
       the fields are labeled '_XXX' with XXX the position (starting from 1)
     - a non-empty list of (field name, agg object)
     - a dictionary of {field name, agg obj}. The resulting structure is returned 
       sorted in field name order.
     - an OrderedDict object. The order is preserved.
    """
    return _agg_ks(self, aggobj, name)

  def transform(self, fun, name=None):
    create_error("not implemented")

  def to_df(self, name=None):
    create_error("not implemented")

  def __repr__(self):
    return "KeyedGroup(ref={}, key={}, value={})".format(
      self._ref, self._key_col.type, self._value_col.type)


def groupby(obj, key):
  if isinstance(obj, AbstractColumn):
    # We group over the whole dataframe or a column of Karps data.
    return _groupby_ks(obj.reference, key, obj.as_column())

def _groupby_ks(obj, key_obj, value_obj):
  """ Implementation of the grouping logic for karps objects.
  """
  if not isinstance(key_obj, AbstractColumn):
    create_error("Key can only be column for now, got type {}".format(type(key_obj)))
  key_col = key_obj.as_column()
  value_col = value_obj.as_column()
  if key_col.reference is not obj:
    create_error("Key reference: {} is distinct from group reference: {}".format(key_col.reference, obj))
  if value_col.reference is not obj:
    create_error("Value reference {} is distinct from group reference: {}".format(value_col.reference, obj))
  return KeyedGroup(obj, key_col, value_col)

def _agg_ks(kg, aggobj, name):
  """ Implementation of the aggregation logic for karps keyed groups.
  """
  df = struct([('key', kg._key_col), ('value', kg._value_col)]).as_dataframe()
  ph = placeholder_like(kg._value_col)
  out = _process_aggobj(aggobj, ph)
  print("_agg_ks: out={}".format(out))
  # The fields of the return type.
  dt = StructType([StructField(kg._key_col.type, "key")] + [StructField(o.type, fname) for (fname, o) in out])
  return build_dataframe(
    op_name="org.spark.FunctionalShuffle",
    type_p=dt,
    parents=[df, ph] + [obs for (_, obs) in out],
    name_hint="shuffle",
    path_extra=name)

def _process_aggobj(aggobj, pholder):
  if hasattr(aggobj, '__call__'):
    # Just a single element -> wrap with a tuple name
    # No need to be too smart for now about the return name:
    return _process_aggobj0([(aggobj.__name__, aggobj)], pholder)
  return _process_aggobj0(aggobj, pholder)

def _process_aggobj0(aggobj, pholder):
  # Returns a list of (name, observable)
  if isinstance(aggobj, dict):
    # Flatten the dictionary and sort by name:
    l = sorted(aggobj.items(), key=lambda x:x[0])
    return _process_aggobj0(l, pholder)
  if isinstance(aggobj, (list, tuple)):
    aggobj = list(aggobj)
    res = []
    for obj in aggobj:
      if isinstance(obj, tuple):
        assert len(obj) == 2, obj
        (key, obj1) = obj
        assert isinstance(key, str), (type(key), key)
        res.append((key, _process_aggobj0(obj1, pholder)))
    return res
  if hasattr(aggobj, '__call__'):
    # It is a function.
    return aggobj(pholder)
  create_error("Aggregation object not understood: {}: {}".format(type(aggobj), aggobj))
