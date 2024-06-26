# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v1alpha1.scorecards import auto_evaluation_pb2 as api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2
from api.v1alpha1.scorecards import category_pb2 as api_dot_v1alpha1_dot_scorecards_dot_category__pb2
from api.v1alpha1.scorecards import evaluation_pb2 as api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2
from api.v1alpha1.scorecards import scorecard_pb2 as api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2


class ScorecardsSupportStub(object):
    """ScorecardsSupport provies customer support
    specific endpoints for Scorecards.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEvaluationsByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/ListEvaluationsByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsResponse.FromString,
                )
        self.ListAutoEvaluationsByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/ListAutoEvaluationsByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsResponse.FromString,
                )
        self.BulkDeleteEvaluations = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/BulkDeleteEvaluations',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsResponse.FromString,
                )
        self.BulkDeleteAutoEvaluations = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/BulkDeleteAutoEvaluations',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsResponse.FromString,
                )
        self.DeleteEvaluationByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/DeleteEvaluationByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationResponse.FromString,
                )
        self.DeleteAutoEvaluationByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/DeleteAutoEvaluationByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationResponse.FromString,
                )
        self.ListScorecardsByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/ListScorecardsByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsResponse.FromString,
                )
        self.ListCategoriesByOrgId = channel.unary_unary(
                '/api.v1alpha1.scorecards.ScorecardsSupport/ListCategoriesByOrgId',
                request_serializer=api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesByOrgIdRequest.SerializeToString,
                response_deserializer=api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesResponse.FromString,
                )


class ScorecardsSupportServicer(object):
    """ScorecardsSupport provies customer support
    specific endpoints for Scorecards.
    """

    def ListEvaluationsByOrgId(self, request, context):
        """ListEvaluationsByOrgId gets a list of evaluations by org id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAutoEvaluationsByOrgId(self, request, context):
        """ListAutoEvaluationsByOrgId gets a list of auto evaluations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkDeleteEvaluations(self, request, context):
        """BulkDeleteEvaluations deletes a set of evaluations in a given org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkDeleteAutoEvaluations(self, request, context):
        """BulkDeleteAutoEvaluations deletes a set of auto evaluations in a given org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEvaluationByOrgId(self, request, context):
        """DeleteEvaluationByOrgId delete an evaluation in a specific org
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAutoEvaluationByOrgId(self, request, context):
        """DeleteAutoEvaluationByOrgId deletes an auto evaluations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListScorecardsByOrgId(self, request, context):
        """ListScorecardsByOrgId lists scorecards
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCategoriesByOrgId(self, request, context):
        """ListCategoriesByOrgId lists categories
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScorecardsSupportServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListEvaluationsByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvaluationsByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsResponse.SerializeToString,
            ),
            'ListAutoEvaluationsByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAutoEvaluationsByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsResponse.SerializeToString,
            ),
            'BulkDeleteEvaluations': grpc.unary_unary_rpc_method_handler(
                    servicer.BulkDeleteEvaluations,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsResponse.SerializeToString,
            ),
            'BulkDeleteAutoEvaluations': grpc.unary_unary_rpc_method_handler(
                    servicer.BulkDeleteAutoEvaluations,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsResponse.SerializeToString,
            ),
            'DeleteEvaluationByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEvaluationByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationResponse.SerializeToString,
            ),
            'DeleteAutoEvaluationByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAutoEvaluationByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationResponse.SerializeToString,
            ),
            'ListScorecardsByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.ListScorecardsByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsResponse.SerializeToString,
            ),
            'ListCategoriesByOrgId': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCategoriesByOrgId,
                    request_deserializer=api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesByOrgIdRequest.FromString,
                    response_serializer=api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1alpha1.scorecards.ScorecardsSupport', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScorecardsSupport(object):
    """ScorecardsSupport provies customer support
    specific endpoints for Scorecards.
    """

    @staticmethod
    def ListEvaluationsByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/ListEvaluationsByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.ListEvaluationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAutoEvaluationsByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/ListAutoEvaluationsByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.ListAutoEvaluationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkDeleteEvaluations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/BulkDeleteEvaluations',
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.BulkDeleteEvaluationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkDeleteAutoEvaluations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/BulkDeleteAutoEvaluations',
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.BulkDeleteAutoEvaluationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEvaluationByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/DeleteEvaluationByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2.DeleteEvaluationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAutoEvaluationByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/DeleteAutoEvaluationByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2.DeleteAutoEvaluationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListScorecardsByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/ListScorecardsByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2.ListScorecardsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCategoriesByOrgId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1alpha1.scorecards.ScorecardsSupport/ListCategoriesByOrgId',
            api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesByOrgIdRequest.SerializeToString,
            api_dot_v1alpha1_dot_scorecards_dot_category__pb2.ListCategoriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
