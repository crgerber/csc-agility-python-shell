#!/usr/bin/python

# --------------------------------------------------------------------------
# Copyright (c) 2012, University of Cambridge Computing Service
#
# This file is part of the Lookup/Ibis client library.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Dean Rasheed (dev-group@ucs.cam.ac.uk)
# --------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Original code can be found here: https://dev.csi.cam.ac.uk/svn/lookup/trunk/src/generate-client-methods.py
# Modified to handle Agility REST API's WADL
# Changes can be spotted by diffing with original file
#
# Requires Python 2.6 or later
#
# Change Log:
# 1. error function now throws an Exception, instead of exit(1)
# 2. handle multiple representation tags in response node, ignore mediaType(s) other than 'application/xml'
# 3. overrode code expecting resultField and resultType in the WADL (non-standard attributes)
#
# Date: Oct 2012
# Author: Shaady Dawood <shaady.dawood@servicemesh.com>
#---------------------------------------------------------------------------

import logging

ROOT_LOGGER_NAME = 'agility-clientgenerator'

logger = logging.getLogger(ROOT_LOGGER_NAME)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
LOG_FILE_NAME = '%s.log'%ROOT_LOGGER_NAME
#fh = logging.handlers.TimedRotatingFileHandler(LOG_FILE_NAME, when='D', interval=1, backupCount=5, encoding=None, delay=False, utc=False)
fh = logging.FileHandler(LOG_FILE_NAME)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

usage = """
generate-client-methods
-----------------------

Generate the client method classes from the Lookup/Ibis application.wadl.

The generated code relies on specific hand-written code in separate files
to actually send requests to the server and decode the results. The
auto-generated client methods contain the details of all the API methods,
including their parameters, documentation and the URLs on the server
needed to invoke them.

Usage: generate-client-methods [options] <wadl_file>

Where <wadl_file> is the location of the application.wadl file.
The following options are supported:

    -lang <language>    Specify the Language of the generated code. This
                        may be any of the following:

                            * "java" 
                            * "python" (the default)
                            * "php"

    -d <output_dir>     The directory in which to write the output code.
                        This defaults to the current directory.

NOTE: The generated code files are only touched if they actually need to
be modified. Otherwise their original timestamps are preserved.

"""

import re
import os
import sys
import xml.dom.minidom
from xml.dom import *

validSymbol = lambda txt, prefix='': re.sub('^[\W|\d]|\W+?', '_', prefix + txt)
isValidSymbol = lambda txt: re.match('^\W|.*\W+.*', txt) is None

lang = "python"
out_dir = "."
wadl_file = None
api_version = None

#Agility control directives
__AGILITY__PARSE_RESULT_FIELD__ = False

def error(msg, context=None):
    raise RuntimeError("ERROR: %s\n" % msg)

def warning(msg, context=None):
    sys.stderr.write("WARNING: %s\n%s" %(msg, 'CONTEXT: %s\n'%context if context else ''))

# ==========================================================================
# Code to read and parse the WADL file.
# ==========================================================================

class Param(object):
    """
    A class representing a method parameter.
    """
    def __init__(self, node=None, kind='', name='', path=None, cleanupName=True, doc=''):
        """
        Create a Param instance from a <param> node in the WADL file. This may
        be a path parameter, a query parameter or a form parameter.
        """
        self.kind = node.getAttribute("type") if node else kind
        self.name = node.getAttribute("name") if node else name
        if cleanupName:
            self.name = re.sub('\W', '_', self.name)
        self.required = False
        self.defaultValue = None
        self.path = path
        self.path_start_index = -1
        self.path_end_index = -1
        self.alias = self.name
        self.doc = doc
        for k, v in self.__dict__.items():
            if isinstance(v, (unicode)):
                setattr(self, k, str(v))

        self._id_attrs = ('kind', 'name', 'alias', 'required', 'defaultValue')
        
    def getDocs(self, doc_indent=''):
        return doc_indent + (self.doc or '''@param %(alias)s: %(alias)s\n%(indent)s@type %(alias)s: str'''%{'alias' : self.alias, 'indent' : doc_indent})
        
    def format(self):
        if '*' in self.name: #handle any special *args or **kwargs without messing up the syntax
            return self.name
        return '%s%s%s'%(self.alias, 
                         '=' if not self.required else '', 
                         str(self.defaultValue) if not self.required else '')
    def __str__(self):
        return str({idattr : getattr(self, idattr) for idattr in self._id_attrs})
        
    def __eq__(self, other):
        return eval(repr(self)) == eval(repr(other))
        
    def __hash__(self):
        id_string = ''.join([str(getattr(self, id_attr)) for id_attr in self._id_attrs])
        return hash(id_string)

    __repr__ = __str__


class Method(object):
    """
    A class representing an API method contained in a second-level resource
    from the WADL file. Note that there may be multiple methods in a second-
    level resource node (if they have the same path and path parameters).
    """
    def __init__(self, node, cls, idx, level=2):
        """
        Create a Method instance from a second-level <resource> node in the
        WADL file. The idx argument specifies which method to use (0, 1, ...)
        in the case where the <resource> node contains multiple <method>
        nodes.
        """
        # Get the method path and prefix it with the class's path
        path1 = cls.path
        if path1.startswith("/"): path1 = path1[1:]
        if path1.endswith("/"): path1 = path1[:-1]
        
        if level==2:
            path2 = node.getAttribute("path")
            if path2.startswith("/"): path2 = path2[1:]
        else:
            path2 = ''

        self.path = str(path1) + ("/" if path2 else '') + str(path2)

        # Look for path <param> nodes and the required <method> node
        self.path_params = []
        method_idx = 0
        method = None
        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                if child.tagName == "param":
                    pattern = '\{%s:*\s*[^\}]*\}'
                    newparam = Param(child, path=self.path)
                    match = re.search(pattern%newparam.name, self.path)
                    if match:
                        newparam.path_start_index = match.start()
                        newparam.path_end_index = match.end()
                         
                    self.path_params.append(newparam)
                elif child.tagName == "method":
                    if method_idx == idx: method = child
                    method_idx += 1

        # Get the method name and kind (GET, POST, PUT or DELETE)
        if method == None:
            error("Failed to find <method> node under <resource> node")

        self.name = str(method.getAttribute("id"))
        self.kind = str(method.getAttribute("name"))

        if __AGILITY__PARSE_RESULT_FIELD__:
            # Get the method result field and type (colon separated)
            self.result_field = method.getAttribute("resultField")
            idx = self.result_field.find(":")
            if idx == -1:
                error("Invalid method result field '%s'" % self.result_field)
    
            self.result_type = self.result_field[idx+1:]
            self.result_field = self.result_field[:idx]

        # Find the method docs, if any
        self.docs = ""
        self.doc_indent = "        "
        for child in method.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and\
               child.tagName == "doc":
                self.docs = child.firstChild.nodeValue
                break

        # Look for a <request> child node (holds any non-path parameters)
        request = None
        for child in method.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and\
               child.tagName == "request":
                if request != None:
                    error("Can't handle multiple <request> nodes under "\
                          "a single <method> node")
                request = child

        # Process any query parameters in the <request> node, and look
        # out for a <representation> node holding form parameters
        self.query_params = []
        representation = None
        UNSUPPORTED_MEDIA_TYPES = ['application/x-amf']
        request_mediaType = None
        if request != None:
            for child in request.childNodes:
                if child.nodeType == Node.ELEMENT_NODE:
                    if child.tagName == "param":
                        self.query_params.append(Param(child))
                    elif child.tagName == "representation":
                        if representation != None:
                            warning("Method [%s] Can't handle multiple <representation> "\
                                  "nodes under a <request> node, ignoring representation %s"%(self.name, child.getAttribute('mediaType')))
                        else:
                            _mediaType = str(child.getAttribute('mediaType'))
                            if _mediaType not in UNSUPPORTED_MEDIA_TYPES:
                                representation = child
                                request_mediaType = _mediaType

        # Finally process any form parameters in the <representation> node
        self.form_params = []
        if representation != None:
            for child in representation.childNodes:
                if child.nodeType == Node.ELEMENT_NODE and\
                   child.tagName == "param":
                    self.form_params.append(Param(child))
                    
        #if there are {<param>} within the url, mark all as required except for the last one
        #example <resource path="{id}/policy/{policyid}"> container_id must be supplied, while policyid is optional, if missing, all policies under the specified contianer will be returned             
        
        #sort the list of path params according to the location in the path template string, mark every param but the very last one as required, since they would be part of the service endpoint URI
        self.path_params.sort(key=lambda p: p.path_end_index, reverse=False)
        if self.path_params:
            if len(self.path_params) > 1:
                [setattr(param, 'required', True) for param in self.path_params[:-1]]
            else: #one param, check if it is contextual
                singleparam = self.path_params[0]
                if singleparam.path_end_index < len(singleparam.path):
                    singleparam.required = True
        
        self.rename_params()
        self.all_params = self.path_params +\
                          self.query_params + self.form_params#, Param(name='custom_headers', kind='str')]
        
        self.hasData = False
        if self.kind in ('POST', 'PUT'):
            self.all_params += [Param(name='data', kind='str', doc='''@param data: POST or PUT data, can be XML text or content of file to import\n%s@type data: str'''%self.doc_indent)]
            self.hasData = True
        
        self.hasFiles = False    
        if request_mediaType in ('application/x-zip', 'multipart/mixed'):
            self.all_params += [Param(name='files', kind='str', doc='''@files: list of file paths, would be encoded as multipart request, e.g. attachments\n%s@type: list'''%self.doc_indent)]
            self.hasFiles = True
            
        self.all_params += [Param(name='**kwargs', kind='str', cleanupName=False, doc='''@param **kwargs: keyword arguments param1=value1, param2=value2, will be used as the URL parameters: https://url?param1=value1&param2=value2\n%s@type **kwargs: keyword argument list or expanded dict, e.g. **dct'''%self.doc_indent)]
            
        
        self.custom_headers = {'Content-Type' : request_mediaType} if request_mediaType else {}

    def rename_params(self):
        def findbackwards(text, sub, start):
            idx = start if start <= len(text) else len(text)
            while idx > 0:
                if text[idx] == '/':
                    return idx + 1
                idx -= 1
            return idx

        path_params = self.path_params
        path = self.path
        pattern = '/\{%s:*\s*[^\}]*\}'
        newnames = set()
        for param in path_params:
            alias = param.name
            match = re.search(pattern%param.name, path)
            if match:
                start_index = match.start()
                end_index = match.end()
                node_start = findbackwards(path, '/', start_index - 1)
                alias = path[node_start:start_index]#parent service endpoint name
                generic_param_pattern = '\{\w+:*\s*[^\}]*\}'
                consecutiveParams = re.search(generic_param_pattern, alias)
                if consecutiveParams:#path = /xyz{param1}/{param2}
                    pass
                else:
                    if str(param.name).startswith(alias):
                        pass
                    else:
                        newname = '%s_%s'%(alias, param.name)
                        param.alias = '%s%s'%(newname, '2' if newname in newnames else '')
            newnames.add(param.alias)
        return

        

    def get_docs(self):
        """
        Get the documentation for this method (decorated with the method's
        HTTP method and path).
        """
        required_query_params = []
        for param in self.query_params:
            if ("@param %s [required]" % param.name) in self.docs:
                required_query_params.append("%s=..." % param.name)

        if required_query_params:
            doc_params = "?%s" % ("&".join(required_query_params))
        else:
            doc_params = ""

        style = "background-color: #eec;"
        extra_docs = '<code style="%s">[ HTTP: %s /%s%s ]</code>'\
                     % (style, self.kind, self.path, doc_params)

        if self.docs == "":
            return "    /**\n     * %s\n     */" % extra_docs

        i1 = self.docs.find("@param")
        i2 = self.docs.find("@return")
        if i1 == -1: idx = i2
        elif i2 == -1: idx = i1
        else: idx = min(i1, i2)
        if idx == -1: idx = self.docs.rfind("*/")
        idx = self.docs.rfind("\n", 0, idx)
        if self.docs[:idx].endswith("     *"):
            idx = self.docs.rfind("\n", 0, idx-1)

        return "%s\n     * <p>\n     * %s%s"\
               % (self.docs[:idx], extra_docs, self.docs[idx:])
               
    def __hash__(self):
        return self.name.__hash__()


    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, self.__class__):
            return false
        return self.name == other.name
    
class MethodClass(object):
    """
    A class representing a top-level resource from the WADL file.
    """
    def __init__(self, node, className, path):
        """
        Create a method class instance from a top-level <resource> node in
        the WADL file.
        """
        cleanedup_classname = re.sub("Resource$", "Methods", className)
        pattern = '/*\{:*\s*[^\}]*\}/*' #cleanup resource names of the format: blueprint/{bp_id}/workload
        cleanedup_classname = re.sub(pattern, '_', className)
        cleanedup_classname = re.sub('\W', '_', cleanedup_classname) #remove any '/' or illegal characters
        self.name = cleanedup_classname
        self.path = str(path)

        # Find the class docs, if any
        self.docs = ""
        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and\
               child.tagName == "doc":
                self.docs = child.firstChild.nodeValue
                break

        # Find any methods on the class
        self.methods = {}
        method_idx = 0
        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                if child.tagName == "method":
                    newmethod = Method(node, self, method_idx, level=1)
                    if newmethod.name in self.methods:
                        updateMethodName(self, newmethod, self.methods[newmethod.name], self.methods)
                    else:
                        self.methods[newmethod.name] = newmethod
                    method_idx += 1
                elif child.tagName == "resource":
                    method_idx = 0
                    for grandchild in child.childNodes:
                        if grandchild.nodeType == Node.ELEMENT_NODE and\
                           grandchild.tagName == "method":
                            newmethod = Method(child, self, method_idx, level=2)
                            if newmethod.name in self.methods:
                                updateMethodName(self, newmethod, self.methods[newmethod.name], self.methods)
                            else:
                                self.methods[newmethod.name] = newmethod
                            method_idx += 1
############ Dedup Map Initializer @todo group globals in a datastructue ##########
duplicateMethodNames = {}
try:
    from dedup_map import duplicateMethods
except ImportError, ex:
    duplicateMethods = {}
############ Dedup Map Initializer @todo group globals in a datastructue ##########
def persistDedupLog(dirpath='.', filename='dedup_map.py'):
    with open(os.path.join(dirpath, filename), 'w') as dedup_log:
        dedup_log.write('duplicateMethods = %s'%str(duplicateMethods))

def updateMethodName(cls, method, othermethod, methodsMap):
    # if api_version == 'v2_0':
    #     return updatedMethodName_v2_0(cls, method, othermethod, methodsMap)
    return resolveMethodNameConflict(cls, method, othermethod, methodsMap)

def resolveMethodNameConflict(cls, method, othermethod, methodsMap):
    method_to_dict = lambda cls, m:  {'class' : cls.path,'name' : m.name, 'kind' : m.kind, 'path' : m.path, 'Content-Type' : m.custom_headers, 'path_params' : m.path_params, 'path_param_names' : '_'.join([str(p.name) for p in m.path_params]), 'method_alias' : m.name}
    methodentry = method_to_dict(cls, method)
    othermethodentry = method_to_dict(cls, othermethod)
    #othermethodentry = {'class' : cls.path,'name' : othermethod.name, 'kind' : othermethod.kind, 'path' : othermethod.path, 'Content-Type' : othermethod.custom_headers, 'path_params' : othermethod.path_params, 'path_param_names' : '_'.join([str(p.name) for p in othermethod.path_params]), 'method_alias' : othermethod.name}
    keytemplate = '%(class)s_%(name)s_%(path)s_%(Content-Type)s_%(path_param_names)s'
    methodKey = str(keytemplate%methodentry)
    othermethodKey = str(keytemplate%othermethodentry)

    if methodKey not in duplicateMethodNames:
#        duplicateMethodNames.append(methodentry)
        duplicateMethodNames[methodKey] = methodentry
    if othermethodKey not in duplicateMethodNames:
#        duplicateMethodNames.append(othermethodentry)
        duplicateMethodNames[othermethodKey] = othermethodentry

    if methodKey not in duplicateMethods or othermethodKey not in duplicateMethods:
        methodAlias, othermethodAlias = promptResolveMethodNameConflict(methodentry, othermethodentry)
    else:
        methodAlias = duplicateMethods[methodKey]['method_alias']
        othermethodAlias = duplicateMethods[othermethodKey]['method_alias']

    warning('Duplicate method definition [%s.%s], renaming to [%s]' %(cls.name, method.name, methodAlias))
    del methodsMap[method.name]
    method.name = methodAlias
    methodsMap[methodAlias] = method


    warning('Duplicate method definition [%s.%s], renaming to [%s]' %(cls.name, othermethod.name, othermethodAlias))
    othermethod.name = othermethodAlias
    methodsMap[othermethodAlias] = othermethod

    #cache up-to-date dicts
    duplicateMethods[methodKey] = method_to_dict(cls, method)
    duplicateMethods[othermethodKey] = method_to_dict(cls, othermethod)
    persistDedupLog()
    return

def promptResolveMethodNameConflict(methodentry, othermethodentry):
    print 'Method name conflict, under the same endpoint:'
    print '1. %s'%methodentry
    print '-'*30
    print '2. %s'%othermethodentry
    print '-'*30
    #@todo convert Method/Param classes to hashable object, suggest smarter renaming using info about path params
    while True:
        method_alias = raw_input('Enter an alias for method (1): [%s] '%methodentry['name'])
        method_alias = '%s%s'%(methodentry['name'], method_alias[1:]) if method_alias.startswith('*') else method_alias if method_alias else methodentry['name']
        other_method_alias = raw_input('Enter an alias for method (2): [%s] '%othermethodentry['name'])
        other_method_alias = '%s%s'%(othermethodentry['name'], other_method_alias[1:]) if other_method_alias.startswith('*') else other_method_alias if other_method_alias else othermethodentry['name']
        if method_alias == methodentry['name'] \
                and other_method_alias == othermethodentry['name'] \
                or method_alias == other_method_alias:
            print 'Method aliases can not be the same for both methods, try again ...'
            continue
        else:
            break
    return method_alias, other_method_alias



def updatedMethodName_v2_0(cls, method, othermethod, methodsMap):
    from agility_rest_generator_helper import duplicateMethods
    methodentry = {'class' : cls.path,'name' : method.name, 'path' : method.path, 'Content-Type' : method.custom_headers, 'path_params' : method.path_params, 'path_param_names' : '_'.join([str(p.name) for p in method.path_params]), 'method_alias' : method.name}
    othermethodentry = {'class' : cls.path,'name' : othermethod.name, 'path' : othermethod.path, 'Content-Type' : othermethod.custom_headers, 'path_params' : othermethod.path_params, 'path_param_names' : '_'.join([str(p.name) for p in othermethod.path_params]), 'method_alias' : othermethod.name}
    keytemplate = '%(class)s_%(name)s_%(path)s_%(Content-Type)s_%(path_param_names)s'
    methodKey = str(keytemplate%methodentry)
    othermethodKey = str(keytemplate%othermethodentry)
    assert methodKey in duplicateMethods
    assert othermethodKey in duplicateMethods
    if methodKey not in duplicateMethodNames:
#        duplicateMethodNames.append(methodentry)
        duplicateMethodNames[methodKey] = methodentry
    if othermethodKey not in duplicateMethodNames:
#        duplicateMethodNames.append(othermethodentry)
        duplicateMethodNames[othermethodKey] = othermethodentry
    methodAlias = duplicateMethods[methodKey]['method_alias']
    warning('Duplicate method definition [%s.%s], renaming to [%s]' %(cls.name, method.name, methodAlias))
    del methodsMap[method.name]
    method.name = methodAlias
    methodsMap[methodAlias] = method

    othermethodAlias = duplicateMethods[othermethodKey]['method_alias']
    warning('Duplicate method definition [%s.%s], renaming to [%s]' %(cls.name, othermethod.name, othermethodAlias))
    othermethod.name = othermethodAlias
    methodsMap[othermethodAlias] = othermethod
    
    return 

class Application(object):
    """
    A class representing the entire web service API.

    This is basically just a list of top-level resources, which are
    represented as MethodClass objects.
    """
    def __init__(self, app):
        """
        Create the Application from the top-level <application> node in the
        WADL file, creating all the child objects underneath it.
        """
        self.classes = []

        # Look for the <resources> node
        resources = None
        for child in app.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and\
               child.tagName == "resources":
                resources = child
                break
        if resources == None:
            error("Failed to find '<resources>' node")

        # Process each child <resource> node (class definitions)
        classes_found = set()
        for child in resources.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and\
               child.tagName == "resource":
                path = child.getAttribute("path")
                className = child.getAttribute("className")
                if not className:
                    if path[0] != '/':
                        warning('Top level resource [%s] should be named [/%s]'%(path, path))
                        className = path
                    else:
                        className = path[1:]
                if path != None and className != None:
                    if className in classes_found:
                        error("Found 2 copies of class '%s'" % className)
                    classes_found.add(className)
                    self.classes.append(MethodClass(child, className, path))

# ==========================================================================
# Common code to help generate client code.
# ==========================================================================


def aligned_output(cols, indent, tab_size=4):
    """
    Pretty printing function to output tabular data containing multiple
    columns of text, left-aligned.

    The first column is aligned at an indentation of "indent". Each
    successive column is aligned on a suitable multiple of the "tab_size"
    with spaces for all indentation.

    "cols" is assumed to be a list of columns, with each column holding
    an equal length list of string values.
    """
    # Check the input data
    ncols = len(cols)
    if ncols == 0: return ""
    nrows = len(cols[0])
    if nrows == 0: return ""

    # Work out the indentations and widths of each column
    indents = [ indent ]
    widths = []
    for col in range(1, ncols):
        width = max(len(x) for x in cols[col-1])
        indents.append(((indents[col-1]+width+tab_size) / tab_size) * tab_size)
        widths.append(indents[col] - indents[col-1])

    # Now output the actual tabular values
    result = ""
    for row in range(0, nrows):
        if row > 0:
            result += ",\n" + (" " * indent)
        if len(cols) > 1:
            for col in range(0, ncols-1):
                result += cols[col][row].ljust(widths[col])
        result += cols[-1][row]
    return result

def javadocs_to_text(docs, line_prefix=""):
    """
    Convert some javadocs to plain text.
    """
    docs = docs.strip()

    # Remove start and end javadoc comments
    if docs.startswith("/**"): docs = docs[3:].strip()
    if docs.endswith("*/"): docs = docs[:-2].strip()

    # Replace comment line prefixes with the specified line prefix
    docs = re.sub("(?m)^\\s*[*][ ]?", line_prefix, docs)

    # Replace <li> with "*" for plain text bullet points
    docs = re.sub("<li>\\s*", "* ", docs)

    # Remove any other HTML tags
    docs = re.sub("<[^>]+>", "", docs)

    # Strip off end-of-line whitespace
    docs = re.sub("(?m)\\s+$", "\n", docs)

    return docs

def comment_out(text, comment="#"):
    """
    Comment out some text, using the specified comment character(s) at the
    start of each line.
    """
    text = text.strip()

    result = ""
    for line in text.split("\n"):
        if line: result += comment+" "+line+"\n"
        else: result += comment+"\n"

    return result.strip()

def update_file_if_changed(filename, contents):
    """
    Update a file using the specified contents. We deliberately avoid touching
    the file if it's contents haven't changed, so that re-compiles aren't
    triggered unnecessariliy, and tar/jar files don't need updating if nothing
    has really changed.
    """
    if len(content) < 10:
        error("Failed to generate valid file contents")

    # Any existing file contents
    try:
        f = open(filename, "rb")
        try:
            old_content = f.read()
        finally:
            f.close()
    except IOError:
        old_content = None

    # Write the file if it has changed (or didn't exist)
    if content != old_content:
        f = open(filename, "wb")
        try:
            f.write(content)
            print "%s ... *** UPDATED ***" % filename
        finally:
            f.close()
    else:
        print "%s ... unchanged" % filename

# ==========================================================================
# Code to generate the Python methods module.
# ==========================================================================

def generate_python_method(method):
    """
    Generate the Python code for a single web service API method, using the
    PYTHON_METHOD_TEMPLATE.
    """
    # Method parameters
    param_names = ["self"]
            
    [param_names.append(param.format()) for param in method.all_params]        
    method_params = aligned_output([param_names], 9 + len(method.name))
    doc_indent = method.doc_indent
    # Method docs in plain text
    docs = javadocs_to_text(method.get_docs(), doc_indent)

    # Path parameters
    param_pairs = [ '"'+x.name+'": '+x.alias for x in method.path_params ]
    path_params = aligned_output([param_pairs], 23)

    # Query parameters
    param_pairs = [ '"'+x.name+'": '+x.name for x in method.query_params ]
    query_params = aligned_output([param_pairs], 24)

    # Form parameters
    param_pairs = [ '"'+x.name+'": '+x.name for x in method.form_params ]
    form_params = aligned_output([param_pairs], 23)

    # Method path - replace any placeholders with Python format specifiers
    path = re.sub("\{([^}]+)\}", "%(\\1)s", method.path)

    if __AGILITY__PARSE_RESULT_FIELD__:        
        # Final method result (only int and boolean value fields need to be
        # coerced into the required type)
        if method.result_type == "boolean":
            result = "result.value and result.value.lower() == \"true\""
        elif method.result_type == "int":
            result = "int(result.value)"
        else:
            result = "result.%s" % method.result_field
    else:
        result = 'result'
    process_data_objects_code = '''if data is not None:
            data = str(data)
'''
    method_context = { "method_name": method.name,
                                      "method_params": method_params,
                                      "method_docs": docs,
                                      "param_docs" : '\n'.join([p.getDocs(doc_indent) for p in method.all_params]),
                                      "path_params": path_params,
                                      "query_params": query_params,
                                      "form_params": form_params,
                                      "method_kind": method.kind,
                                      "method_path": path,
                                      "result": result,
                                      "custom_headers" : method.custom_headers,
                                      "files" : 'files' if method.hasFiles else None,
                                      "hasData" : method.hasData,
                                      "data" : 'data' if method.hasData else None,
                                      "process_data_objects" : process_data_objects_code if method.hasData else ''}
    
    meta_context = {"method_name": method.name,
                                      "method_params": method.all_params,
                                      "method_docs": docs,
                                      "path_params": method.path_params,
                                      "query_params": method.query_params,
                                      "form_params": method.form_params,
                                      "method_kind": method.kind,
                                      "method_path": path,
                                      "result": result,
                                      "custom_headers" : method.custom_headers,
                                      "hasFiles" : method.hasFiles,
                                      "hasData" : method.hasData,
                    }
    meta_context = dict([(k, str(v).strip() if isinstance(v, (str, unicode)) else v)for k, v in meta_context.items()])
    method_context['method_context'] = meta_context
    PYTHON_METHOD_TEMPLATE = open(os.path.join('templates', 'python', 'method.txt')).read()
    return PYTHON_METHOD_TEMPLATE % method_context


def generate_python_class(cls):
    """
    Generate the Python code for a single XxxMethods class, using the
    PYTHON_CLASS_TEMPLATE.
    """
    docs = javadocs_to_text(cls.docs, "    ")
    methods = "\n".join(generate_python_method(x) for x in cls.methods.values())
    PYTHON_CLASS_TEMPLATE = open(os.path.join('templates', 'python', 'class.txt')).read()
    return PYTHON_CLASS_TEMPLATE % { "class_name": cls.name,
                                     "class_docs": docs,
                                     "methods": methods }

def generate_python_module(app):
    """
    Generate the Python code for the entire methods module, containing all
    the XxxMethods classes, using the PYTHON_MODULE_TEMPLATE.
    """
    classes = "\n".join(generate_python_class(x) for x in app.classes)
    LICENSE = open(os.path.join('templates', 'license.txt')).read()
    PYTHON_MODULE_TEMPLATE = open(os.path.join('templates', 'python', 'module.txt')).read()
    return PYTHON_MODULE_TEMPLATE % { "licence": comment_out(LICENSE),
                                      "classes": classes }



# ==========================================================================
# Main entry point.
# ==========================================================================

if __name__ == "__main__":

    # Parse the command line arguments
    num_args = len(sys.argv)
    if num_args > 1 and (sys.argv[1][:2] == "-h" or sys.argv[1] == "--help"):
        sys.stdout.write(usage)
        sys.exit(0)

    arg = 1
    while arg < num_args:
        if sys.argv[arg] == "-lang":
            arg += 1
            if arg >= num_args:
                error("No language specified")
            lang = sys.argv[arg].lower()
            arg += 1
        elif sys.argv[arg] == "-d":
            arg += 1
            if arg >= num_args:
                error("No output directory specified")
            out_dir = sys.argv[arg]
            arg += 1
        elif sys.argv[arg] == "-v":
            arg += 1
            if arg >= num_args:
                error("No API version specified")
            api_version = sys.argv[arg].replace('.', '_')
            arg += 1
        elif arg == num_args-1:
            wadl_file = sys.argv[arg]
            arg += 1
        else:
            error("Invalid option: '%s'" % sys.argv[arg])

    if wadl_file == None:
        error("No WADL file specified")

    # Read and parse the WADL file
    doc = xml.dom.minidom.parse(wadl_file)
    app = Application(doc.documentElement)

    # Create/update the output file(s) as necessary
    
    if lang == "python":
        out_dir = os.path.join(out_dir, api_version)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        filename = os.path.join(out_dir, "methods.py")
        content = generate_python_module(app)
        update_file_if_changed(filename, content)
    else:
        error("Unsupported language: '%s'" % lang)
    print duplicateMethodNames
    persistDedupLog()


