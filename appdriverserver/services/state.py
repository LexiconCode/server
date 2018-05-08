import appdriverserver.grpcs.state_pb2_grpc as state_pb2_grpc

from appdriverserver.grpcs.state_pb2 import *
from appdriverserver.server import server


class State(state_pb2_grpc.StateServicer):
    def GetState(self, request, context):
        response = StateInfo(app = StateInfo.App(executable='test'))
        return response

    @staticmethod
    def serve():
        state_pb2_grpc.add_StateServicer_to_server(State(), server)
