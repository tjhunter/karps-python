

import grpc

from .proto import types_pb2
from .proto import interface_pb2_grpc
from .proto import interface_pb2
from .proto.computation_pb2 import SessionId


class Session(object):
  """ A session in Karps.

  A session encapsulates all the state that is communicated between the frontend and the backend.
  """

  def __init__(self, name, stub):
    self._stub = stub
    self.name = name
    self.computation_counter = 0

  def __repr__(self):
    return "Session:{}".format(self.name)

  def value(self, path, computation = None):
    """ Retrieves a single value with the given path.
    If no computation is specified, it will try to retrieve the latest 
    value that corresponds to this path.
    """
    pass

  def pandas(self, path, computation = None):
    """ Retrieves a single value with the given path, and returns it as 
    a Pandas dataframe.
    If the data is scalar, it is returned as a scala. If the data is a
    collection of scalar values, they are returned as a Pandas Series.
    Otherwise, they are returned as a Pandas dataframe.
    """
    pass

  def run(self, fetches, feed_dict=None):
    """ Blocks until all the fetches are executed.
    """
    pass

  def compute(self, fetches, feed_dict=None):
    """ Executes the fetches in an asynchronous manner.
    """
    pass

def session(name, port = 8082, address = "localhost"):
  """ Creates a new remote session that uses the GRPC interface to communicate with the frontend.
  """
  channel = grpc.insecure_channel('{}:{}'.format(address, str(port)))
  stub = interface_pb2_grpc.KarpsMainStub(channel)
  sessionId = SessionId(id="session")
  # Make sure that the session exists before returning it.
  z = stub.CreateSession(interface_pb2.CreateSessionRequest(requested_session=sessionId))
  return KrapsSession(name, stub)
