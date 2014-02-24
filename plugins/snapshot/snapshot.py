'''
Created on Oct 31, 2012

@author: dawood
'''
__all__ = ['loadSnapshot', 'loadSnapshots']

import os
import logging
from core.restclient import responseparser

from agilityshell import agility

parse = responseparser.parser(parserDialect=responseparser.PARSER.BEAUTIFUL_SOUP)
COMPONENT_NAME = 'snapshot'
import logger
logger = logger.getLogger(COMPONENT_NAME)


_SUMMARY = 'summary'
_DETAILS = 'details'

def loadSnapshot(persistDir, assetName, environment, systemversion=None):
    '''
    loads a persisted XML snapshot of Agility Asset Model
    
    @param persistDir: parent directory of the snapshot, typically <rootdir>/environments
    @param assetName: name of the Asset to load
    @param environment: typically hostname of the agility instance of which the snapshot was taken
    @param version: agility version, e.g. 7.4.14, 8.1.4, etc ...
    '''
    result = loadSnapshots(persistDir, assetName, environment, systemversion=systemversion)
    if not systemversion:
        systemversion = result[environment].keys()[0]  
    return result[environment][systemversion][assetName][_DETAILS]



def loadSnapshots(persistDir, assetName, environments=None, systemversion=None):
    '''
    laods persisted XML snapshots for a specific asset, grouped by environment
    
    expected dir structure:

    environments/
        <versionX.y.z>
        <versionV.w.q>
            <host1>, <host2>, ..., <hostn>/
                <host1>/
                    <Asset1>, <Asset2>, ..., <Assetn>/
                        <Asset1>/
                            summary/
                            details/
                                summary/
                                    <Asset1>.xml, <Asset2>.xml, ..., <Assetn>.xml/
                                details/
                                    <id>_<Asset1>.xml, <id>_<Asset2>.xml, ..., <id>_<Assetn>.xml

    @param assetName: name of the asset to load, e.g. 'Script'
    @param persistDir: parent dir for snapshots 
    @param environments: list of environment (host) names to load, None => ALL
    '''
    environment_selective = False
    if environments is not None:
        if isinstance(environments, str):
            environments = [environments]
            environment_selective = True
        elif not isinstance(environments, (list, tuple)):
            raise ValueError('environments argument must be a single string, or a list or strings')
        else:
            environment_selective = True
    
    assetList = []
    detailedAssetList = []
    result = {}
    selectedVersion = systemversion
    latestVersion = selectedVersion is None
    logger.info('Loading snapshot of environment(s): %s, version: [%s]', environments, selectedVersion if selectedVersion else 'latest')
    isNotHidden = lambda d: not d.startswith('.')
    for environment in filter(isNotHidden, os.listdir(persistDir)):
        if environment_selective:
            if environment not in environments:
                continue
        result[environment] = {}
        environmentPath = os.path.join(persistDir, environment)
        environment_versions = filter(isNotHidden, os.listdir(environmentPath))
        if latestVersion and environment_versions:
            selectedVersion = sorted(environment_versions)[-1]
        for environment_version in environment_versions:
            if environment_version != selectedVersion: continue
            result[environment][selectedVersion] = {}
            assetList = []
            detailedAssetList = []
            
            logger.info('Loading environment [%s] version [%s]', environment, selectedVersion)
            assetsPath = os.path.join(persistDir, environment, environment_version)
            assets = os.listdir(assetsPath)
            if assetName not in assets: raise RuntimeError('No persistent data for asset: %s found in path %s'%(assetName, assetsPath))
            assetSummaryPath = os.path.join(assetsPath, assetName, _SUMMARY)
            assetDetailesPath = os.path.join(assetsPath, assetName, _DETAILS)
            with open(os.path.join(assetSummaryPath, '%s.xml'%assetName)) as assetSummaryFile:
                assetList = parse(assetSummaryFile.read(), assetName)
                logger.info('Environment [%s], Asset [%s] summary loaded successfully', environment, assetName)
            for assetDetailesFileName in filter(isNotHidden, os.listdir(assetDetailesPath)):
                with open(os.path.join(assetDetailesPath, assetDetailesFileName)) as assetDetailsFile:
                    detailedAssetList.append(parse(assetDetailsFile.read(), assetName))
                    logger.debug('Environment [%s], version [%s], %s id=[%s] details loaded successfully', environment, selectedVersion, assetName, assetDetailesFileName.split('_')[0])
            logger.info('Environment [%s], [%s] %s details loaded successfully', environment, len(detailedAssetList), assetName)
            result[environment][selectedVersion][assetName] = {_SUMMARY : assetList, _DETAILS : detailedAssetList}
    return result

#an easy way to communicate function CONSTANTS to the outside world
loadSnapshot.SUMMARY = _SUMMARY
loadSnapshot.DETAILS = _DETAILS