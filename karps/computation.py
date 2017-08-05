""" An asynchronous computation.
"""

from .proto import computation_pb2
from .utils import Path
from .row import CellWithType, as_python_object

class Computation(object):
  """ An asynchronous computation.

  This object provides access to the different lifetimes of a computation:
   - original computation graph (with functional attributes)
   - static computation graph (after unrolling of the functions)
   - pinned graph (after optimization, which will be provided to the backend)
   - results and stats (including for spark, the detail of the various plans)
  """

  def __init__(self, session_id_p, computation_id_p,
    channel, target_fetch_paths, final_unpack, return_mode):
    self._session_id_p = session_id_p
    self._computation_id_p = computation_id_p
    self._channel = channel
    self._target_fetch_paths = target_fetch_paths
    self._final_unpack = final_unpack
    self._return_mode = return_mode
    # All the results that we have received so far.
    self._results = {}

  def values(self):
    """ Returns the fetches (or the unique fetch if there is only one).

    Blocks until the fetches are available or until an error is raised.
    """
    while not self._values():
      self._progress()
    return self._values()

  def _values(self):
    # Returns the values if they are all done, None otherwise.
    res = []
    for p in self._target_fetch_paths:
      if p not in self._results:
        return None
      cr = self._results[p]
      if cr.final_error:
        raise Exception(cr.final_error)
      elif cr.final_result:
        res.append(CellWithType(cr.final_result))
      else:
        return None
    if self._final_unpack:
      res = res[0]
    if self._return_mode == 'proto':
      return res
    if self._return_mode == 'python':
      return as_python_object(res)

  def _progress(self):
    # Read one more value from the channel.
    csr = next(self._channel)
    print("channel: got value", type(csr), csr)
    if csr.start_graph:
      print("channel: received graph (discarding)")
    if csr.pinned_graph:
      print("channel: received pinned graph (discarding)")
    if csr.results:
      for res in csr.results.results:
        assert res.local_path, (res, csr)
        path = Path(res.local_path)
        if path not in self._results:
          self._results[path] = computation_pb2.ComputationResult()
        current = self._results[path]
        current.MergeFrom(res)
