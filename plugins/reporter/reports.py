'''
Created on Nov 19, 2012

@author: dawood
'''
__all__ = ['getAssetList', 'generateAssetReport', '_createAssetReport', 'diffReport', 'customReport', 'diff']
from agilityshell import agility
from core.proxy.hook import Hook
from reporting.reporter import getAssetList, generateAssetReport
from reporting.reporter import _createAssetReport as internal_createAssetReport
from reporting.diff import COMPARE_MODE, assertEqual, compare,\
    compareMapValues, compareComposites
from queries.exportcsv import exportSearchResultsCSV, exportCSV
from core.pyworx.partialfunc import partially


from reporting.diff import diffReport

from queries.exportcsv import customReport

#partial invocation to expose a friendly method to the shell
_createAssetReport = partially(internal_createAssetReport, agility.cfg.conn.conn_params)

#meta grouping of features
diff = Hook(**{'COMPARE_MODE' : COMPARE_MODE,
                          'assertEqual' : assertEqual,
                          'compare' : compare,
                          'compareMapValues' : compareMapValues,
                          'compareHierarchicalMaps' : compareComposites})

#inject some utility methods to the agility instance
agility._addServiceMethod(exportSearchResultsCSV)
agility._addServiceMethod(exportCSV)




