'''
Created on Nov 6, 2012

@author: dawood
'''
from fixtures.computefixture import ComputeFixture
from agilityshell import agility
import unittest
from unittest import TestCase
import os

import fixtures

import agilityshell

import logger
logger = logger.getLogger(__name__)
agility._initPlugins()
class TestInstanceVolumeAttachment(unittest.TestCase):

    def setUp(self):
        self.computeFixture = ComputeFixture(agility.cfg.conn, snapshot=ComputeFixture.SNAPSHOT.LOAD)
#        snapshotpath = os.path.join(agility.cfg.path.rootdir, '../cba_snapshots/')
        snapshotpath = agility.cfg.path.rootdir
        config = dict(client = 'cba',
        baseDir = snapshotpath,
        createCSVReport = True,
        recreateCSVReport = False,
        detailedReport = True)
        self.computeFixture.configure(**config)
        self.computeFixture.setUp()
        self.curret_detailedAssetList = agility.compute.listDetails()

    def tearDown(self):
        pass


    def test_VolumeAssignment(self):
        def computeDisks(computeList):
            compute_disks = {}
            idmap = agility.tools.scripting.idmap
            getField = agility.tools.scripting.getField
            disks = lambda compute: [r for r in getField(compute, 'resources', []) if getField(r, 'resourceType', '')=='Disk Drive'] 
            [compute_disks.update([(id, disks(compute))]) for id, compute in list(idmap(computeList).items()) if disks(compute)]
            return compute_disks
            
        expectedComputeDisks = computeDisks(self.computeFixture.detailedAssetList)
        currentComputeDisks = computeDisks(self.curret_detailedAssetList)
        
        logger.info('Found [%s] compute instances with Disk resources', len(currentComputeDisks))
        
        
        
    
    def test_VolumeMounting(self):
        pass


def attributeIdMap(attributeFQN, detailedAssetList, filter=lambda attr: attr):
    levels = attributeFQN.split('.')
    attrIdMap = {}
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()