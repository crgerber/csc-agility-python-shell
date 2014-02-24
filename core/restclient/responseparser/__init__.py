
import ParserBeautifulSoup as BeautifulSoup
import ParserLxml as Lxml
import ParserLxmlToModelObjects as LxmlModel
from ParserBeautifulSoup import AssetEntryBeautifulSoup
from ParserLxml import AssetEntryLxml

import sys

class PARSER():
    BEAUTIFUL_SOUP = 'BeautifulSoup'
    LXML = 'Lxml'
    LXML_MODEL = 'LxmlModel'

_current_parser = PARSER.LXML_MODEL

def register_parser(parserDialect=PARSER.LXML):
    setattr(sys.modules[__name__], '_current_parser', parserDialect)

def parser(parserDialect=None):
    currentModule = sys.modules[__name__]
    return getattr(currentModule, parserDialect or currentModule._current_parser).parse

def createProxy(dct, assetName=''):
    currentModule = sys.modules[__name__]
    return getattr(currentModule, 'AssetEntry%s'%currentModule._current_parser)(dct, assetName)
