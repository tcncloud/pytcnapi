# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.classifier import service_pb2 as api_dot_v1alpha1_dot_classifier_dot_service__pb2


class ClassifierFileTemplatesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ParseFile = channel.unary_unary(
                '/api.v1alpha1.classifier.ClassifierFileTemplates/ParseFile',
                request_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileResponse.FromString,
                )
        self.UpdateFileTemplate = channel.unary_unary(
                '/api.v1alpha1.classifier.ClassifierFileTemplates/UpdateFileTemplate',
                request_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateResponse.FromString,
                )
        self.DeleteFileTemplate = channel.unary_unary(
                '/api.v1alpha1.classifier.ClassifierFileTemplates/DeleteFileTemplate',
                request_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateResponse.FromString,
                )
        self.ListFileTemplates = channel.unary_unary(
                '/api.v1alpha1.classifier.ClassifierFileTemplates/ListFileTemplates',
                request_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesResponse.FromString,
                )
        self.GetFileTemplate = channel.unary_unary(
                '/api.v1alpha1.classifier.ClassifierFileTemplates/GetFileTemplate',
                request_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateResponse.FromString,
                )


class ClassifierFileTemplatesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ParseFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFileTemplate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFileTemplate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFileTemplates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileTemplate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClassifierFileTemplatesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ParseFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ParseFile,
                    request_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileResponse.SerializeToString,
            ),
            'UpdateFileTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFileTemplate,
                    request_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateResponse.SerializeToString,
            ),
            'DeleteFileTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFileTemplate,
                    request_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateResponse.SerializeToString,
            ),
            'ListFileTemplates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFileTemplates,
                    request_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesResponse.SerializeToString,
            ),
            'GetFileTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFileTemplate,
                    request_deserializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.classifier.ClassifierFileTemplates', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClassifierFileTemplates(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ParseFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.classifier.ClassifierFileTemplates/ParseFile',
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileRequest.SerializeToString,
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.ParseFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFileTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.classifier.ClassifierFileTemplates/UpdateFileTemplate',
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateRequest.SerializeToString,
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.UpdateFileTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFileTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.classifier.ClassifierFileTemplates/DeleteFileTemplate',
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateRequest.SerializeToString,
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.DeleteFileTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFileTemplates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.classifier.ClassifierFileTemplates/ListFileTemplates',
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesRequest.SerializeToString,
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.ListFileTemplatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFileTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.classifier.ClassifierFileTemplates/GetFileTemplate',
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateRequest.SerializeToString,
            api_dot_v1alpha1_dot_classifier_dot_service__pb2.GetFileTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)