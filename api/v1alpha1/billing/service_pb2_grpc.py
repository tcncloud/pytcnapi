# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.billing import entities_pb2 as api_dot_v1alpha1_dot_billing_dot_entities__pb2


class BillingStub(object):
    """Billing service for handling billing requests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBillingPlan = channel.unary_unary(
                '/api.v1alpha1.billing.Billing/CreateBillingPlan',
                request_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanRes.FromString,
                )
        self.GetBillingPlan = channel.unary_unary(
                '/api.v1alpha1.billing.Billing/GetBillingPlan',
                request_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanRes.FromString,
                )
        self.UpdateBillingPlan = channel.unary_unary(
                '/api.v1alpha1.billing.Billing/UpdateBillingPlan',
                request_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanRes.FromString,
                )
        self.DeleteBillingDetails = channel.unary_unary(
                '/api.v1alpha1.billing.Billing/DeleteBillingDetails',
                request_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsRes.FromString,
                )
        self.GetInvoice = channel.unary_unary(
                '/api.v1alpha1.billing.Billing/GetInvoice',
                request_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceRes.FromString,
                )


class BillingServicer(object):
    """Billing service for handling billing requests.
    """

    def CreateBillingPlan(self, request, context):
        """CreateBillingPlan - saves the provided billing plan, and returns the saved
        plan. However, in an organization's Billing Plan there can only ever be
        one billing detail with a specific config type and event type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBillingPlan(self, request, context):
        """GetBillingPlan - returns the billing plan for the provided organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBillingPlan(self, request, context):
        """UpdateBillingPlan - updates the provided billing plan and it's details.
        If some details are not provided, they will be left as is. However, if
        deletion is desired, the DeleteBillingDetails method should be used. The
        billing plan still follows the constraint of only having one billing detail
        with a specific config type and event type, and so if the request contains
        more than one billing detail with a config type and event type, the request
        is malformed and will result in potentially unexpected behavior.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBillingDetails(self, request, context):
        """DeleteBillingDetails - deletes the provided billing details. If the billing
        details do not exist, this won't do anything.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInvoice(self, request, context):
        """GetInvoice - returns the invoice for the organization. If a date is
        provided, this will return the invoice for the organization that
        corresponds to the billing cycle that contains the provided date. If
        no date is provided, this will return the invoice as it currently
        stands for the current billing cycle.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BillingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBillingPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBillingPlan,
                    request_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanRes.SerializeToString,
            ),
            'GetBillingPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBillingPlan,
                    request_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanRes.SerializeToString,
            ),
            'UpdateBillingPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBillingPlan,
                    request_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanRes.SerializeToString,
            ),
            'DeleteBillingDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBillingDetails,
                    request_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsRes.SerializeToString,
            ),
            'GetInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInvoice,
                    request_deserializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.billing.Billing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Billing(object):
    """Billing service for handling billing requests.
    """

    @staticmethod
    def CreateBillingPlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.billing.Billing/CreateBillingPlan',
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanReq.SerializeToString,
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.CreateBillingPlanRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBillingPlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.billing.Billing/GetBillingPlan',
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanReq.SerializeToString,
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetBillingPlanRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBillingPlan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.billing.Billing/UpdateBillingPlan',
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanReq.SerializeToString,
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.UpdateBillingPlanRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBillingDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.billing.Billing/DeleteBillingDetails',
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsReq.SerializeToString,
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.DeleteBillingDetailsRes.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.billing.Billing/GetInvoice',
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceReq.SerializeToString,
            api_dot_v1alpha1_dot_billing_dot_entities__pb2.GetInvoiceRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
