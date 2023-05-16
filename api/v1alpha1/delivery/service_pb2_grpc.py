# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.delivery import service_pb2 as api_dot_v1alpha1_dot_delivery_dot_service__pb2


class DeliveryApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTransferConfig = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/CreateTransferConfig',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigRes.FromString,
                )
        self.ListTransferConfigs = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/ListTransferConfigs',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsRes.FromString,
                )
        self.ListTransferConfigsByCredentialID = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/ListTransferConfigsByCredentialID',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDRes.FromString,
                )
        self.UpdateTransferConfig = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/UpdateTransferConfig',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigRes.FromString,
                )
        self.DeleteTransferConfig = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/DeleteTransferConfig',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigRes.FromString,
                )
        self.GetTransferConfig = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/GetTransferConfig',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigRes.FromString,
                )
        self.GetTransferConfigByName = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/GetTransferConfigByName',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameRes.FromString,
                )
        self.ListHistory = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/ListHistory',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryRes.FromString,
                )
        self.ListHistoryByTransferConfig = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/ListHistoryByTransferConfig',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigRes.FromString,
                )
        self.ListCredentials = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/ListCredentials',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsRes.FromString,
                )
        self.GetCredential = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/GetCredential',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialRes.FromString,
                )
        self.CreateCredential = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/CreateCredential',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialRes.FromString,
                )
        self.DeleteCredential = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/DeleteCredential',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialRes.FromString,
                )
        self.UpdateCredential = channel.unary_unary(
                '/api.v1alpha1.delivery.DeliveryApi/UpdateCredential',
                request_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialRes.FromString,
                )


class DeliveryApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTransferConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransferConfigs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransferConfigsByCredentialID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTransferConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTransferConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransferConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransferConfigByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListHistoryByTransferConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCredentials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCredential(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCredential(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCredential(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCredential(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeliveryApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTransferConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTransferConfig,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigRes.SerializeToString,
            ),
            'ListTransferConfigs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTransferConfigs,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsRes.SerializeToString,
            ),
            'ListTransferConfigsByCredentialID': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTransferConfigsByCredentialID,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDRes.SerializeToString,
            ),
            'UpdateTransferConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTransferConfig,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigRes.SerializeToString,
            ),
            'DeleteTransferConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTransferConfig,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigRes.SerializeToString,
            ),
            'GetTransferConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransferConfig,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigRes.SerializeToString,
            ),
            'GetTransferConfigByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransferConfigByName,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameRes.SerializeToString,
            ),
            'ListHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHistory,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryRes.SerializeToString,
            ),
            'ListHistoryByTransferConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.ListHistoryByTransferConfig,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigRes.SerializeToString,
            ),
            'ListCredentials': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCredentials,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsRes.SerializeToString,
            ),
            'GetCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCredential,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialRes.SerializeToString,
            ),
            'CreateCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCredential,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialRes.SerializeToString,
            ),
            'DeleteCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCredential,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialRes.SerializeToString,
            ),
            'UpdateCredential': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCredential,
                    request_deserializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.delivery.DeliveryApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeliveryApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTransferConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/CreateTransferConfig',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateTransferConfigRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTransferConfigs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/ListTransferConfigs',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTransferConfigsByCredentialID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/ListTransferConfigsByCredentialID',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListTransferConfigsByCredentialIDRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTransferConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/UpdateTransferConfig',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateTransferConfigRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTransferConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/DeleteTransferConfig',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteTransferConfigRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransferConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/GetTransferConfig',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransferConfigByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/GetTransferConfigByName',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetTransferConfigByNameRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/ListHistory',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListHistoryByTransferConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/ListHistoryByTransferConfig',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListHistoryByTransferConfigRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCredentials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/ListCredentials',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.ListCredentialsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/GetCredential',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.GetCredentialRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/CreateCredential',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.CreateCredentialRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/DeleteCredential',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.DeleteCredentialRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCredential(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.delivery.DeliveryApi/UpdateCredential',
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialReq.SerializeToString,
            api_dot_v1alpha1_dot_delivery_dot_service__pb2.UpdateCredentialRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
