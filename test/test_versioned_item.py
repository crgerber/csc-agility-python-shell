'''
Description: 

@author: cgerber
'''
import unittest
from unittest import TestCase
import plugins.fieldtests.fixtures
from plugins.fieldtests.fixtures.scriptfixture import ScriptFixture
from core import agility as client

from agilityinit import *
agility = init()
agility._initPlugins()
conf = agility.cfg.configuration
conn = agility.cfg.conn

import os
import logging
from logger import logger, configRootLogger
logger = configRootLogger('test_versioned_item', os.path.join(SHELL_ROOT_DIR, 'logs'), 'test_versioned_item.log', conf.get(section='log', option='level'), conf.get(section='log', option='console')) 

from core.restclient.responseparser import parser
parse = parser()
 
EXACT = agility.tools.report.diff.COMPARE_MODE.EXACT
MASTER_INTACT = agility.tools.report.diff.COMPARE_MODE.MASTER_INTACT
SLAVE_INTACT = agility.tools.report.diff.COMPARE_MODE.SLAVE_INTACT
 
class VersionedItemTest(TestCase):
    
    def setUp(self):
        logger.info("Setting up test fixtures...")
        #set up test fixtures, note that this test can run before the upgrade to take a snapshot, and later after the upgrade to compare the snapshot with reality     
        self.conf = conf
        self.snapshot = ScriptFixture.SNAPSHOT.NEW 
        #self.snapshot = ScriptFixture.SNAPSHOT.LOAD
        self.scriptFixture = ScriptFixture(conn, snapshot=self.snapshot, logger=logger)
        self.scriptFixture.configure(client=client, baseDir=SHELL_ROOT_DIR)
        self.scriptFixture.setUp()
        
    def test_headVersionIntact(self):
        scriptMap = agility.tools.scripting.idmap(self.scriptFixture.detailedAssetList)
        fields = ['id', 'name', 'version', 'latest']
        details = agility.script.listDetails()
        actualScriptMap = agility.tools.scripting.idmap(details)
        isEqual = agility.tools.report.diff.assertEqual(scriptMap, actualScriptMap, fields=fields, mode=EXACT, _logger=logger)
        
        if not isEqual :
            agility.tools.report.diff.diffReport(master=scriptMap, slave=actualScriptMap, fields=fields, reportFileName='test_versioned_item_diff_report.log', reportDir=os.path.join(SHELL_ROOT_DIR, 'logs'), include=(DIFF_REPORT_INCLUDE.DELETED, DIFF_REPORT_INCLUDE.ADDED, DIFF_REPORT_INCLUDE.MODIFIED), hierarchical=False, format='csv')
        
        self.assertTrue(isEqual, 'Script attributes changed')
        
    def tearDown(self):
        logger.info("Tearing down test fixtures...")
        pass
    
def main():
    unittest.main()
if __name__ == "__main__":
    main()