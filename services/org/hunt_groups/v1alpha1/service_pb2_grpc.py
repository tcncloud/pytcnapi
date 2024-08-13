# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.org.hunt_groups.v1alpha1 import entities_pb2 as services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2


class HuntGroupsServiceStub(object):
    """HuntGroupsService is the service for managing hunt groups and their related entities.

    Exile Link

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
        self.CopyHuntGroupExileLink = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupExileLink',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkResponse.FromString,
                )
        self.UpdateHuntGroupExileLinks = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateHuntGroupExileLinks',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksResponse.FromString,
                )
        self.ListHuntGroupAgentTriggers = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListHuntGroupAgentTriggers',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersResponse.FromString,
                )
        self.CopyHuntGroupAgentTrigger = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupAgentTrigger',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerResponse.FromString,
                )
        self.UpdateHuntGroupAgentTriggers = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateHuntGroupAgentTriggers',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersResponse.FromString,
                )


class HuntGroupsServiceServicer(object):
    """HuntGroupsService is the service for managing hunt groups and their related entities.

    Exile Link

    """

    def ListHuntGroupExileLinks(self, request, context):
        """ListHuntGroupExileLinks returns a list of Exile links for a given hunt group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyHuntGroupExileLink(self, request, context):
        """CopyHuntGroupExileLink copies an exile link from one hunt group to another.
        It will create a new exile link in the destination hunt group with the same
        settings/parameters as the source exile link.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHuntGroupExileLinks(self, request, context):
        """UpdateHuntGroupExileLinks updates the exile links for a hunt group.
        It will create any new exile links that do not already exist in the hunt group,
        update any existing exile links with the new settings/parameters, and
        delete any exile links that are not in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHuntGroupAgentTriggers(self, request, context):
        """
        Agent Triggers


        ListHuntGroupAgentTriggers returns a list of agent triggers for the given hunt group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyHuntGroupAgentTrigger(self, request, context):
        """CopyHuntGroupAgentTrigger copys an agent trigger to the given hunt group in the same org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHuntGroupAgentTriggers(self, request, context):
        """UpdateHuntGroupAgentTriggers updates all agent triggers for the given hunt group.
        """
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
            'CopyHuntGroupExileLink': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyHuntGroupExileLink,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkResponse.SerializeToString,
            ),
            'UpdateHuntGroupExileLinks': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHuntGroupExileLinks,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksResponse.SerializeToString,
            ),
            'ListHuntGroupAgentTriggers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHuntGroupAgentTriggers,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersResponse.SerializeToString,
            ),
            'CopyHuntGroupAgentTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyHuntGroupAgentTrigger,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerResponse.SerializeToString,
            ),
            'UpdateHuntGroupAgentTriggers': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHuntGroupAgentTriggers,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.org.hunt_groups.v1alpha1.HuntGroupsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HuntGroupsService(object):
    """HuntGroupsService is the service for managing hunt groups and their related entities.

    Exile Link

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

    @staticmethod
    def CopyHuntGroupExileLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupExileLink',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupExileLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateHuntGroupExileLinks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateHuntGroupExileLinks',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupExileLinksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListHuntGroupAgentTriggers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListHuntGroupAgentTriggers',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListHuntGroupAgentTriggersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CopyHuntGroupAgentTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupAgentTrigger',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupAgentTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateHuntGroupAgentTriggers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateHuntGroupAgentTriggers',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateHuntGroupAgentTriggersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
