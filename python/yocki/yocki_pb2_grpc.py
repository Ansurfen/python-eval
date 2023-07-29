# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import yocki_pb2 as yocki__pb2


class YockInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
            '/Yocki.YockInterface/Ping',
            request_serializer=yocki__pb2.PingRequest.SerializeToString,
            response_deserializer=yocki__pb2.PingResponse.FromString,
        )
        self.Call = channel.unary_unary(
            '/Yocki.YockInterface/Call',
            request_serializer=yocki__pb2.CallRequest.SerializeToString,
            response_deserializer=yocki__pb2.CallResponse.FromString,
        )
        self.Info = channel.unary_unary(
            '/Yocki.YockInterface/Info',
            request_serializer=yocki__pb2.InfoRequest.SerializeToString,
            response_deserializer=yocki__pb2.InfoResponse.FromString,
        )


class YockInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Ping is used to detect whether the connection is available
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YockInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Ping': grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=yocki__pb2.PingRequest.FromString,
            response_serializer=yocki__pb2.PingResponse.SerializeToString,
        ),
        'Call': grpc.unary_unary_rpc_method_handler(
            servicer.Call,
            request_deserializer=yocki__pb2.CallRequest.FromString,
            response_serializer=yocki__pb2.CallResponse.SerializeToString,
        ),
        'Info': grpc.unary_unary_rpc_method_handler(
            servicer.Info,
            request_deserializer=yocki__pb2.InfoRequest.FromString,
            response_serializer=yocki__pb2.InfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Yocki.YockInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class YockInterface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Yocki.YockInterface/Ping',
                                             yocki__pb2.PingRequest.SerializeToString,
                                             yocki__pb2.PingResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Call(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Yocki.YockInterface/Call',
                                             yocki__pb2.CallRequest.SerializeToString,
                                             yocki__pb2.CallResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Info(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Yocki.YockInterface/Info',
                                             yocki__pb2.InfoRequest.SerializeToString,
                                             yocki__pb2.InfoResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
