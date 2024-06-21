# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.translations.v1alpha1 import entities_pb2 as services_dot_translations_dot_v1alpha1_dot_entities__pb2


class TranslationsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TranslateTemplate = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/TranslateTemplate',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateResponse.FromString,
                )


class TranslationsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TranslateTemplate(self, request, context):
        """
        Required permissions:
        Any Authenticated User (TODO: Validate this assumption)
        Errors:
        - grpc.PermissionDenied: Caller doesn't have the required permissions.
        - grpc.AlreadyExists : This template is already translated for the given context and language.
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranslationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TranslateTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.TranslateTemplate,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.translations.v1alpha1.TranslationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TranslationsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TranslateTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/TranslateTemplate',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TranslateTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
