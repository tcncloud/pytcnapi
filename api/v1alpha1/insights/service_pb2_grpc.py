# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.insights import insight_pb2 as api_dot_v1alpha1_dot_insights_dot_insight__pb2


class InsightsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/CreateInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.FromString,
                )
        self.ListInsights = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/ListInsights',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsResponse.FromString,
                )
        self.ListOrgInsights = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/ListOrgInsights',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsResponse.FromString,
                )
        self.UpdateInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/UpdateInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.FromString,
                )
        self.DeleteInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/DeleteInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.FromString,
                )
        self.GetInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/GetInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightResponse.FromString,
                )
        self.CreateCommonsInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/CreateCommonsInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.FromString,
                )
        self.UpdateCommonsInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/UpdateCommonsInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.FromString,
                )
        self.DeleteCommonsInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/DeleteCommonsInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.FromString,
                )
        self.GetVfsSchema = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/GetVfsSchema',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaResponse.FromString,
                )
        self.ListVfses = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/ListVfses',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesResponse.FromString,
                )
        self.ListVfsSchemas = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/ListVfsSchemas',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasResponse.FromString,
                )
        self.PublishInsight = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/PublishInsight',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightResponse.FromString,
                )
        self.CreateOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/CreateOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationResponse.FromString,
                )
        self.ListOutputConfigurations = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/ListOutputConfigurations',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsResponse.FromString,
                )
        self.UpdateOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/UpdateOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationResponse.FromString,
                )
        self.DeleteOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/DeleteOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationResponse.FromString,
                )
        self.GetOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/GetOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationResponse.FromString,
                )
        self.SetDefaultOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/SetDefaultOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationResponse.FromString,
                )
        self.GetDefaultOutputConfiguration = channel.unary_unary(
                '/api.v1alpha1.insights.Insights/GetDefaultOutputConfiguration',
                request_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationResponse.FromString,
                )


class InsightsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateInsight(self, request, context):
        """CreateInsight creates a new insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInsights(self, request, context):
        """ListInsights lists insights
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrgInsights(self, request, context):
        """ListOrgInsights lists insights for an org. Used for support app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInsight(self, request, context):
        """UpdateInsight updates an existing insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInsight(self, request, context):
        """DeleteInsight deletes a insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInsight(self, request, context):
        """GetInsight gets a insight by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCommonsInsight(self, request, context):
        """CreateCommonsInsight is deprecated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCommonsInsight(self, request, context):
        """UpdateCommonsInsight is deprecated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCommonsInsight(self, request, context):
        """DeleteCommonsInsight is deprecated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVfsSchema(self, request, context):
        """GetVfsSchema gets schema for a vfs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVfses(self, request, context):
        """ListVfses lists exported vfs aliases
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVfsSchemas(self, request, context):
        """ListVfses lists exported vfs aliases
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishInsight(self, request, context):
        """PublishInsight publishes an insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOutputConfiguration(self, request, context):
        """CreateOutputConfiguration creates an output configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOutputConfigurations(self, request, context):
        """ListOutputConfigurations lists output configurations for an insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOutputConfiguration(self, request, context):
        """UpdateOutputConfiguration updates an output configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOutputConfiguration(self, request, context):
        """DeleteOutputConfiguration deletes an output configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOutputConfiguration(self, request, context):
        """GetOutputConfiguration gets an output configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDefaultOutputConfiguration(self, request, context):
        """SetDefaultOutputConfiguration sets the specified output configuration to default
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDefaultOutputConfiguration(self, request, context):
        """GetDefaultOutputConfiguration gets the default output configuration for an insight
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InsightsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.SerializeToString,
            ),
            'ListInsights': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInsights,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsResponse.SerializeToString,
            ),
            'ListOrgInsights': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrgInsights,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsResponse.SerializeToString,
            ),
            'UpdateInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.SerializeToString,
            ),
            'DeleteInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.SerializeToString,
            ),
            'GetInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightResponse.SerializeToString,
            ),
            'CreateCommonsInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCommonsInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.SerializeToString,
            ),
            'UpdateCommonsInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCommonsInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.SerializeToString,
            ),
            'DeleteCommonsInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCommonsInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.SerializeToString,
            ),
            'GetVfsSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVfsSchema,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaResponse.SerializeToString,
            ),
            'ListVfses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVfses,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesResponse.SerializeToString,
            ),
            'ListVfsSchemas': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVfsSchemas,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasResponse.SerializeToString,
            ),
            'PublishInsight': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishInsight,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightResponse.SerializeToString,
            ),
            'CreateOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationResponse.SerializeToString,
            ),
            'ListOutputConfigurations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOutputConfigurations,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsResponse.SerializeToString,
            ),
            'UpdateOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationResponse.SerializeToString,
            ),
            'DeleteOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationResponse.SerializeToString,
            ),
            'GetOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationResponse.SerializeToString,
            ),
            'SetDefaultOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDefaultOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationResponse.SerializeToString,
            ),
            'GetDefaultOutputConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDefaultOutputConfiguration,
                    request_deserializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.insights.Insights', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Insights(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/CreateInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListInsights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/ListInsights',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListInsightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrgInsights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/ListOrgInsights',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOrgInsightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/UpdateInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/DeleteInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/GetInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCommonsInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/CreateCommonsInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCommonsInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/UpdateCommonsInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCommonsInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/DeleteCommonsInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVfsSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/GetVfsSchema',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetVfsSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListVfses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/ListVfses',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListVfsSchemas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/ListVfsSchemas',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListVfsSchemasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishInsight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/PublishInsight',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.PublishInsightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/CreateOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.CreateOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOutputConfigurations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/ListOutputConfigurations',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.ListOutputConfigurationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/UpdateOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.UpdateOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/DeleteOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.DeleteOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/GetOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDefaultOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/SetDefaultOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.SetDefaultOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDefaultOutputConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.insights.Insights/GetDefaultOutputConfiguration',
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationRequest.SerializeToString,
            api_dot_v1alpha1_dot_insights_dot_insight__pb2.GetDefaultOutputConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
