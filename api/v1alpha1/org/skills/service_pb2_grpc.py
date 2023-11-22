# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.org.skills import entities_pb2 as api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2


class SkillsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSkillGroup = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/CreateSkillGroup',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupResponse.FromString,
                )
        self.ListSkillGroups = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/ListSkillGroups',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsResponse.FromString,
                )
        self.UpdateSkillGroup = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/UpdateSkillGroup',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupResponse.FromString,
                )
        self.GetSkillGroup = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/GetSkillGroup',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupResponse.FromString,
                )
        self.DeleteSkillGroup = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/DeleteSkillGroup',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupResponse.FromString,
                )
        self.AssignSkillGroups = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/AssignSkillGroups',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsResponse.FromString,
                )
        self.RevokeSkillGroups = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/RevokeSkillGroups',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsResponse.FromString,
                )
        self.GetUserSkillGroups = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/GetUserSkillGroups',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsResponse.FromString,
                )
        self.GetUserSkills = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/GetUserSkills',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsResponse.FromString,
                )
        self.GetSkillGroupMembers = channel.unary_unary(
                '/api.v1alpha1.org.skills.SkillsService/GetSkillGroupMembers',
                request_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersResponse.FromString,
                )


class SkillsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSkillGroup(self, request, context):
        """CreateSkillGroup creates a new skill group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSkillGroups(self, request, context):
        """ListSkillGroups lists the skill groups belonging to an organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSkillGroup(self, request, context):
        """UpdateSkillGroup updates a single skill group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSkillGroup(self, request, context):
        """GetSkillGroup gets a single skill group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSkillGroup(self, request, context):
        """DeleteSkillGroup deletes a skill group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignSkillGroups(self, request, context):
        """AssignSkillGroups assigns a user to the given skill groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeSkillGroups(self, request, context):
        """RevokeSkillGroups revokes the given skill groups from a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserSkillGroups(self, request, context):
        """GetUserSkillGroups gets the skill groups assigned to a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserSkills(self, request, context):
        """GetUserSkills gets a user's skill proficiencies.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSkillGroupMembers(self, request, context):
        """GetSkillGroupMembers gets the members of a skill group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SkillsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSkillGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSkillGroup,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupResponse.SerializeToString,
            ),
            'ListSkillGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSkillGroups,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsResponse.SerializeToString,
            ),
            'UpdateSkillGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSkillGroup,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupResponse.SerializeToString,
            ),
            'GetSkillGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSkillGroup,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupResponse.SerializeToString,
            ),
            'DeleteSkillGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSkillGroup,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupResponse.SerializeToString,
            ),
            'AssignSkillGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignSkillGroups,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsResponse.SerializeToString,
            ),
            'RevokeSkillGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeSkillGroups,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsResponse.SerializeToString,
            ),
            'GetUserSkillGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserSkillGroups,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsResponse.SerializeToString,
            ),
            'GetUserSkills': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserSkills,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsResponse.SerializeToString,
            ),
            'GetSkillGroupMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSkillGroupMembers,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.org.skills.SkillsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SkillsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSkillGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/CreateSkillGroup',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.CreateSkillGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSkillGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/ListSkillGroups',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.ListSkillGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSkillGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/UpdateSkillGroup',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.UpdateSkillGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSkillGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/GetSkillGroup',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSkillGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/DeleteSkillGroup',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.DeleteSkillGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignSkillGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/AssignSkillGroups',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.AssignSkillGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeSkillGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/RevokeSkillGroups',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.RevokeSkillGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserSkillGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/GetUserSkillGroups',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserSkills(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/GetUserSkills',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetUserSkillsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSkillGroupMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.skills.SkillsService/GetSkillGroupMembers',
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2.GetSkillGroupMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)