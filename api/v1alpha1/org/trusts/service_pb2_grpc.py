# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.org import trusts_pb2 as api_dot_v1alpha1_dot_org_dot_trusts__pb2


class TrustsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/CreateTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustResponse.FromString,
                )
        self.AcceptTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/AcceptTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustResponse.FromString,
                )
        self.RejectTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/RejectTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustResponse.FromString,
                )
        self.GetTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/GetTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustResponse.FromString,
                )
        self.ListIncomingTrusts = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/ListIncomingTrusts',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsResponse.FromString,
                )
        self.ListGivenTrusts = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/ListGivenTrusts',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsResponse.FromString,
                )
        self.ListAssignableTrusts = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/ListAssignableTrusts',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsResponse.FromString,
                )
        self.DeleteTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/DeleteTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustResponse.FromString,
                )
        self.AssignTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/AssignTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustResponse.FromString,
                )
        self.UnassignTrust = channel.unary_unary(
                '/api.v1alpha1.org.trusts.TrustsService/UnassignTrust',
                request_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustResponse.FromString,
                )


class TrustsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTrust(self, request, context):
        """CreateTrust creates a new trust.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptTrust(self, request, context):
        """AcceptTrust accepts an incoming trust.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RejectTrust(self, request, context):
        """RejectTrust rejects an incoming trust.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrust(self, request, context):
        """GetTrust returns a single trust by trust id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIncomingTrusts(self, request, context):
        """ListIncomingTrusts returns all pending trusts that are being granted
        to the org of the currently logged in user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListGivenTrusts(self, request, context):
        """ListGivenTrusts returns all trusts that have been given out for
        the currently logged in user's org. The returned list will contain
        accepted, pending, and rejected trusts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAssignableTrusts(self, request, context):
        """ListAssignableTrusts returns all accepted trusts that are being granted
        to the org of the currently logged in user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTrust(self, request, context):
        """DeleteTrust deletes a trust by trust id. Only trusts where the current
        org is the grantor can be deleted by this endpoint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignTrust(self, request, context):
        """AssignTrust assigns a trust to the given user ids.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnassignTrust(self, request, context):
        """UnassignTrust unassigns a trust from the given user id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrustsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustResponse.SerializeToString,
            ),
            'AcceptTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustResponse.SerializeToString,
            ),
            'RejectTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.RejectTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustResponse.SerializeToString,
            ),
            'GetTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustResponse.SerializeToString,
            ),
            'ListIncomingTrusts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListIncomingTrusts,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsResponse.SerializeToString,
            ),
            'ListGivenTrusts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListGivenTrusts,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsResponse.SerializeToString,
            ),
            'ListAssignableTrusts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAssignableTrusts,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsResponse.SerializeToString,
            ),
            'DeleteTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustResponse.SerializeToString,
            ),
            'AssignTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustResponse.SerializeToString,
            ),
            'UnassignTrust': grpc.unary_unary_rpc_method_handler(
                    servicer.UnassignTrust,
                    request_deserializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.org.trusts.TrustsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrustsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/CreateTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.CreateTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/AcceptTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.AcceptTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RejectTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/RejectTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.RejectTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/GetTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.GetTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListIncomingTrusts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/ListIncomingTrusts',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListIncomingTrustsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListGivenTrusts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/ListGivenTrusts',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListGivenTrustsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAssignableTrusts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/ListAssignableTrusts',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.ListAssignableTrustsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/DeleteTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.DeleteTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/AssignTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.AssignTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnassignTrust(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.org.trusts.TrustsService/UnassignTrust',
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustRequest.SerializeToString,
            api_dot_v1alpha1_dot_org_dot_trusts__pb2.UnassignTrustResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)