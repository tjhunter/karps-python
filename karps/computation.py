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

  def __init__(self, sessionId, computationId, channel):
    self.sessionId = sessionId
    self.computationId = computationId
    self._channel = channel
