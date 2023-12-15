# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.omnichannel.oauth.v1alpha1 import entities_pb2 as services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2


class OauthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConnectedInboxOAuthURL = channel.unary_unary(
                '/services.omnichannel.oauth.v1alpha1.OauthService/GetConnectedInboxOAuthURL',
                request_serializer=services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLRequest.SerializeToString,
                response_deserializer=services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLResponse.FromString,
                )


class OauthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetConnectedInboxOAuthURL(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OauthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConnectedInboxOAuthURL': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConnectedInboxOAuthURL,
                    request_deserializer=services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLRequest.FromString,
                    response_serializer=services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.omnichannel.oauth.v1alpha1.OauthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OauthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetConnectedInboxOAuthURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.omnichannel.oauth.v1alpha1.OauthService/GetConnectedInboxOAuthURL',
            services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLRequest.SerializeToString,
            services_dot_omnichannel_dot_oauth_dot_v1alpha1_dot_entities__pb2.GetConnectedInboxOAuthURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)