# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.workflows import entities_pb2 as api_dot_v1alpha1_dot_workflows_dot_entities__pb2


class WorkflowsDefinitionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFlowDefinitions = channel.unary_unary(
                '/api.v1alpha1.workflows.WorkflowsDefinitionService/ListFlowDefinitions',
                request_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsResponse.FromString,
                )
        self.SaveFlowDefinition = channel.unary_unary(
                '/api.v1alpha1.workflows.WorkflowsDefinitionService/SaveFlowDefinition',
                request_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionResponse.FromString,
                )
        self.GetFlowDefinition = channel.unary_unary(
                '/api.v1alpha1.workflows.WorkflowsDefinitionService/GetFlowDefinition',
                request_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionResponse.FromString,
                )
        self.DeleteFlowDefinition = channel.unary_unary(
                '/api.v1alpha1.workflows.WorkflowsDefinitionService/DeleteFlowDefinition',
                request_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionResponse.FromString,
                )


class WorkflowsDefinitionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFlowDefinitions(self, request, context):
        """ListFlowDefinitions lists flow definitions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveFlowDefinition(self, request, context):
        """SaveFlowDefinition creates or updates a flow definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFlowDefinition(self, request, context):
        """GetFlowDefinition gets a flow definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFlowDefinition(self, request, context):
        """DeleteFlowDefinition deletes a flow definition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkflowsDefinitionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFlowDefinitions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFlowDefinitions,
                    request_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsResponse.SerializeToString,
            ),
            'SaveFlowDefinition': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveFlowDefinition,
                    request_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionResponse.SerializeToString,
            ),
            'GetFlowDefinition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlowDefinition,
                    request_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionResponse.SerializeToString,
            ),
            'DeleteFlowDefinition': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFlowDefinition,
                    request_deserializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.workflows.WorkflowsDefinitionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkflowsDefinitionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFlowDefinitions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.workflows.WorkflowsDefinitionService/ListFlowDefinitions',
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsRequest.SerializeToString,
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.ListFlowDefinitionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveFlowDefinition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.workflows.WorkflowsDefinitionService/SaveFlowDefinition',
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionRequest.SerializeToString,
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.SaveFlowDefinitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFlowDefinition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.workflows.WorkflowsDefinitionService/GetFlowDefinition',
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionRequest.SerializeToString,
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.GetFlowDefinitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFlowDefinition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.workflows.WorkflowsDefinitionService/DeleteFlowDefinition',
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionRequest.SerializeToString,
            api_dot_v1alpha1_dot_workflows_dot_entities__pb2.DeleteFlowDefinitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
