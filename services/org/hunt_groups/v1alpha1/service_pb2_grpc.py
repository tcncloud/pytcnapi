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
        self.CopyHuntGroupToOrganization = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupToOrganization',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationResponse.FromString,
                )
        self.AdminCopyHuntGroupToOrganization = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AdminCopyHuntGroupToOrganization',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationResponse.FromString,
                )
        self.AdminListHuntGroups = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AdminListHuntGroups',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsResponse.FromString,
                )
        self.ListAgentScripts = channel.unary_stream(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListAgentScripts',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsResponse.FromString,
                )
        self.CreateAgentClientInfoDisplayTemplate = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CreateAgentClientInfoDisplayTemplate',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateResponse.FromString,
                )
        self.UpdateAgentClientInfoDisplayTemplate = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateAgentClientInfoDisplayTemplate',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateResponse.FromString,
                )
        self.GetAgentClientInfoDisplayTemplate = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/GetAgentClientInfoDisplayTemplate',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateResponse.FromString,
                )
        self.ListAgentClientInfoDisplayTemplates = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListAgentClientInfoDisplayTemplates',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesResponse.FromString,
                )
        self.DeleteAgentClientInfoDisplayTemplate = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/DeleteAgentClientInfoDisplayTemplate',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateResponse.FromString,
                )
        self.AssignAgentClientInfoDisplayTemplateToHuntGroups = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AssignAgentClientInfoDisplayTemplateToHuntGroups',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsResponse.FromString,
                )
        self.UnassignAgentClientInfoDisplayTemplateFromHuntGroups = channel.unary_unary(
                '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UnassignAgentClientInfoDisplayTemplateFromHuntGroups',
                request_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsResponse.FromString,
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
        Agent Trigger


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

    def CopyHuntGroupToOrganization(self, request, context):
        """
        Hunt Group


        CopyHuntGroupToOrganization copies a hunt group to a different organization.
        The destination organization must be a child of the source organization.
        This would create a new hunt group in the destination organization with the same
        settings/parameters and all associated data (skill, call-queue config) as the source hunt group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdminCopyHuntGroupToOrganization(self, request, context):
        """AdminCopyHuntGroupToOrganization copies a hunt group to a different organization.
        This will create a new hunt group in the destination organization with the same
        settings/parameters and all associated data (skill, call-queue config) as the source hunt group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdminListHuntGroups(self, request, context):
        """AdminListHuntGroups returns a list of hunt groups for the given organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAgentScripts(self, request, context):
        """ListAgentScripts returns a list of agent scripts for the given organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAgentClientInfoDisplayTemplate(self, request, context):
        """CreateAgentClientInfoDisplayTemplate persists the given template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAgentClientInfoDisplayTemplate(self, request, context):
        """UpdateAgentClientInfoDisplayTemplate persists changes to the given template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentClientInfoDisplayTemplate(self, request, context):
        """GetAgentClientInfoDisplayTemplate returns requested template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAgentClientInfoDisplayTemplates(self, request, context):
        """ListAgentClientInfoDisplayTemplates returns org related templates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAgentClientInfoDisplayTemplate(self, request, context):
        """DeleteAgentClientInfoDisplayTemplate removes the requested template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignAgentClientInfoDisplayTemplateToHuntGroups(self, request, context):
        """AssignAgentClientInfoDisplayTemplateToHuntGroups assigns a display template to the specified groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnassignAgentClientInfoDisplayTemplateFromHuntGroups(self, request, context):
        """UnassignAgentClientInfoDisplayTemplateFromHuntGroups removes display templates from the specified groups.
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
            'CopyHuntGroupToOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyHuntGroupToOrganization,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationResponse.SerializeToString,
            ),
            'AdminCopyHuntGroupToOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.AdminCopyHuntGroupToOrganization,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationResponse.SerializeToString,
            ),
            'AdminListHuntGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.AdminListHuntGroups,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsResponse.SerializeToString,
            ),
            'ListAgentScripts': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAgentScripts,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsResponse.SerializeToString,
            ),
            'CreateAgentClientInfoDisplayTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAgentClientInfoDisplayTemplate,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateResponse.SerializeToString,
            ),
            'UpdateAgentClientInfoDisplayTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAgentClientInfoDisplayTemplate,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateResponse.SerializeToString,
            ),
            'GetAgentClientInfoDisplayTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentClientInfoDisplayTemplate,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateResponse.SerializeToString,
            ),
            'ListAgentClientInfoDisplayTemplates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAgentClientInfoDisplayTemplates,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesResponse.SerializeToString,
            ),
            'DeleteAgentClientInfoDisplayTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAgentClientInfoDisplayTemplate,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateResponse.SerializeToString,
            ),
            'AssignAgentClientInfoDisplayTemplateToHuntGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignAgentClientInfoDisplayTemplateToHuntGroups,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsResponse.SerializeToString,
            ),
            'UnassignAgentClientInfoDisplayTemplateFromHuntGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.UnassignAgentClientInfoDisplayTemplateFromHuntGroups,
                    request_deserializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsRequest.FromString,
                    response_serializer=services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsResponse.SerializeToString,
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

    @staticmethod
    def CopyHuntGroupToOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CopyHuntGroupToOrganization',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CopyHuntGroupToOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AdminCopyHuntGroupToOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AdminCopyHuntGroupToOrganization',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminCopyHuntGroupToOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AdminListHuntGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AdminListHuntGroups',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AdminListHuntGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAgentScripts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListAgentScripts',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentScriptsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAgentClientInfoDisplayTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/CreateAgentClientInfoDisplayTemplate',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.CreateAgentClientInfoDisplayTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAgentClientInfoDisplayTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UpdateAgentClientInfoDisplayTemplate',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UpdateAgentClientInfoDisplayTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentClientInfoDisplayTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/GetAgentClientInfoDisplayTemplate',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.GetAgentClientInfoDisplayTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAgentClientInfoDisplayTemplates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/ListAgentClientInfoDisplayTemplates',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.ListAgentClientInfoDisplayTemplatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAgentClientInfoDisplayTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/DeleteAgentClientInfoDisplayTemplate',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.DeleteAgentClientInfoDisplayTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignAgentClientInfoDisplayTemplateToHuntGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/AssignAgentClientInfoDisplayTemplateToHuntGroups',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.AssignAgentClientInfoDisplayTemplateToHuntGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnassignAgentClientInfoDisplayTemplateFromHuntGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.hunt_groups.v1alpha1.HuntGroupsService/UnassignAgentClientInfoDisplayTemplateFromHuntGroups',
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsRequest.SerializeToString,
            services_dot_org_dot_hunt__groups_dot_v1alpha1_dot_entities__pb2.UnassignAgentClientInfoDisplayTemplateFromHuntGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
