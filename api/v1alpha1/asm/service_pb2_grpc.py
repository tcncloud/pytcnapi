# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from api.v1alpha1.asm import service_pb2 as api_dot_v1alpha1_dot_asm_dot_service__pb2


class AsmApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/CreateSession',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionRes.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/GetStatus',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusRes.FromString,
                )
        self.EndSession = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/EndSession',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionRes.FromString,
                )
        self.GetCurrentSession = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/GetCurrentSession',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetCurrentSessionReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AsmSession.FromString,
                )
        self.SwitchSubsession = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/SwitchSubsession',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionRes.FromString,
                )
        self.ListConversations = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/ListConversations',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsRes.FromString,
                )
        self.AssignNewConversation = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/AssignNewConversation',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationRes.FromString,
                )
        self.ListAgents = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/ListAgents',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsRes.FromString,
                )
        self.SetConversationCollectedData = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/SetConversationCollectedData',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataReq.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataRes.FromString,
                )
        self.GetQueuesDetails = channel.unary_unary(
                '/api.v1alpha1.asm.AsmApi/GetQueuesDetails',
                request_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetQueuesDetailsReq.SerializeToString,
                response_deserializer=api_dot_commons_dot_omnichannel__pb2.GetQueuesDetailsRes.FromString,
                )


class AsmApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSession(self, request, context):
        """Creates an agent session and enables the voice channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Returns an aggregate of the statuses of all channels
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndSession(self, request, context):
        """Closes an asm session and all sub sessions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCurrentSession(self, request, context):
        """Gets an agent's current asm session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchSubsession(self, request, context):
        """Updates the currently active subsession
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConversations(self, request, context):
        """Lists the conversations for an assigned agent
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignNewConversation(self, request, context):
        """Assign agent to matched conversation based on skills and channelTypes requested
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAgents(self, request, context):
        """List all agents for the given user. Contains statistical enrichments for each agent and their conversations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConversationCollectedData(self, request, context):
        """Set collected data per conversation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetQueuesDetails(self, request, context):
        """Set queue details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AsmApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionRes.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusRes.SerializeToString,
            ),
            'EndSession': grpc.unary_unary_rpc_method_handler(
                    servicer.EndSession,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionRes.SerializeToString,
            ),
            'GetCurrentSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentSession,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetCurrentSessionReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AsmSession.SerializeToString,
            ),
            'SwitchSubsession': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchSubsession,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionRes.SerializeToString,
            ),
            'ListConversations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConversations,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsRes.SerializeToString,
            ),
            'AssignNewConversation': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignNewConversation,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationRes.SerializeToString,
            ),
            'ListAgents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAgents,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsRes.SerializeToString,
            ),
            'SetConversationCollectedData': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConversationCollectedData,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataReq.FromString,
                    response_serializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataRes.SerializeToString,
            ),
            'GetQueuesDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQueuesDetails,
                    request_deserializer=api_dot_v1alpha1_dot_asm_dot_service__pb2.GetQueuesDetailsReq.FromString,
                    response_serializer=api_dot_commons_dot_omnichannel__pb2.GetQueuesDetailsRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.asm.AsmApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AsmApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/CreateSession',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.CreateSessionRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/GetStatus',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.GetStatusRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/EndSession',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.EndSessionRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCurrentSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/GetCurrentSession',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.GetCurrentSessionReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.AsmSession.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SwitchSubsession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/SwitchSubsession',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.SwitchSubsessionRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListConversations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/ListConversations',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.ListConversationsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignNewConversation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/AssignNewConversation',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.AssignNewConversationRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAgents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/ListAgents',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.ListAgentsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConversationCollectedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/SetConversationCollectedData',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataReq.SerializeToString,
            api_dot_v1alpha1_dot_asm_dot_service__pb2.SetConversationCollectedDataRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetQueuesDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.asm.AsmApi/GetQueuesDetails',
            api_dot_v1alpha1_dot_asm_dot_service__pb2.GetQueuesDetailsReq.SerializeToString,
            api_dot_commons_dot_omnichannel__pb2.GetQueuesDetailsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
