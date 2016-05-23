'''
Created on Apr 30, 2013

@author: dawood
'''
import time
import os
import mimetypes
from io import StringIO
from core.agility.common.AgilityModelBase import AgilityModelBase

COMPONENT_NAME = __name__
from logger import getLogger
logger = getLogger(COMPONENT_NAME)

class LocalArchive(AgilityModelBase):
    
    def __init__(self, localPath=None, fileName=None, attachmentName=None, data=None):
        AgilityModelBase.__init__(self, logger)
        self.localPath = localPath
        self.fileName = fileName
        self.attachmentName = attachmentName or fileName
        self.data = data
        self.timestamp = time.strftime('%Y_%m_%d_%H_%M_%S')
        self.sourceServiceName = ''
        self.assetType = 'Attachment'
        self.saved = False
    
    def __repr__(self):
        dct = dict(self.__dict__)
        dct.pop('data')
        return repr(dct)
    
    __str__ = __repr__
    
    def _getSize(self):
        return 0 if self.data is None else len(self.data)
    
    size = property(fget=_getSize)
    
    def _getFullPath(self):
        return os.path.join(self.localPath, self.fileName)
    
    fullPath = property(fget=_getFullPath)
    
    def _getMimetype(self):
        return mimetypes.guess_type(self.fileName)[0] or 'application/octet-stream'
    
    mimetype = property(fget=_getMimetype)
    
    def save(self):
        if self.data is None:
            raise RuntimeError('save() invoked with empty data')
        if not os.path.exists(self.localPath):
            os.makedirs(self.localPath)
        #make sure inferred attributes are up to date
        with open(self.fullPath, 'wb') as dataFile:
            dataFile.write(self.data)
        logger.info('Successfully saved file: [%s] content info: [%s]'%(self.fullPath, self))
        self.saved = True
        return self
    
    def load(self):
        with open(self.fullPath, 'r') as fh:
            self.data = fh.read()
    
    def read(self):
        return self.data
    
    def getFileHandle(self):
        return StringIO(self.data)
        
    def close(self):
        self.data = None
        
    def getFormParts(self):
        envelopXML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Attachment xmlns="http://servicemesh.com/agility/api">
    <name>%s</name>
</Attachment>'''
        if self.assetType == 'Attachment':
            return [LocalArchive(localPath='', fileName='envelop.xml', attachmentName='attachment', data=envelopXML%self.attachmentName), self]
        else:
            return [self]
    