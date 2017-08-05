""" An asynchronous computation.
"""

class Computation(object):
  """ An asynchronous computation.

  This object provides access to the different lifetimes of a computation:
   - original computation graph (with functional attributes)
   - static computation graph (after unrolling of the functions)
   - pinned graph (after optimization, which will be provided to the backend)
   - results and stats (including for spark, the detail of the various plans)
  """

  def __init__(self, session_id_p, computation_id_p, channel, target_fetch_paths):
    self._session_id_p = session_id_p
    self._computation_id_p = computation_id_p
    self._channel = channel
    self._target_fetch_paths = target_fetch_paths

  def values(self):
    """ Returns the fetches (or the unique fetch if there is only one).

    Blocks until the fetches are available or until an error is raised.
    """
    for x in self._channel:
      print(x)
    raise None
