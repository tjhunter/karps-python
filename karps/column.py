""" The expression of a column or a dataframe (unbounded lists of values).
"""

class Column(object):
  pass

# Same thing in python.
DataFrame = Column

def dataframe(obj, schema=None):
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
  assert False
