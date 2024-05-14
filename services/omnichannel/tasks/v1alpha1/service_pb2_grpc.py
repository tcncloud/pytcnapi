# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.omnichannel.tasks.v1alpha1 import entities_pb2 as services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2


class TasksServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CancelTasks = channel.unary_unary(
                '/services.omnichannel.tasks.v1alpha1.TasksService/CancelTasks',
                request_serializer=services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksRequest.SerializeToString,
                response_deserializer=services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksResponse.FromString,
                )


class TasksServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CancelTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TasksServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CancelTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelTasks,
                    request_deserializer=services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksRequest.FromString,
                    response_serializer=services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.omnichannel.tasks.v1alpha1.TasksService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TasksService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CancelTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.omnichannel.tasks.v1alpha1.TasksService/CancelTasks',
            services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksRequest.SerializeToString,
            services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2.CancelTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)