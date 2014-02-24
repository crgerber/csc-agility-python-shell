'''
Created on Oct 31, 2012

@author: dawood
'''
__all__ = ['snapshot']
from collections import defaultdict
import os
import logging
#using TestFixtures to create snapshots
from core.restclient.connection import RESTConnection

from agilityshell import agility
COMPONENT_NAME = 'snapshot'
import logger
logger = logger.getLogger(COMPONENT_NAME)

loadSnapshot = agility.tools.snapshot.loadSnapshot
loadSnapshots = agility.tools.snapshot.loadSnapshots
getAssetList = agility.tools.report.getAssetList
createAssetReport = agility.tools.report._createAssetReport

def snapshot(host=None, username='admin', password=None, systemversion=None, assetNames=None, clientName='client', baseDir=''):
    '''set up test fixtures, do snapshots of all
    
    @param host: host name or address, if not specified, the current agility shell rest-connection will be used 
    '''
    conn = agility.cfg.conn if (not host) else RESTConnection(host=host, username=username, password=password, systemversion=systemversion)
    assetNames = assetNames or agility._assetNames
    persistDir = os.path.join(baseDir, 'environments')
    reportDir = os.path.join(baseDir, 'reports')
    logger.info('Creating a new snapshot: %s.%s.%s.%s', host, systemversion, 'current', assetNames)
    for assetName in assetNames:
        assetList, detailedAssetList = getAssetList(conn, assetName, getDetails=True, persistRootDir=persistDir)        
    
