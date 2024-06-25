# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.integrationspublic import service_pb2 as api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2


class IntegrationsPublicStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLinkData = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetLinkData',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataRes.FromString,
                )
        self.SubmitVerification = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/SubmitVerification',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationRes.FromString,
                )
        self.SessionKeepAlive = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/SessionKeepAlive',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveRes.FromString,
                )
        self.GetInvoice = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetInvoice',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceRes.FromString,
                )
        self.SubmitPayment = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/SubmitPayment',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentRes.FromString,
                )
        self.GetReceipt = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetReceipt',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptRes.FromString,
                )
        self.ProcessWorkflow = channel.unary_unary(
                '/api.v1alpha1.integrationspublic.IntegrationsPublic/ProcessWorkflow',
                request_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowRes.FromString,
                )


class IntegrationsPublicServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLinkData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitVerification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionKeepAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInvoice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitPayment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReceipt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IntegrationsPublicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLinkData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLinkData,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataRes.SerializeToString,
            ),
            'SubmitVerification': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitVerification,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationRes.SerializeToString,
            ),
            'SessionKeepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionKeepAlive,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveRes.SerializeToString,
            ),
            'GetInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInvoice,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceRes.SerializeToString,
            ),
            'SubmitPayment': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitPayment,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentRes.SerializeToString,
            ),
            'GetReceipt': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReceipt,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptRes.SerializeToString,
            ),
            'ProcessWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessWorkflow,
                    request_deserializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.integrationspublic.IntegrationsPublic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IntegrationsPublic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLinkData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetLinkData',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetLinkDataRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitVerification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/SubmitVerification',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitVerificationRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionKeepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/SessionKeepAlive',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SessionKeepAliveRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetInvoice',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetInvoiceRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitPayment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/SubmitPayment',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.SubmitPaymentRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReceipt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/GetReceipt',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.GetReceiptRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessWorkflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.integrationspublic.IntegrationsPublic/ProcessWorkflow',
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowReq.SerializeToString,
            api_dot_v1alpha1_dot_integrationspublic_dot_service__pb2.ProcessWorkflowRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
