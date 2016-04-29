'''
Created on Oct 24, 2012

@author: dawood
'''
import unittest
from core.restclient import responseparser

class ClientTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.parse_bs = responseparser.parser(responseparser.PARSER.BEAUTIFUL_SOUP)
        self.parse_lxml = responseparser.parser(responseparser.PARSER.LXML)
        self.xmlFile = '../agilityFieldTestBench/cba_s1_8.1.4_v2.0_snapshot/environments/10.231.219.132/8.1.4/Network/details/1_Network.xml'
        self.typeName = 'Network'

    def testName(self):
        network_bs = self.parse_bs(open(self.xmlFile).read(), 'Network')
        network_lxml = self.parse_lxml(open(self.xmlFile).read(), 'Network')
        print(network_bs)
        print(network_lxml)
        self.assertEqual(network_bs, network_lxml, 'mismatched objects for asset [%s]'%network_bs.typeName)
    def tearDown(self):
        unittest.TestCase.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()