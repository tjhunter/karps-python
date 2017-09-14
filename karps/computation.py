""" An asynchronous computation.
"""
import logging

from .proto import computation_pb2
from .utils import Path
from .row import CellWithType, as_python_object

__all__ = ['Computation']

logger = logging.getLogger('karps')

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
    # The proto of the session id.
    self._session_id_p = session_id_p
    # The proto of the computation id
    self._computation_id_p = computation_id_p
    # The GRPC channel
    self._channel = channel
    # The paths to fetch (list of strings)
    self._target_fetch_paths = target_fetch_paths
    # Bool, indicates wether the head of the list should be returned.
    self._final_unpack = final_unpack
    # The return mode for deserializing the data.
    self._return_mode = return_mode
    # All the results that we have received so far.
    self._results = {}
    # The compilation phases.
    self._compilation_phases = None

  def values(self):
    """ Returns the fetches (or the unique fetch if there is only one).

    Blocks until the fetches are available or until an error is raised.
    """
    while not self._values():
      self._progress()
    return self._values()

  def compiler_step(self, step_name):
    """ Returns the given compiler phase.
    """
    while self._compilation_phases is None:
      self._progress()
    for comp_phase in self._compilation_phases:
      if comp_phase.phase_name.lower() == step_name.lower():
        return comp_phase
    step_names = [comp_phase.phase_name for comp_phase in self._compilation_phases]
    logger.warn("Could not find compiler step %s. Available steps are %s", step_name, step_names)
    return None

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
    """ Attempts to make progress by blocking on the connection until an update is received.
    """
    logger.debug("Calling _progress")
    # Read one more value from the channel.
    csr = next(self._channel)
    #logger.debug("channel: got value %s: %s", type(csr), str(csr))
    if csr.HasField("start_graph"):
      logger.debug("channel: received graph (discarding)")
    if csr.HasField("pinned_graph"):
      logger.debug("channel: received pinned graph (discarding)")
    if csr.HasField("compilation_result"):
      logger.debug("channel: received compilation results")
      # Did we receive some steps?
      if csr.compilation_result.compilation_graph:
        logger.debug("channel: received compilation steps")
        self._compilation_phases = csr.compilation_result.compilation_graph
    if csr.results:
      for res in csr.results.results:
        assert res.local_path, (res, csr)
        path = Path(res.local_path)
        logger.debug("channel: received result for %s" % path)
        if path not in self._results:
          self._results[path] = computation_pb2.ComputationResult()
        current = self._results[path]
        current.MergeFrom(res)
