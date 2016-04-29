'''
Created on Nov 16, 2012

@author: dawood
'''
import unittest
from core.plugin import prioritizePlugins

class Test(unittest.TestCase):


    def setUp(self):
        self.pluginConfigs = [
                              {'location' : 'a.tests.snapshot', 'dependency' : ['a.report.csv']},
                              {'location' : 'a.clients.xml', 'dependency' : []},
                              {'location' : 'a.report.csv', 'dependency' : ['a.tools.diff']},
                              {'location' : 'a.report', 'dependency' : []},
                              {'location' : 'a.tools.diff', 'dependency' : []},
                              {'location' : 'a.tools', 'dependency' : []},
                              {'location' : 'a.clients.ssh.dummy2', 'dependency' : []},
                              {'location' : 'a.clients.ssh.dummy', 'dependency' : ['a.clients.ssh.dummy2']},
                              {'location' : 'a.clients.ssh', 'dependency' : []},
                              {'location' : 'a.clients', 'dependency' : []},
                              ]
        self.allconfig = dict(list(zip(list(range(len(self.pluginConfigs))), self.pluginConfigs)))

    def tearDown(self):
        pass


    def testPrioritizePlugins(self):
        expectedResult = [(9, {'dependency': [], 'location': 'a.clients'}),
                        (8, {'dependency': [], 'location': 'a.clients.ssh'}),
                        (6, {'dependency': [], 'location': 'a.clients.ssh.dummy2'}),
                        (7, {'dependency': ['a.clients.ssh.dummy2'], 'location': 'a.clients.ssh.dummy'}),
                        (1, {'dependency': [], 'location': 'a.clients.xml'}),
                        (3, {'dependency': [], 'location': 'a.report'}),
                        (5, {'dependency': [], 'location': 'a.tools'}),
                        (4, {'dependency': [], 'location': 'a.tools.diff'}),
                        (2, {'dependency': ['a.tools.diff'], 'location': 'a.report.csv'}),
                        (0, {'dependency': ['a.report.csv'], 'location': 'a.tests.snapshot'})]
        actualResult = prioritizedPlugins = prioritizePlugins(self.allconfig)
        self.assertEqual(actualResult, expectedResult, 'error ordering plugin according to dependency')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()