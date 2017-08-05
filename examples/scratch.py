import grpc

from karps.proto import interface_pb2_grpc
from karps.proto import interface_pb2
from karps.proto.computation_pb2 import SessionId


import karps as ks
import karps.functions as f

df = ks.dataframe([(1,)], schema="ee")
print(df)
ct = f.collect(df)
print(ct)

print(df.ee)

print(ks.dataframe([(1,)], schema="ee"))
print(ks.dataframe([[1]], schema="ee"))
print(ks.dataframe([(1,)], schema=["ee"]))
print(ks.dataframe([(1,)]))

df = ks.dataframe([1,2,3], name="df")
#df2 = df / f.max(df)

with ks.scope("scope1"):
  df = ks.dataframe([1,2,3], name="df")
  print(df)
  ct = f.collect(df)
  print(ct)

s = ks.session("test")
comp = s.run(ct)
print(comp.values())

# channel = grpc.insecure_channel('localhost:8082')
# stub = interface_pb2_grpc.KarpsMainStub(channel)

# sessionId = SessionId(id="session")

# z = stub.CreateSession(interface_pb2.CreateSessionRequest(requested_session=sessionId))

