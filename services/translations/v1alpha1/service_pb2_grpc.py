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
        self.ListTranslations = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/ListTranslations',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsResponse.FromString,
                )
        self.ListLanguages = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/ListLanguages',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesResponse.FromString,
                )
        self.ListContexts = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/ListContexts',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsResponse.FromString,
                )
        self.UpdateTranslation = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/UpdateTranslation',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationResponse.FromString,
                )
        self.TriggerLLMTranslation = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/TriggerLLMTranslation',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationResponse.FromString,
                )
        self.TriggerLLMTranslations = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/TriggerLLMTranslations',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsResponse.FromString,
                )
        self.SetSystemMessage = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/SetSystemMessage',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageResponse.FromString,
                )
        self.GetSystemMessage = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/GetSystemMessage',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageResponse.FromString,
                )
        self.TestSystemMessage = channel.unary_unary(
                '/services.translations.v1alpha1.TranslationsService/TestSystemMessage',
                request_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageRequest.SerializeToString,
                response_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageResponse.FromString,
                )


class TranslationsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TranslateTemplate(self, request, context):
        """Translate a template for a given context and language.
        Required permissions:
        Any Authenticated User
        Errors:
        - grpc.AlreadyExists : This template is already translated for the given context and language.
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTranslations(self, request, context):
        """Management support calls

        Lists translations by context/language
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
        - grpc.InvalidArgument: The request is not valid.
        - grpc.NotFound: No templates found for the given context and language.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLanguages(self, request, context):
        """Lists localization languages
        Required permissions:
        - Any Authenticated User
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListContexts(self, request, context):
        """Lists localization contexts
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTranslation(self, request, context):
        """Overrides the translation for a given translationID
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerLLMTranslation(self, request, context):
        """Re-run the LLM translation for a given translationID
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerLLMTranslations(self, request, context):
        """re-run all translations for a given context (WARNING - this should be ran sparingly as it is a heavy operation and costs money)
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSystemMessage(self, request, context):
        """set/get context system message to give more tuned LLMs when translating for that context (WARNING - this overrides the previous system message for the context if exists)
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
        - grpc.InvalidArgument: The request is not valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSystemMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestSystemMessage(self, request, context):
        """Gives a translation for a system message, template and language with no side effects (Used for testing system messages)
        Required permissions:
        - PERMISSION_CUSTOMER_SUPPORT
        Errors:
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
            'ListTranslations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTranslations,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsResponse.SerializeToString,
            ),
            'ListLanguages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLanguages,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesResponse.SerializeToString,
            ),
            'ListContexts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListContexts,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsResponse.SerializeToString,
            ),
            'UpdateTranslation': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTranslation,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationResponse.SerializeToString,
            ),
            'TriggerLLMTranslation': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerLLMTranslation,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationResponse.SerializeToString,
            ),
            'TriggerLLMTranslations': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerLLMTranslations,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsResponse.SerializeToString,
            ),
            'SetSystemMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSystemMessage,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageResponse.SerializeToString,
            ),
            'GetSystemMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSystemMessage,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageResponse.SerializeToString,
            ),
            'TestSystemMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.TestSystemMessage,
                    request_deserializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageRequest.FromString,
                    response_serializer=services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageResponse.SerializeToString,
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

    @staticmethod
    def ListTranslations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/ListTranslations',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListTranslationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLanguages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/ListLanguages',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListLanguagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListContexts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/ListContexts',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.ListContextsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTranslation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/UpdateTranslation',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.UpdateTranslationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TriggerLLMTranslation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/TriggerLLMTranslation',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TriggerLLMTranslations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/TriggerLLMTranslations',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TriggerLLMTranslationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSystemMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/SetSystemMessage',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.SetSystemMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSystemMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/GetSystemMessage',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.GetSystemMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestSystemMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.translations.v1alpha1.TranslationsService/TestSystemMessage',
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageRequest.SerializeToString,
            services_dot_translations_dot_v1alpha1_dot_entities__pb2.TestSystemMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)