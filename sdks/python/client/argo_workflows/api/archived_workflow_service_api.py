"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.api_client import ApiClient, Endpoint as _Endpoint
from argo_workflows.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_label_keys import IoArgoprojWorkflowV1alpha1LabelKeys
from argo_workflows.model.io_argoproj_workflow_v1alpha1_label_values import IoArgoprojWorkflowV1alpha1LabelValues
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_list import IoArgoprojWorkflowV1alpha1WorkflowList


class ArchivedWorkflowServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_archived_workflow(
            self,
            uid,
            **kwargs
        ):
            """delete_archived_workflow  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_archived_workflow(uid, async_req=True)
            >>> result = thread.get()

            Args:
                uid (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['uid'] = \
                uid
            return self.call_with_http_info(**kwargs)

        self.delete_archived_workflow = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/api/v1/archived-workflows/{uid}',
                'operation_id': 'delete_archived_workflow',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'uid',
                ],
                'required': [
                    'uid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uid':
                        (str,),
                },
                'attribute_map': {
                    'uid': 'uid',
                },
                'location_map': {
                    'uid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_archived_workflow
        )

        def __get_archived_workflow(
            self,
            uid,
            **kwargs
        ):
            """get_archived_workflow  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_archived_workflow(uid, async_req=True)
            >>> result = thread.get()

            Args:
                uid (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1Workflow
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['uid'] = \
                uid
            return self.call_with_http_info(**kwargs)

        self.get_archived_workflow = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1Workflow,),
                'auth': [],
                'endpoint_path': '/api/v1/archived-workflows/{uid}',
                'operation_id': 'get_archived_workflow',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uid',
                ],
                'required': [
                    'uid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uid':
                        (str,),
                },
                'attribute_map': {
                    'uid': 'uid',
                },
                'location_map': {
                    'uid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_archived_workflow
        )

        def __list_archived_workflow_label_keys(
            self,
            **kwargs
        ):
            """list_archived_workflow_label_keys  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_archived_workflow_label_keys(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1LabelKeys
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_archived_workflow_label_keys = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1LabelKeys,),
                'auth': [],
                'endpoint_path': '/api/v1/archived-workflows-label-keys',
                'operation_id': 'list_archived_workflow_label_keys',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_archived_workflow_label_keys
        )

        def __list_archived_workflow_label_values(
            self,
            **kwargs
        ):
            """list_archived_workflow_label_values  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_archived_workflow_label_values(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                list_options_label_selector (str): A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional.. [optional]
                list_options_field_selector (str): A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional.. [optional]
                list_options_watch (bool): Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional.. [optional]
                list_options_allow_watch_bookmarks (bool): allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. +optional.. [optional]
                list_options_resource_version (str): resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_resource_version_match (str): resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_timeout_seconds (str): Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional.. [optional]
                list_options_limit (str): limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.. [optional]
                list_options_continue (str): The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1LabelValues
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_archived_workflow_label_values = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1LabelValues,),
                'auth': [],
                'endpoint_path': '/api/v1/archived-workflows-label-values',
                'operation_id': 'list_archived_workflow_label_values',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'list_options_label_selector',
                    'list_options_field_selector',
                    'list_options_watch',
                    'list_options_allow_watch_bookmarks',
                    'list_options_resource_version',
                    'list_options_resource_version_match',
                    'list_options_timeout_seconds',
                    'list_options_limit',
                    'list_options_continue',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'list_options_label_selector':
                        (str,),
                    'list_options_field_selector':
                        (str,),
                    'list_options_watch':
                        (bool,),
                    'list_options_allow_watch_bookmarks':
                        (bool,),
                    'list_options_resource_version':
                        (str,),
                    'list_options_resource_version_match':
                        (str,),
                    'list_options_timeout_seconds':
                        (str,),
                    'list_options_limit':
                        (str,),
                    'list_options_continue':
                        (str,),
                },
                'attribute_map': {
                    'list_options_label_selector': 'listOptions.labelSelector',
                    'list_options_field_selector': 'listOptions.fieldSelector',
                    'list_options_watch': 'listOptions.watch',
                    'list_options_allow_watch_bookmarks': 'listOptions.allowWatchBookmarks',
                    'list_options_resource_version': 'listOptions.resourceVersion',
                    'list_options_resource_version_match': 'listOptions.resourceVersionMatch',
                    'list_options_timeout_seconds': 'listOptions.timeoutSeconds',
                    'list_options_limit': 'listOptions.limit',
                    'list_options_continue': 'listOptions.continue',
                },
                'location_map': {
                    'list_options_label_selector': 'query',
                    'list_options_field_selector': 'query',
                    'list_options_watch': 'query',
                    'list_options_allow_watch_bookmarks': 'query',
                    'list_options_resource_version': 'query',
                    'list_options_resource_version_match': 'query',
                    'list_options_timeout_seconds': 'query',
                    'list_options_limit': 'query',
                    'list_options_continue': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_archived_workflow_label_values
        )

        def __list_archived_workflows(
            self,
            **kwargs
        ):
            """list_archived_workflows  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_archived_workflows(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                list_options_label_selector (str): A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional.. [optional]
                list_options_field_selector (str): A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional.. [optional]
                list_options_watch (bool): Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional.. [optional]
                list_options_allow_watch_bookmarks (bool): allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. +optional.. [optional]
                list_options_resource_version (str): resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_resource_version_match (str): resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
                list_options_timeout_seconds (str): Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional.. [optional]
                list_options_limit (str): limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.. [optional]
                list_options_continue (str): The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.. [optional]
                name_prefix (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                IoArgoprojWorkflowV1alpha1WorkflowList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_archived_workflows = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1WorkflowList,),
                'auth': [],
                'endpoint_path': '/api/v1/archived-workflows',
                'operation_id': 'list_archived_workflows',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'list_options_label_selector',
                    'list_options_field_selector',
                    'list_options_watch',
                    'list_options_allow_watch_bookmarks',
                    'list_options_resource_version',
                    'list_options_resource_version_match',
                    'list_options_timeout_seconds',
                    'list_options_limit',
                    'list_options_continue',
                    'name_prefix',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'list_options_label_selector':
                        (str,),
                    'list_options_field_selector':
                        (str,),
                    'list_options_watch':
                        (bool,),
                    'list_options_allow_watch_bookmarks':
                        (bool,),
                    'list_options_resource_version':
                        (str,),
                    'list_options_resource_version_match':
                        (str,),
                    'list_options_timeout_seconds':
                        (str,),
                    'list_options_limit':
                        (str,),
                    'list_options_continue':
                        (str,),
                    'name_prefix':
                        (str,),
                },
                'attribute_map': {
                    'list_options_label_selector': 'listOptions.labelSelector',
                    'list_options_field_selector': 'listOptions.fieldSelector',
                    'list_options_watch': 'listOptions.watch',
                    'list_options_allow_watch_bookmarks': 'listOptions.allowWatchBookmarks',
                    'list_options_resource_version': 'listOptions.resourceVersion',
                    'list_options_resource_version_match': 'listOptions.resourceVersionMatch',
                    'list_options_timeout_seconds': 'listOptions.timeoutSeconds',
                    'list_options_limit': 'listOptions.limit',
                    'list_options_continue': 'listOptions.continue',
                    'name_prefix': 'namePrefix',
                },
                'location_map': {
                    'list_options_label_selector': 'query',
                    'list_options_field_selector': 'query',
                    'list_options_watch': 'query',
                    'list_options_allow_watch_bookmarks': 'query',
                    'list_options_resource_version': 'query',
                    'list_options_resource_version_match': 'query',
                    'list_options_timeout_seconds': 'query',
                    'list_options_limit': 'query',
                    'list_options_continue': 'query',
                    'name_prefix': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_archived_workflows
        )
