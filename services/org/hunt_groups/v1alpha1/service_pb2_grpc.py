# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.org.hunt_groups.v1alpha1 import entities_pb2 as services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2


class HuntGroupsServiceStub(object):
    """HuntGroupsService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListHuntGroupExileLinks = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListHuntGroupExileLinks',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksResponse.FromString,
                )


class HuntGroupsServiceServicer(object):
    """HuntGroupsService
    """

    def ListHuntGroupExileLinks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HuntGroupsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListHuntGroupExileLinks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHuntGroupExileLinks,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.org.hunt_groups.v1alpha1.HuntGroupsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HuntGroupsService(object):
    """HuntGroupsService
    """

    @staticmethod
    def ListHuntGroupExileLinks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListHuntGroupExileLinks',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupExileLinksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
