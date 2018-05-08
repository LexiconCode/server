# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import state_pb2 as state__pb2


class StateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetState = channel.unary_unary(
        '/State/GetState',
        request_serializer=state__pb2.StateFilter.SerializeToString,
        response_deserializer=state__pb2.StateInfo.FromString,
        )


class StateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=state__pb2.StateFilter.FromString,
          response_serializer=state__pb2.StateInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'State', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))