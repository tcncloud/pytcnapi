# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.org.legacy import entities_pb2 as api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2


class OrgLegacyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterOrganization = channel.unary_unary(
                '/api.v1alpha1.org.legacy.OrgLegacy/RegisterOrganization',
                request_serializer=api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationResponse.FromString,
                )


class OrgLegacyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterOrganization(self, request, context):
        """Registers a new organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrgLegacyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterOrganization,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.org.legacy.OrgLegacy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrgLegacy(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.legacy.OrgLegacy/RegisterOrganization',
            api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2.RegisterOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
