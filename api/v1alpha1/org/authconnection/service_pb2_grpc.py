# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.org.authconnection import entities_pb2 as api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2


class AuthConnectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAuthConnection = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/CreateAuthConnection',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionResponse.FromString,
                )
        self.ListAuthConnectionIds = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/ListAuthConnectionIds',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsResponse.FromString,
                )
        self.GetAuthConnectionSettings = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/GetAuthConnectionSettings',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsResponse.FromString,
                )
        self.GetAuthConnection = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/GetAuthConnection',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionResponse.FromString,
                )
        self.DeleteAuthConnection = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/DeleteAuthConnection',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionResponse.FromString,
                )
        self.UpdateAuthConnectionSecret = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/UpdateAuthConnectionSecret',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretResponse.FromString,
                )
        self.UpdateAuthConnectionGroups = channel.unary_unary(
                '/api.v1alpha1.org.authconnection.AuthConnectionService/UpdateAuthConnectionGroups',
                request_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsResponse.FromString,
                )


class AuthConnectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAuthConnection(self, request, context):
        """CreateAuthConnection creates a new auth0 connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAuthConnectionIds(self, request, context):
        """ListAuthConnectionIds returns the IDs of all authconnections belonging to the current org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuthConnectionSettings(self, request, context):
        """GetAuthConnectionSettings gets auth connection settings.
        DEPRECATED: use GetAuthConnection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuthConnection(self, request, context):
        """GetAuthConnection gets an existing auth connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAuthConnection(self, request, context):
        """DeleteAuthConnection removes the current orgs auth settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAuthConnectionSecret(self, request, context):
        """UpdateAuthConnectionSecret updates a connections secret.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAuthConnectionGroups(self, request, context):
        """UpdateAuthConnectionGroups updates a connections groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAuthConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAuthConnection,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionResponse.SerializeToString,
            ),
            'ListAuthConnectionIds': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAuthConnectionIds,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsResponse.SerializeToString,
            ),
            'GetAuthConnectionSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthConnectionSettings,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsResponse.SerializeToString,
            ),
            'GetAuthConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthConnection,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionResponse.SerializeToString,
            ),
            'DeleteAuthConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAuthConnection,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionResponse.SerializeToString,
            ),
            'UpdateAuthConnectionSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAuthConnectionSecret,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretResponse.SerializeToString,
            ),
            'UpdateAuthConnectionGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAuthConnectionGroups,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.org.authconnection.AuthConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthConnectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAuthConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/CreateAuthConnection',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.CreateAuthConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAuthConnectionIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/ListAuthConnectionIds',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.ListAuthConnectionIdsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuthConnectionSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/GetAuthConnectionSettings',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionSettingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuthConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/GetAuthConnection',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.GetAuthConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAuthConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/DeleteAuthConnection',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.DeleteAuthConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAuthConnectionSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/UpdateAuthConnectionSecret',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionSecretResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAuthConnectionGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.authconnection.AuthConnectionService/UpdateAuthConnectionGroups',
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2.UpdateAuthConnectionGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
