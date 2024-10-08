# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tcnapi.omni.projects.v1 import entities_pb2 as tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2
from tcnapi.omni.projects.v1 import projects_pb2 as tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2


class ProjectsStub(object):
    """Projects service is the public api for the omni/projects service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListProjects = channel.unary_unary(
                '/tcnapi.omni.projects.v1.Projects/ListProjects',
                request_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/tcnapi.omni.projects.v1.Projects/GetProject',
                request_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/tcnapi.omni.projects.v1.Projects/CreateProject',
                request_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
                )
        self.UpdateProject = channel.unary_unary(
                '/tcnapi.omni.projects.v1.Projects/UpdateProject',
                request_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/tcnapi.omni.projects.v1.Projects/DeleteProject',
                request_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
                )


class ProjectsServicer(object):
    """Projects service is the public api for the omni/projects service.
    """

    def ListProjects(self, request, context):
        """Method to list projects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """Method to get a rpoject
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """Method to create a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """Method to update a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """Method to delete a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProjects,
                    request_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsRequest.FromString,
                    response_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.GetProjectRequest.FromString,
                    response_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.CreateProjectRequest.FromString,
                    response_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.UpdateProjectRequest.FromString,
                    response_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.DeleteProjectRequest.FromString,
                    response_serializer=tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tcnapi.omni.projects.v1.Projects', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Projects(object):
    """Projects service is the public api for the omni/projects service.
    """

    @staticmethod
    def ListProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tcnapi.omni.projects.v1.Projects/ListProjects',
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsRequest.SerializeToString,
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.ListProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tcnapi.omni.projects.v1.Projects/GetProject',
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.GetProjectRequest.SerializeToString,
            tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tcnapi.omni.projects.v1.Projects/CreateProject',
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.CreateProjectRequest.SerializeToString,
            tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tcnapi.omni.projects.v1.Projects/UpdateProject',
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.UpdateProjectRequest.SerializeToString,
            tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tcnapi.omni.projects.v1.Projects/DeleteProject',
            tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2.DeleteProjectRequest.SerializeToString,
            tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
