# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import advanced_pb2 as advanced__pb2


class HelloStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.stream_stream(
        '/advance.Hello/Echo',
        request_serializer=advanced__pb2.Request.SerializeToString,
        response_deserializer=advanced__pb2.Response.FromString,
        )


class HelloServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Echo(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.stream_stream_rpc_method_handler(
          servicer.Echo,
          request_deserializer=advanced__pb2.Request.FromString,
          response_serializer=advanced__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'advance.Hello', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
