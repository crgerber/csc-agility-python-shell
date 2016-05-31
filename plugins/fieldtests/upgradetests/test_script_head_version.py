'''
Created on Oct 24, 2012

@author: dawood
'''
from agilityshell import agility
import os
import unittest
from unittest import TestCase
import fixtures
from fixtures.scriptfixture import ScriptFixture

import logger
COMPONENT_NAME = 'agility-testbench'
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))
class TestScriptElginUpgrade(TestCase):

    def setUp(self):
        "set up test fixtures"
        before = False
        self.snapshot = ScriptFixture.SNAPSHOT.NEW if before else ScriptFixture.SNAPSHOT.LOAD
        self.scriptFixture = ScriptFixture(agility.cfg.conn, snapshot=self.snapshot)
#        snapshotpath = '/Users/dawood/Documents/workspace/dist_0.2/shellsnapshot'
#        snapshotpath = os.path.join(agility.cfg.path.rootdir, 'shellsnapshot')
        snapshotpath = agility.cfg.path.rootdir
        self.scriptFixture.configure(client='cba', baseDir=snapshotpath)
        self.scriptFixture.setUp()
        
    def test_headVersionIntact(self):
        if self.snapshot == ScriptFixture.SNAPSHOT.NEW:
            logger.info('Running in snapshot mode, skipping test method')
            return
        scriptMap = agility.tools.scripting.idmap(self.scriptFixture.detailedAssetList)
        fields = ['id', 'name', 'version', 'latest']
        actualScriptMap = agility.tools.scripting.idmap(agility.script.listDetails())
        self.assertTrue(agility.tools.report.diff.assertEqual(scriptMap, actualScriptMap, fields=fields, mode=agility.tools.report.diff.COMPARE_MODE.EXACT, _logger=logger), 'Script attributes changed')
        
        
        
    def tearDown(self):
        "tear down test fixtures"
        pass
def main():
    unittest.main()
if __name__ == "__main__":
    main()
