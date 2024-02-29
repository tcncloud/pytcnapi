# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api.v0alpha import learn_pb2 as api_dot_v0alpha_dot_learn__pb2


class LearnStub(object):
    """A service for creating and reading learning material
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Exist = channel.unary_unary(
                '/api.v0alpha.Learn/Exist',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ExistReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ExistRes.FromString,
                )
        self.Content = channel.unary_unary(
                '/api.v0alpha.Learn/Content',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ContentReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentRes.FromString,
                )
        self.ExportMany = channel.unary_unary(
                '/api.v0alpha.Learn/ExportMany',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ExportManyReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ExportRes.FromString,
                )
        self.SearchContent = channel.unary_unary(
                '/api.v0alpha.Learn/SearchContent',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.SearchContentReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
                )
        self.ListSearchResults = channel.unary_stream(
                '/api.v0alpha.Learn/ListSearchResults',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.SearchContentReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
                )
        self.Standalone = channel.unary_unary(
                '/api.v0alpha.Learn/Standalone',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.StandaloneReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.StandaloneRes.FromString,
                )
        self.ContentEditorData = channel.unary_unary(
                '/api.v0alpha.Learn/ContentEditorData',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ContentEditorDataReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentEditorDataRes.FromString,
                )
        self.Update = channel.unary_unary(
                '/api.v0alpha.Learn/Update',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.UpdateReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.UpdateRes.FromString,
                )
        self.StoreStaticImage = channel.unary_unary(
                '/api.v0alpha.Learn/StoreStaticImage',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.StoreStaticImageReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.StoreStaticImageRes.FromString,
                )
        self.UploadDynamicScreenshot = channel.unary_unary(
                '/api.v0alpha.Learn/UploadDynamicScreenshot',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotRes.FromString,
                )
        self.DeleteStandalone = channel.unary_unary(
                '/api.v0alpha.Learn/DeleteStandalone',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneRes.FromString,
                )
        self.Snippet = channel.unary_unary(
                '/api.v0alpha.Learn/Snippet',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.SnippetReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.SnippetRes.FromString,
                )
        self.DeleteLearnPages = channel.unary_unary(
                '/api.v0alpha.Learn/DeleteLearnPages',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesRes.FromString,
                )
        self.CreateEditVersion = channel.unary_unary(
                '/api.v0alpha.Learn/CreateEditVersion',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.CreateEditVersionReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.CreateEditVersionRes.FromString,
                )
        self.PublishVersion = channel.unary_unary(
                '/api.v0alpha.Learn/PublishVersion',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.PublishVersionReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.PublishVersionRes.FromString,
                )
        self.ContentByVersion = channel.unary_unary(
                '/api.v0alpha.Learn/ContentByVersion',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ContentByVersionReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentRes.FromString,
                )
        self.UpdateByVersion = channel.unary_unary(
                '/api.v0alpha.Learn/UpdateByVersion',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.UpdateByVersionReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.UpdateRes.FromString,
                )
        self.ListSearchResultsByVersion = channel.unary_stream(
                '/api.v0alpha.Learn/ListSearchResultsByVersion',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.SearchContentByVersionReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
                )
        self.ReviewFileVersions = channel.unary_unary(
                '/api.v0alpha.Learn/ReviewFileVersions',
                request_serializer=api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsReq.SerializeToString,
                response_deserializer=api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsRes.FromString,
                )


class LearnServicer(object):
    """A service for creating and reading learning material
    """

    def Exist(self, request, context):
        """check if learning page already exists
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Content(self, request, context):
        """retreive content from learning pages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportMany(self, request, context):
        """exports multiple pages of the learning center markdown as PDF
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchContent(self, request, context):
        """search content in learning pages
        we allow all the logged in agents/admins to view search content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSearchResults(self, request, context):
        """stream search content results in learning pages
        we allow all the logged in agents/admins to view search content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Standalone(self, request, context):
        """get standalone articles from learning pages
        we allow all the logged in agents/admins to view standalone articles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContentEditorData(self, request, context):
        """retrieve user who edited the content last
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """update contents for learning pages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreStaticImage(self, request, context):
        """upload url for static images
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadDynamicScreenshot(self, request, context):
        """upload dynamic learning image screenshot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStandalone(self, request, context):
        """delete standalone articles from learning pages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Snippet(self, request, context):
        """get snippet content from learning pages
        we allow all the logged in agents/admins to view snippet content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteLearnPages(self, request, context):
        """delete learning pages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEditVersion(self, request, context):
        """create edit version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishVersion(self, request, context):
        """publish version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContentByVersion(self, request, context):
        """retrieve content from learning pages based on version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateByVersion(self, request, context):
        """update contents for learning pages by version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSearchResultsByVersion(self, request, context):
        """stream search content results in learning pages by version
        we allow all the logged in agents/admins to view search content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReviewFileVersions(self, request, context):
        """return diff by comparing file contens from any version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LearnServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Exist': grpc.unary_unary_rpc_method_handler(
                    servicer.Exist,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ExistReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ExistRes.SerializeToString,
            ),
            'Content': grpc.unary_unary_rpc_method_handler(
                    servicer.Content,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ContentRes.SerializeToString,
            ),
            'ExportMany': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportMany,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ExportManyReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ExportRes.SerializeToString,
            ),
            'SearchContent': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchContent,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchContentReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.SerializeToString,
            ),
            'ListSearchResults': grpc.unary_stream_rpc_method_handler(
                    servicer.ListSearchResults,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchContentReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.SerializeToString,
            ),
            'Standalone': grpc.unary_unary_rpc_method_handler(
                    servicer.Standalone,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.StandaloneReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.StandaloneRes.SerializeToString,
            ),
            'ContentEditorData': grpc.unary_unary_rpc_method_handler(
                    servicer.ContentEditorData,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentEditorDataReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ContentEditorDataRes.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.UpdateReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.UpdateRes.SerializeToString,
            ),
            'StoreStaticImage': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreStaticImage,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.StoreStaticImageReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.StoreStaticImageRes.SerializeToString,
            ),
            'UploadDynamicScreenshot': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadDynamicScreenshot,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotRes.SerializeToString,
            ),
            'DeleteStandalone': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStandalone,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneRes.SerializeToString,
            ),
            'Snippet': grpc.unary_unary_rpc_method_handler(
                    servicer.Snippet,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.SnippetReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.SnippetRes.SerializeToString,
            ),
            'DeleteLearnPages': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteLearnPages,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesRes.SerializeToString,
            ),
            'CreateEditVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEditVersion,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.CreateEditVersionReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.CreateEditVersionRes.SerializeToString,
            ),
            'PublishVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishVersion,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.PublishVersionReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.PublishVersionRes.SerializeToString,
            ),
            'ContentByVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ContentByVersion,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ContentByVersionReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ContentRes.SerializeToString,
            ),
            'UpdateByVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateByVersion,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.UpdateByVersionReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.UpdateRes.SerializeToString,
            ),
            'ListSearchResultsByVersion': grpc.unary_stream_rpc_method_handler(
                    servicer.ListSearchResultsByVersion,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.SearchContentByVersionReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.SearchRes.SerializeToString,
            ),
            'ReviewFileVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.ReviewFileVersions,
                    request_deserializer=api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsReq.FromString,
                    response_serializer=api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v0alpha.Learn', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Learn(object):
    """A service for creating and reading learning material
    """

    @staticmethod
    def Exist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/Exist',
            api_dot_v0alpha_dot_learn__pb2.ExistReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ExistRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Content(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/Content',
            api_dot_v0alpha_dot_learn__pb2.ContentReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ContentRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/ExportMany',
            api_dot_v0alpha_dot_learn__pb2.ExportManyReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ExportRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/SearchContent',
            api_dot_v0alpha_dot_learn__pb2.SearchContentReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSearchResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.v0alpha.Learn/ListSearchResults',
            api_dot_v0alpha_dot_learn__pb2.SearchContentReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Standalone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/Standalone',
            api_dot_v0alpha_dot_learn__pb2.StandaloneReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.StandaloneRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContentEditorData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/ContentEditorData',
            api_dot_v0alpha_dot_learn__pb2.ContentEditorDataReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ContentEditorDataRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/Update',
            api_dot_v0alpha_dot_learn__pb2.UpdateReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.UpdateRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StoreStaticImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/StoreStaticImage',
            api_dot_v0alpha_dot_learn__pb2.StoreStaticImageReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.StoreStaticImageRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadDynamicScreenshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/UploadDynamicScreenshot',
            api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.UploadDynamicScreenshotRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStandalone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/DeleteStandalone',
            api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.DeleteStandaloneRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Snippet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/Snippet',
            api_dot_v0alpha_dot_learn__pb2.SnippetReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.SnippetRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteLearnPages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/DeleteLearnPages',
            api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.DeleteLearnPagesRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEditVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/CreateEditVersion',
            api_dot_v0alpha_dot_learn__pb2.CreateEditVersionReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.CreateEditVersionRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/PublishVersion',
            api_dot_v0alpha_dot_learn__pb2.PublishVersionReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.PublishVersionRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContentByVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/ContentByVersion',
            api_dot_v0alpha_dot_learn__pb2.ContentByVersionReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ContentRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateByVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/UpdateByVersion',
            api_dot_v0alpha_dot_learn__pb2.UpdateByVersionReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.UpdateRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSearchResultsByVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.v0alpha.Learn/ListSearchResultsByVersion',
            api_dot_v0alpha_dot_learn__pb2.SearchContentByVersionReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.SearchRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReviewFileVersions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v0alpha.Learn/ReviewFileVersions',
            api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsReq.SerializeToString,
            api_dot_v0alpha_dot_learn__pb2.ReviewFileVersionsRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
