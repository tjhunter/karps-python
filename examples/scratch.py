import grpc

from karps.proto import interface_pb2_grpc
from karps.proto import interface_pb2
from karps.proto.computation_pb2 import SessionId

channel = grpc.insecure_channel('localhost:8082')
stub = interface_pb2_grpc.KarpsMainStub(channel)

sessionId = SessionId(id="session")

z = stub.CreateSession(interface_pb2.CreateSessionRequest(requested_session=sessionId))

