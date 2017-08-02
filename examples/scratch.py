import grpc

from karps.proto import interface_pb2_grpc

channel = grpc.insecure_channel('localhost:8082')
stub = interface_pb2_grpc.KarpsMainStub(channel)