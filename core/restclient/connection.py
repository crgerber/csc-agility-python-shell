'''
Created on Oct 8, 2012

@author: dawood
'''
import urllib.request, urllib.error, urllib.parse
import base64
import os
import http.cookiejar
import ssl

from functools import update_wrapper
from base64 import b64encode

from core.http.put.multipartform import MultiPartForm
from logger import logger


CONTENT_TYPE_APLICATION_XML = 'application/xml'
CONTENT_TYPE_MULTIPART_MIXED = 'multipart/mixed'

class RESTException(RuntimeError):
    def __init__(self, response):
        self.info = {}
        self.info['code'] = response.code
        self.info['message'] = '%s '%response.msg if response.msg else ''
        self.info['url'] = response.geturl()
        self.info['headers'] = str(response.headers).replace('\n', ';')
        self.info['body'] = response.read()

    def __repr__(self):
        template = '''ERROR: %(code)s %(message)sWhile invoking %(url)s. Response headers: %(headers)s Response body: %(body)s
'''
        return template%self.info
    
    __str__ = __repr__

class reauthenticate(object):
    '''
    Decorator class, designed to be used with connection instance methods that require re-authentication (e.g. getting a new Token after expiry)
    '''
    retry = False #set externally, possibly through a configuration flag to control behavior
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        self.f = f
        update_wrapper(self, f)
        
    def __get__(self, connection, cls=None):
        """
        Caching the instance reference when decorating methods, allows access to instance attributes
        """
        self._connection = connection
        return self
    
    def __call__(self, *args, **kwargs):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        try:
            response = self.f(self._connection, *args, **kwargs)
        except RESTException as restEx:
            if self.retry and 401 == restEx.info.get('code'):
                logger.info('Authentication Error, invalid or expired token, retrying to re authenticate ...')
                self._connection._connected = False
                self._connection.connect() #use same connection params
                #retry the method once more, if it fails, bail
                response = self.f(self._connection, *args, **kwargs)
            else:
                raise
        return response
    
class RESTConnection(object):
    def __init__(self, auth='basic', **kwargs):
        self.http_exception_hooks = dict()
        self._connected = False
        self.conn_params = {
                        'username' : 'admin',
                        'password' : '',
                        'host' : '',
                        'port' : '8443',
                        'version' : 'current', #API Version
                        'systemversion' : 'latest',
                        'ssl_context_unverified' : True,
                        'ssl_cacert_location' : 'cacert.pem' 
                        }
        self._auth = auth
        self.conn_params.update(kwargs)
        
        missing_conn_params = [k for k, v in list(self.conn_params.items()) if (v is None) or (v == '')]
        if missing_conn_params:
            raise RuntimeError('missing connection params %s'%missing_conn_params)
          
        check_hostname = None
        https_context = None
        
        if self.conn_params['ssl_context_unverified'] == 'True' :
            https_context = ssl._create_unverified_context()
            #https_context.verify_mode = ssl.CERT_NONE
            check_hostname = False
        else :
            https_context = ssl._create_default_https_context()
            #https_context.verify_mode = ssl.CERT_REQUIRED
            https_context.load_verify_locations(self.conn_params['ssl_cacert_location'])
            check_hostname = True
            
        handlers = [urllib.request.HTTPHandler(), urllib.request.HTTPSHandler(context = https_context, check_hostname = check_hostname)]

        if self._auth == 'basic':
            self._opener = urllib.request.build_opener(*handlers)
        elif self._auth == 'oauth':
            self._parse_token = True
            self._cookies = http.cookiejar.LWPCookieJar()
            handlers.append(urllib.request.HTTPCookieProcessor(self._cookies))
            self._opener = urllib.request.build_opener(*handlers)
            
    def connect(self, host=None, port=None, username=None, password=None):
        '''
        Connect (or re-connect) to Agility using the configured auth mode
        '''
        if host: self.conn_params['host'] = host
        if port: self.conn_params['port'] = str(port)
        if username: self.conn_params['username'] = username
        if password: self.conn_params['password'] = password
        
        token = None
        if self._auth == 'basic':
            credentials = '%s:%s' % (username, password)
            self._auth_string = b64encode(credentials.encode(encoding='utf-8')).decode("utf-8") 
        elif self._auth == 'oauth':
            token = self._oauth(self.conn_params)
        
        #only cache username and password if we are using Tokens and re-authenticate configuration flag is set, else clear them
        if self._auth == 'oauth' and self.conn_params.get('reauthenticate', False):
            reauthenticate.retry = True#attribute of the decorator class
        else:    
            del self.conn_params['username']
            del self.conn_params['password']
            
        self._connected = True
        return token
            
    def _oauth(self, conn_params):
        oauth_url = "https://%(host)s:%(port)s/agility/j_spring_security_check?product=AgilityManager&j_username=%(username)s&j_password=%(password)s"
        url = oauth_url%conn_params
        
        request = urllib.request.Request(url)
        response = self._opener.open(request)
        if self.conn_params.get('use_cookies'):
            return#Cookies would be handled automatically by the cookielib handler. just a place holder for further actions
        
        token_string = response.headers.get('set-cookie', None)
        if not token_string:
            exc = RuntimeError('Error: failed to retrieve authentication token. Response code: [%s], response headers: %s'%(response.code, dict(list(response.headers.items()))))
            if 401 in self.http_exception_hooks:
                logger.error(exc)
                exception_class, message = self.http_exception_hooks[401]
                raise exception_class('Failed to retrieve authentication token.')
            else:
                raise exc
        
        if self._parse_token:
            tuplize = lambda split_result: (split_result[0].strip(), split_result[1].strip() if len(split_result) == 2 else '')
            token = dict([tuplize(pair.split('=', 1)) for pair in token_string.split(';')])
        else:
            token = token_string
            
        self.conn_params['token'] = token
        self._cookies.clear()#making sure cookies are not sent unintentionally
        return token
        
    def get_token(self):
        assert (self._auth == 'oauth' and not self.conn_params.get('use_cookies')), 'Token is not available in the current auth mode'
        if self._parse_token:
            return '%s=%s'%('JSESSIONID', self.conn_params['token']['JSESSIONID'])
        else:
            return self.conn_params['token']
        
    def set_token(self, auth_token):
        assert self._auth == 'oauth'
        token = {'JSESSIONID': auth_token, 'Path': '/agility', 'Secure': ''}
        if self.conn_params.get('token') is None:
            self.conn_params['token'] = token
        else:
            self.conn_params['token']['JSESSIONID'] = auth_token
        self._connected = True#optimistic assumption that the token is valid, otherwise server would return an error anyways
        return self
        
    def invoke_method(self, method, path, path_params=None, query_params=None, form_params=None,  data=None, version=None, custom_headers=None, files=None):
        """
        Invoke a web service GET, POST, PUT or DELETE method.
        
        The path should be the relative path to the method with standard
        Python format specifiers for any path parameters, for example path would identify the resource variable in the following pattern
        'https://%(host)s:%(port)s/agility/api/%(version)s/%(resource)s'. Any path parameters
        specified are then substituted into the path.
        """
        if path_params is None:
            path_params = {}
        if query_params is None:
            query_params = {}
        if form_params is None:
            form_params = {}
        if custom_headers is None:
            custom_headers = {}
            
            
        path_params = self._params_to_string(path_params)
        query_params = self._params_to_string(query_params)
        
        self.conn_params['resource'] = path
        if version:
            self.conn_params['version'] = version
        self.url_base = 'https://%(host)s:%(port)s/agility/api/%(version)s/'%self.conn_params

        url = self._build_url(path, path_params, query_params)
        logger.info("url:=%s"%url)
        
        response = None
        try:
            response = self.request(url, method, custom_headers, data, form_params, files=files)
        except RESTException as ex:
            exc_code = ex.info['code']
            exc_message = ex.info['message']
            exc_body = ex.info['body']
            if exc_code in self.http_exception_hooks:
                exception_class, message = self.http_exception_hooks[exc_code]
                raise exception_class(message if message else exc_message if exc_message else exc_body)
            raise#else re-throw
        
        return response
            
    
    @reauthenticate
    def request(self, url, method='GET', custom_headers=None, data=None, form_params=None, files=None):
        assert self._connected, 'Not connected, call connection.connect(...)'
        _form_params = form_params or {}
        files = files or []
        headers = {"Content-Type" : CONTENT_TYPE_APLICATION_XML}
        
        if self._auth == 'basic':
            headers["Authorization"] = "Basic %s" % self._auth_string
        elif self._auth == 'oauth' and not self.conn_params['use_cookies']:
            headers["Cookie"] = self.get_token()
        
        if custom_headers:
            headers.update(custom_headers)
        request = urllib.request.Request(url)
        formtext = ''
        form = None
        for k, v in list(headers.items()):
            request.add_header(k, v)
        request.get_method = lambda: method
        
        if data is not None:
            request.data = bytes(data, 'utf-8')
            request.add_header('Content-Length', len(data))
        
        elif _form_params:
    #            _form_params = self._params_to_string(_form_params)
            form = MultiPartForm()
            [form.add_field(k, v) for k, v in list(_form_params.items())]
        if files:
            request.add_header('Accept', '*/*')
            form = form or MultiPartForm()
            [form.add_file(os.path.basename(filename), filename, open(os.path.realpath(os.path.expanduser(filename)))) if isinstance(filename, str) else form.add_archive(filename) for filename in files]
    #            body = urllib.urlencode(_form_params)
        if form:
            formtext = str(form)
            request.add_data(formtext)
            request.add_header('Content-Length', len(formtext))
            request.add_header('Content-Type', form.get_content_type())
        
        #logger.debug('REST [%s]: [%s] headers: [%s] data: [%s] form: [%s]', method, url, request.headers, data, formtext)
        #urllib2.Request would use POST if request has data, otherwise would do a GET, check if this complies with expectations
        response = None
        try:
            response = self._opener.open(request)
        except urllib.error.HTTPError as ex:
            restEx = RESTException(ex)
            logger.error(restEx)
            raise restEx
        return response
        

    def _params_to_string(self, params):
        """
        Convert the values in a parameter map into strings suitable for
        sending to the server. Any null values will be omitted.
        """
        new_params = {}
        for key, value in params.items():
            if key.find('query_params') >= 0:
                new_params.update(self._params_to_string(value))
                continue
            if value != None:
                if isinstance(value, bool):
                    if value: new_params[key] = "true"
                    else: new_params[key] = "false"
                elif isinstance(value, list) or isinstance(value, tuple):
                    new_params[key] = ",".join(value)
                elif not isinstance(value, str):
                    new_params[key] = str(value)
                else:
                    new_params[key] = value

        return new_params

    def _build_url(self, path, path_params={}, query_params={}):
        """
        Build the full URL needed to invoke a method in the web service API.

        The path may contain standard Python format specifiers, which will
        be substituted from the path parameters (suitably URL-encoded). Thus
        for example, given the following arguments:

            * path = "api/v1/person/%(scheme)s/%(identifier)s"
            * path_params = {"scheme": "crsid", "identifier": "dar17"}
            * query_params = {"fetch": "email,title"}

        This method will create a URL like the following:

            api/v1/person/crsid/dar17?fetch=email%2Ctitle

        Note that all parameter values are automatically URL-encoded.
        """
        for key, value in path_params.items():
            path_params[key] = urllib.parse.quote_plus(value)
        path = path % path_params

#        if not query_params.has_key("flatten"):
#            query_params["flatten"] = "true"
        _query_params = urllib.parse.urlencode(query_params)
        
        path += "?%s"%_query_params if _query_params else ''

        if path.startswith("/"):
            return "%s%s" % (self.url_base, path[1:])
        return "%s%s" % (self.url_base, path)
    

    
