# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v0alpha import cfg_pb2 as api_dot_v0alpha_dot_cfg__pb2


class CfgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWebAgentConfig = channel.unary_unary(
                '/api.v0alpha.Cfg/GetWebAgentConfig',
                request_serializer=api_dot_v0alpha_dot_cfg__pb2.GetConfigReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_cfg__pb2.WebAgent.FromString,
                )


class CfgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetWebAgentConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CfgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWebAgentConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWebAgentConfig,
                    request_deserializer=api_dot_v0alpha_dot_cfg__pb2.GetConfigReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_cfg__pb2.WebAgent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v0alpha.Cfg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Cfg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetWebAgentConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Cfg/GetWebAgentConfig',
            api_dot_v0alpha_dot_cfg__pb2.GetConfigReq.SerializeToString,
            api_dot_v0alpha_dot_cfg__pb2.WebAgent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
