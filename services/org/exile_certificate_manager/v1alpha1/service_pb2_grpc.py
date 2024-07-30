# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from services.org.exile_certificate_manager.v1alpha1 import exile_certificate_pb2 as services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2
from services.org.exile_certificate_manager.v1alpha1 import exile_configuration_pb2 as services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2


class ExileCertificateManagerServiceStub(object):
    """ExileCertificateManagerService is the service for managing organization's exile ceritificate.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateExileCertificate = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/CreateExileCertificate',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateResponse.FromString,
                )
        self.RevokeExileCertificate = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/RevokeExileCertificate',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateResponse.FromString,
                )
        self.AssignExileConfiguration = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/AssignExileConfiguration',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationResponse.FromString,
                )
        self.UnassignExileConfiguration = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/UnassignExileConfiguration',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationResponse.FromString,
                )
        self.ListExileCertificates = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/ListExileCertificates',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesResponse.FromString,
                )
        self.CreateExileConfiguration = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/CreateExileConfiguration',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationResponse.FromString,
                )
        self.UpdateExileConfiguration = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/UpdateExileConfiguration',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationResponse.FromString,
                )
        self.DeleteExileConfiguration = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/DeleteExileConfiguration',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationResponse.FromString,
                )
        self.ListExileConfigurations = channel.unary_unary(
                '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/ListExileConfigurations',
                request_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsRequest.SerializeToString,
                response_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsResponse.FromString,
                )


class ExileCertificateManagerServiceServicer(object):
    """ExileCertificateManagerService is the service for managing organization's exile ceritificate.
    """

    def CreateExileCertificate(self, request, context):
        """CreateExileCertificate creates a new TLS certificate and
        returns the exile ceritificate for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeExileCertificate(self, request, context):
        """RevokeExileCertificate deletes a exile ceritificate for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignExileConfiguration(self, request, context):
        """AssignExileConfiguration assigns a configuration to a certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnassignExileConfiguration(self, request, context):
        """UnassignExileConfiguration unassigns a configuration from a certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExileCertificates(self, request, context):
        """ListExileCertificates returns a list of exile ceritificate for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExileConfiguration(self, request, context):
        """CreateExileConfiguration creates a new exile configuration for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExileConfiguration(self, request, context):
        """UpdateExileConfiguration updates a exile configuration for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteExileConfiguration(self, request, context):
        """DeleteExileConfiguration deletes a exile configuration for the current organization.
        The configuration can only be deleted if it is not assigned to any certificates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExileConfigurations(self, request, context):
        """ListExileConfigurations returns a list of exile configurations for the current organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExileCertificateManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateExileCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExileCertificate,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateResponse.SerializeToString,
            ),
            'RevokeExileCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeExileCertificate,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateResponse.SerializeToString,
            ),
            'AssignExileConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignExileConfiguration,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationResponse.SerializeToString,
            ),
            'UnassignExileConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.UnassignExileConfiguration,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationResponse.SerializeToString,
            ),
            'ListExileCertificates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExileCertificates,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesResponse.SerializeToString,
            ),
            'CreateExileConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExileConfiguration,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationResponse.SerializeToString,
            ),
            'UpdateExileConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExileConfiguration,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationResponse.SerializeToString,
            ),
            'DeleteExileConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteExileConfiguration,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationResponse.SerializeToString,
            ),
            'ListExileConfigurations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExileConfigurations,
                    request_deserializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsRequest.FromString,
                    response_serializer=services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExileCertificateManagerService(object):
    """ExileCertificateManagerService is the service for managing organization's exile ceritificate.
    """

    @staticmethod
    def CreateExileCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/CreateExileCertificate',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.CreateExileCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeExileCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/RevokeExileCertificate',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.RevokeExileCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignExileConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/AssignExileConfiguration',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.AssignExileConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnassignExileConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/UnassignExileConfiguration',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.UnassignExileConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExileCertificates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/ListExileCertificates',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__certificate__pb2.ListExileCertificatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateExileConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/CreateExileConfiguration',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.CreateExileConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateExileConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/UpdateExileConfiguration',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.UpdateExileConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteExileConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/DeleteExileConfiguration',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.DeleteExileConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExileConfigurations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.org.exile_certificate_manager.v1alpha1.ExileCertificateManagerService/ListExileConfigurations',
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsRequest.SerializeToString,
            services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_exile__configuration__pb2.ListExileConfigurationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
