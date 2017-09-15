""" Some basic functions that are used as building blocks 
for other functions.

They are not expected to be called by users, but are exposed
for developers.
"""
from karps.column import Observable, DataFrame, Column, build_dataframe, build_observable
from karps.types import make_tuple

def pack_local(*observables):
  """ Takes a list of observables and returns a tuple of all 
  the observables together.
  """
  if not observables:
    raise CreationError("List of observables cannot be empty")
  for obs in observables:
    if not isinstance(obs, Observable):
      raise CreationError("Expected input to be of type observable, but got type %s instead for %s" % (type(obs), obs))
  tpe = make_tuple(*[obs.type for obs in observables])
  return build_observable(
    op_name="org.spark.PackLocal",
    type_p=tpe._proto,
    parents=observables)