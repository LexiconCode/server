import grpc

import appdriverserver.grpcs.state_pb2_grpc as state_pb2_grpc
import appdriverserver.grpcs.state_pb2 as state_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = state_pb2_grpc.StateStub(channel)

# create a valid request message
filter = state_pb2.StateFilter()

# make the call
response = stub.GetState(filter)

print(response.app.executable)