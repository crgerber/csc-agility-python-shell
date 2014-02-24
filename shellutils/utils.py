'''
Created on Oct 28, 2012

@author: dawood
'''
import sys
import os
import stat

from core.base.enum import Enum
import logging
from core.restclient import responseparser
from core.proxy import serviceproxy
from core.proxy.hook import Hook

from logger import logger
def setParser(parserDialect=responseparser.PARSER.BEAUTIFUL_SOUP):
    '''
    Changes the parser used for all a.* calls parsing decorator
    '''
    serviceproxy.ParseDecorator._parse = responseparser.parser(parserDialect)
setParser.PARSER_DIALECT = responseparser.PARSER

TOOLS = {
         'xml' : Hook(**{'setParser' : setParser,
                         'parse' : responseparser.parser()})
         }

class Tools(object):
    def __init__(self):
        self.__dict__.update(TOOLS)

