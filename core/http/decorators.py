'''
Created on Nov 4, 2012

@author: dawood
'''
from functools import update_wrapper

from core.http.put.localarchive import LocalArchive


COMPONENT_NAME = __name__
from logger import getLogger
logger = getLogger(COMPONENT_NAME)

class download(object):
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        self.f = f
        update_wrapper(self, f)
        
    def __get__(self, instance, cls=None):
        self._instance = instance
        return self
    
    def __call__(self, *args, **kwargs):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        
        response = self.f(self._instance, *args, **kwargs)
        
        content_type = response.headers.get('content-type', None)
        assetType = self._instance.__class__.__name__
        serviceName = self.f.__name__
        if content_type is None:
            result = response.read()# result might be empty as well, should be handled by the parser layer
        elif content_type == 'application/xml':
            result = response.read()
        elif content_type == 'application/x-zip':
            processor = ApplicationXZipResponseHelper(response, assetType, serviceName)
            result = processor.process()
        elif content_type.startswith('multipart/mixed;'):
            processor = MultiPartMixedResponseHelper(response, assetType, serviceName)
            result = processor.process()
        else:
            raise RuntimeError('unable to handle content-type: %s'%content_type)
        return result

class NonXmlResponseHelper(object):
    KEY_FILE_NAME = 'filename'
    def __init__(self, response, assetType, serviceName):
        self.response = response
        self.assetType = assetType
        self.serviceName = serviceName
        self.content_disposition = {}
        self.data = None
    
    def process(self):
        self.parseResponse()
        return self.newArchive()
    
    def parseResponse(self):
        '''
        Process a Non-XML response
        
        Parse the response header
        Parse the content-disposition preamble for multi-part mixed
        Read the data from response body
        '''
        return True
    
    def newArchive(self, parentDir='downloads', fileName=None):
        fileName = fileName or self.content_disposition[self.KEY_FILE_NAME]
        archive = LocalArchive(localPath=parentDir, fileName=fileName, data=self.data)
        archive.assetType = self.assetType
        archive.sourceServiceName = self.serviceName
        archive.save()
        return archive
    
    def doubleSeparatorTextToMap(self, text, sep1=';', sep2='=', targetMap=None):
        '''
        example:
        'form-data;filename="agility-jenkins-plugins-1.0.0-35.e7de2eb.zip";modification-date="Mon, 29 Apr 2013 02:04:30 GMT";size=2399027;name="agility-jenkins-plugins-1.0.0-35.e7de2eb.zip"'
        '''
        result = {} if targetMap is None else targetMap
        [result.update([(part2[0].strip(), part2[1].strip().replace('"', '') if len(part2)==2 else None)]) for part2 in [part1.split(sep2, 2) for part1 in text.split(sep1)]]
        return result
        
    
class ApplicationXZipResponseHelper(NonXmlResponseHelper):
    def __init__(self, *args, **kwargs):
        super(ApplicationXZipResponseHelper, self).__init__(*args, **kwargs)
    
    def parseResponse(self):
        content_disposition = self.response.headers['content-disposition']
        self.content_disposition = self.doubleSeparatorTextToMap(content_disposition)
        self.data = self.response.read()
        return True


class MultiPartMixedResponseHelper(NonXmlResponseHelper):
    PART_MOD_DATE = 'modification-date'
    PART_NAME = 'name'
    PART_SIZE = 'size'
    PART_CONTENT_TYPE = 'Content-Type'
    def __init__(self, *args, **kwargs):
        super(MultiPartMixedResponseHelper, self).__init__(*args, **kwargs)
        self.boundary = None
        self.data = None
        
    def parseResponse(self):
        '''
        Example multipart response body:
\r\n
--Boundary_5_395831751_1367199076705
Content-Type: application/octet-stream
Content-Disposition: form-data;filename="MySQL-server-advanced-5.5.15-1.rhel5.x86_64.rpm";modification-date="Mon, 29 Apr 2013 01:31:16 GMT";size=53721622;name="MySQL-server-advanced-5.5.15-1.rhel5.x86_64.rpm"\r\n
\r\n
<DATA>
\r\n--Boundary_5_395831751_1367199076705--\r\n
'''
        if not self.response:
            return False
        content_type = self.response.headers.get('content-type', None)
        self.content_disposition = {}
        if content_type is None:
            logger.warning('missing content-type header')
            return False
        if not content_type.startswith('multipart/mixed;'):
            logger.warning('unsupported content-type: %s'%content_type)
            return False
        
        try:
            self.boundary = (content_type.split(';')[1]).split('=')[1]
        except IndexError as ex:
            RuntimeError('unable to extract boundary marker for content-type: %s'%content_type)
        
        newline = '\r\n'
        start_marker = '--' + self.boundary + newline
        end_marker = newline + '--' + self.boundary + '--' + newline
        buffer = self.response.readline()
        assert buffer == newline
        buffer = self.response.readline()
        assert buffer == start_marker
        buffer = self.response.readline()
        self.content_disposition[buffer.split(':')[0].strip()] = buffer.split(':')[1].strip()#'Content-Type: application/zip\r\n'
        buffer = self.response.readline()
        assert buffer.startswith('Content-Disposition:')
        content_disposition = buffer[len('Content-Disposition:'):].strip()
        self.doubleSeparatorTextToMap(content_disposition, sep1=';', sep2='=', targetMap=self.content_disposition)
        logger.debug('content disposition: %s'%self.content_disposition)
        buffer = self.response.readline()
        assert buffer == newline
        self.data = self.response.read()
        self.data = self.data[:-len(end_marker)]
        assert len(self.data) == int(self.content_disposition[self.PART_SIZE])
        return True
    
