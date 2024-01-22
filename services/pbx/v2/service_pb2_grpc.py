# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.pbx.v2 import service_pb2 as services_dot_pbx_dot_v2_dot_service__pb2


class PBXServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPBXUsers = channel.unary_unary(
                '/services.pbx.v2.PBXService/ListPBXUsers',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersResponse.FromString,
                )
        self.GetPBXUser = channel.unary_unary(
                '/services.pbx.v2.PBXService/GetPBXUser',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserResponse.FromString,
                )
        self.ListRingGroups = channel.unary_unary(
                '/services.pbx.v2.PBXService/ListRingGroups',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsResponse.FromString,
                )
        self.GetRingGroup = channel.unary_unary(
                '/services.pbx.v2.PBXService/GetRingGroup',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupResponse.FromString,
                )
        self.UpdateSIPAccount = channel.unary_unary(
                '/services.pbx.v2.PBXService/UpdateSIPAccount',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountResponse.FromString,
                )
        self.UpdateRingGroup = channel.unary_unary(
                '/services.pbx.v2.PBXService/UpdateRingGroup',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupResponse.FromString,
                )
        self.CreateRingGroup = channel.unary_unary(
                '/services.pbx.v2.PBXService/CreateRingGroup',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupResponse.FromString,
                )
        self.DeleteRingGroup = channel.unary_unary(
                '/services.pbx.v2.PBXService/DeleteRingGroup',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupResponse.FromString,
                )
        self.AssignRandomExtension = channel.unary_unary(
                '/services.pbx.v2.PBXService/AssignRandomExtension',
                request_serializer=services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionRequest.SerializeToString,
                response_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionResponse.FromString,
                )


class PBXServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListPBXUsers(self, request, context):
        """Returns details of all PBX Users associated with the authenticated callers ORG
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPBXUser(self, request, context):
        """Returns details of the PBX User associated with the pbx_user_id
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The request is invalid.
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.NotFound: The user does not exist or is not in the caller's ORG.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRingGroups(self, request, context):
        """Returns details of all Ring Groups associated with the authenticated callers ORG
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRingGroup(self, request, context):
        """Returns details of the Ring Group associated with the ring_group_id
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The request is invalid.
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.NotFound: The group does not exist or is not in the caller's ORG.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSIPAccount(self, request, context):
        """Updates details of the SIP Account for the specific SIP Account within the authenticated callers ORG.
        Allows for updating, activating, and deactivating a user.
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The request is invalid.
        - grpc.AlreadyExists: The extension already exists
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRingGroup(self, request, context):
        """Updates details of a Ring Group for the authenticated callers ORG. This operation acts as an "upsert".
        - If the groupID is in the update mask and the group exists, the group will be updated.
        - If the groupID is not in the update mask a group will be created.
        Allows for creating and updating a ring group.
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The request is invalid.
        - grpc.AlreadyExists: The extension or name already exists.
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRingGroup(self, request, context):
        """Creates a ring group for the authenticated caller's ORG.
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The request is invalid.
        - grpc.OutOfRange: The request has fields that are out of range of constraints
        - grpc.AlreadyExists: The extension or name already exists.
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRingGroup(self, request, context):
        """Deletes a specific Ring Group for the authenticated caller's ORG.
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.InvalidArgument: The groupID is an invalid format.
        - grpc.NotFound: The group does not exist or is not in the caller's ORG.
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignRandomExtension(self, request, context):
        """Assigns a random extension either to a PBX user or a Ring Group
        Required permissions:
        PBX-MANAGER
        Errors:
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.NotFound: No free extension found.
        - grpc.Internal: An internal error occurred.
        - grpc.Unavailable: The operation is currently unavailable. Likely a transient issue with a downstream service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PBXServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPBXUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPBXUsers,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersResponse.SerializeToString,
            ),
            'GetPBXUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPBXUser,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserResponse.SerializeToString,
            ),
            'ListRingGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRingGroups,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsResponse.SerializeToString,
            ),
            'GetRingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRingGroup,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupResponse.SerializeToString,
            ),
            'UpdateSIPAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSIPAccount,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountResponse.SerializeToString,
            ),
            'UpdateRingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRingGroup,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupResponse.SerializeToString,
            ),
            'CreateRingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRingGroup,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupResponse.SerializeToString,
            ),
            'DeleteRingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRingGroup,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupResponse.SerializeToString,
            ),
            'AssignRandomExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignRandomExtension,
                    request_deserializer=services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionRequest.FromString,
                    response_serializer=services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.pbx.v2.PBXService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PBXService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListPBXUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/ListPBXUsers',
            services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.ListPBXUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPBXUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/GetPBXUser',
            services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.GetPBXUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRingGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/ListRingGroups',
            services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.ListRingGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/GetRingGroup',
            services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.GetRingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSIPAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/UpdateSIPAccount',
            services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.UpdateSIPAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/UpdateRingGroup',
            services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.UpdateRingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/CreateRingGroup',
            services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.CreateRingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/DeleteRingGroup',
            services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.DeleteRingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignRandomExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.pbx.v2.PBXService/AssignRandomExtension',
            services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionRequest.SerializeToString,
            services_dot_pbx_dot_v2_dot_service__pb2.AssignRandomExtensionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
