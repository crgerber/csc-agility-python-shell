__author__ = 'dawood'
from itertools import chain

class WADLEvent(object):
    def __init__(self, name, params=None):
        self.name = name
        self.params = params if params is not None else list()

    def _key(self):
        return '|'.join(chain([self.name], self.params))

    def __hash__(self):
        return hash(self._key())

    def __eq__(self, other):
        return self._key() == other._key()

EVENTS = [
    'application',
    'application_doc',
    'application_grammers',
    'application_resources',
    'application_resources_resource_id',
    'application_resources_resource_path',
    'application_resources_resource_type',
    'application_resources_resource_queryType',
    'application_resources_resource_doc',
    'application_resources_resource_resource',#nested, how many levels allowed?
    'application_resources_resource_param',
    'application_resources_resource_param_id',
    'application_resources_resource_param_name',
    'application_resources_resource_param_href',
    'application_resources_resource_param_option',
    'application_resources_resource_param_option_value',
    'application_resources_resource_param_option_mediaType',
    'application_resources_resource_param_style',#template|matrix|query|header|plain depends on the parent element type. See Table 1: Values of style attribute and context for use below
    'application_resources_resource_param_type',
    'application_resources_resource_param_default',
    'application_resources_resource_param_path',
    'application_resources_resource_param_required',
    'application_resources_resource_param_repeating',
    'application_resources_resource_param_fixed',
    'application_resources_resource_method',
    'application_resources_resource_method_name',
    'application_resources_resource_method_id',
    'application_resources_resource_method_doc',
    'application_resources_resource_method_request',
    'application_resources_resource_method_request_doc',
    'application_resources_resource_method_request_representation',
    'application_resources_resource_method_request_param',#param style is query|header only
    'application_resources_resource_method_response',
    'application_resources_resource_method_response_status',
    'application_resources_resource_method_response_doc',
    'application_resources_resource_method_response_param',#param style is header only
    'application_resources_resource_method_response_representation',
    'application_resources_resource_method_response_representation_id',
    'application_resources_resource_method_response_representation_mediaType',
    'application_resources_resource_method_response_representation_element',
    'application_resources_resource_method_response_representation_profile',
    'application_resources_resource_method_response_representation_href',#representation href can cross reference a definition elsewehre




]

#
#                       Table 1: Values of style attribute and context for use.
#Value	    Parent Element(s) of param	Usage
#matrix	    resource                                        Specifies a matrix URI component.
#header	    resource, resource_type, request or response	Specifies a HTTP header that pertains to the HTTP request (resource or request) or HTTP response (response)
#query	    resource, resource_type or request	            Specifies a URI query parameter represented according to the rules for the query component media type specified by the queryType attribute.
#query	    representation	                                Specifies a component of the representation as a name value pair formatted according to the rules of the media type. Typically used with media type 'application/x-www-form-urlencoded' or 'multipart/form-data'.
#template	resource	                                    The parameter is represented as a string encoding of the parameter value and is substituted into the value of the path attribute of the resource element as described in section 2.6.1.
#plain	    representation	                                Specifies a component of the representation formatted as a string encoding of the parameter value according to the rules of the media type.
#

class WADLParser(object):
    def __init__(self):
        self._events = set()
        self._eventHandlers = dict()
        pass

    def load(self, filepath):
        pass

    def registerEventHandler(self, event, handler):
        if event not in self._events:
            raise RuntimeError('Unrecognized Event [%s]'%event)
        else:
            self._eventHandlers[event] = handler
            return dict(self._eventHandlers) #return a copy
