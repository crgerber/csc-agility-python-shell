'''
Created on Nov 1, 2012

@author: dawood
'''
from agilityshell import agility
import logging
import os
import reporter

from queries.exportcsv import customReport
from core.base.enum import Enum
from xlswriter import ExcelReport

from reporting import LOGGER_NAME
COMPONENT_NAME = LOGGER_NAME
import logger
logger = logger.getLogger('%s.%s'%(COMPONENT_NAME, __name__))

COMPARE_MODE = Enum(**{'EXACT': 'master_equal_slave',
                     'MASTER_INTACT': 'master_subset_slave',
                     'SLAVE_INTACT': 'slave_subset_master'})

DIFF_REPORT_INCLUDE = Enum(**{'ALL' : 'delete_insert_replace',
                        'DELETED' : 'delete',
                        'ADDED' : 'insert',
                        'MODIFIED' : 'replace',
                        'EQUAL' : 'equal'})

COMPARE_OPCODES = Enum(**{'EQUAL' : 'equal',
                          'REPLACE' : 'replace',
                          'DELETE' : 'delete',
                          'INSERT' : 'insert'})

idmap = agility.tools.scripting.idmap
selectFields = agility.tools.scripting.selectFields
listFields = agility.tools.scripting.listFields
flattenmap = agility.tools.scripting.flattenmap
setField = agility.tools.scripting.setField
getField = agility.tools.scripting.getField

def assertEqual(master, slave, fields, mode=COMPARE_MODE.EXACT):
    diffmaster, diffslave, diffcommon, _ = compare(master, slave, fields, detailed=True)
    result = False
    if mode == COMPARE_MODE.EXACT:
        if not any((diffmaster, diffslave, diffcommon)):#no deleted items, no added items, common fields are equal
            result = True
    elif mode == COMPARE_MODE.MASTER_INTACT:
        if not(any(diffmaster, diffcommon)):#no deleted items, common fields are equal, i.e. master is contained within slave
            result = True
    elif mode == COMPARE_MODE.SLAVE_INTACT:
        if not any((diffslave, diffcommon)):#no added items, common fields are equal, i.e. slave is contained within master
            result = True
    return result

assertEqual.MODE = COMPARE_MODE#expose the enum to the outside world as an attribute of the compare function

def compare(master, slave, fields=None, detailed=True, flatten=False):
    '''
    compares two result sets
    
    @param master: master result set, serves as 'expected' result
    @type master: list of <Asset>, or id-map
    @param slave: slave result set, serves as 'actual' result
    @type slave: list of <Asset>, or id-map
    @param fields: list of attributes to take into account when comparing two object with the same id. if flatten, field names can be fully qualified names e.g.: "a.b.c" 
    @param detailed: True will return detailed objects in the result sets, False will only return the keys, i.e. id's
    @param flatten: True will convert the object tree into a map, with attribute names formatted into: <parent>.<attribute>.<childattribute>.<grandchildattribute> facilitating deep comparison
    '''
    master = idmap(master) if isinstance(master, (list, tuple)) else master
    slave = idmap(slave) if isinstance(slave, (list, tuple)) else slave
    
    
    diffmaster, diffslave, diffcommon, unchanged = _compareidmaps(master, slave, fields, detailed, flatten=flatten)
    
    return diffmaster, diffslave, diffcommon, unchanged

def diffReport(master, slave, fields, reportFileName, reportDir=None, include=(DIFF_REPORT_INCLUDE.DELETED, DIFF_REPORT_INCLUDE.ADDED, DIFF_REPORT_INCLUDE.MODIFIED), hierarchical=False, format='xls'):
    '''
    creates diff reports, for deleted, added, modified and unchanged entries selectively based on the include argument
    
    @param master: master result set, serves as 'expected' result
    @type master: list of <Asset>, or id-map
    @param slave: slave result set, serves as 'actual' result
    @type slave: list of <Asset>, or id-map
    @param fields: list of attributes to take into account when comparing two object with the same id. if flatten, field names can be fully qualified names e.g.: "a.b.c"
    @param reportDir: parent directory for reports, a sub dir with the name "diff" will be created to host the report files, defaults to 'reports/diff' 
    @param reportFileName: file name without extension, report files will have ".csv" extension. name will be prefixed with diff-opcodes: [delete, insert, replace, equal] for deleted, added, modified and intact reports respectively
    @param hierarchical: True will convert the object tree into a map, with attribute names formatted into: <parent>.<attribute>.<childattribute>.<grandchildattribute> facilitating deep comparison
    '''
    reportDir= reportDir or 'reports'
    writeReport = customReport
    xlsReoprt = None
    if format == 'xls':
        xlsReoprt = ExcelReport(reportFileName, reportDir)
        #proxy the call to customReport into the workbook object
        writeReport = lambda data, reportFileName, reportDir='reports', fields=None, ignore=False, default='', delimiter='|', ext='': xlsReoprt.writeWorkSheet(data, fields, reportFileName)
        
        
    reportDir = reportDir or os.path.join('reports', 'diff')
    if DIFF_REPORT_INCLUDE.ALL in include:
        include = (DIFF_REPORT_INCLUDE.DELETED, DIFF_REPORT_INCLUDE.ADDED, DIFF_REPORT_INCLUDE.MODIFIED, DIFF_REPORT_INCLUDE.EQUAL)
        
    diffmaster, diffslave, diffcommon, unchanged = compare(master, slave, fields, detailed=True, flatten=hierarchical)
    if DIFF_REPORT_INCLUDE.DELETED in include:
        diffmasterdata = [selectFields(v, fields, ignore=False, default='') for v in diffmaster.values()]
        subReportFileName = '%s_%s'%(DIFF_REPORT_INCLUDE.DELETED , reportFileName)
        writeReport(diffmasterdata, subReportFileName, reportDir=reportDir, fields=fields, ignore=False, default='', delimiter='|', ext='csv')
    if DIFF_REPORT_INCLUDE.ADDED in include:
        diffslavedata = [selectFields(v, fields, ignore=False, default='') for v in diffslave.values()]
        subReportFileName = '%s_%s'%(DIFF_REPORT_INCLUDE.ADDED , reportFileName)
        writeReport(diffslavedata, subReportFileName, reportDir=reportDir, fields=fields, ignore=False, default='', delimiter='|', ext='csv')
    if DIFF_REPORT_INCLUDE.MODIFIED in include:
        if not hierarchical:
            diffcommondata = [selectFields(v, fields, ignore=False, default='') for v in diffcommon['details'].values()]
            subReportFileName = '%s_%s'%(DIFF_REPORT_INCLUDE.MODIFIED , reportFileName)
            writeReport(diffcommondata, subReportFileName, reportDir=reportDir, fields=fields, ignore=False, default='', delimiter='|', ext='csv')
        else:
            #CSV file per Asset, can be potentially loaded as Tabs in an Excel workbook
            for id, item in diffcommon['details'].items():
                data = selectFields(item, fields, ignore=False, default='', match=selectFields.MATCH.PREFIX)
                cols = data.keys()
                #customReport expects data as a sequence of maps
                subReportFileName = '%s_%s_%s_hierarchical'%(DIFF_REPORT_INCLUDE.MODIFIED , reportFileName, id)
                writeReport([data], subReportFileName, reportDir=reportDir, fields=cols, ignore=False, default='', delimiter='|', ext='csv')
    if DIFF_REPORT_INCLUDE.EQUAL in include:
        unchangeddata = [selectFields(v, fields, ignore=False, default='') for v in unchanged.values()]
        subReportFileName = '%s_%s'%(DIFF_REPORT_INCLUDE.EQUAL , reportFileName)
        writeReport(unchangeddata, subReportFileName, reportDir=reportDir, fields=fields, ignore=False, default='', delimiter='|', ext='csv')
        
    if xlsReoprt:
        xlsReoprt.save()
    
        
diffReport.INCLUDE = DIFF_REPORT_INCLUDE

def _compareidmaps(master, slave, fields, detailed=True, flatten=False, assertCommonFields=False):
    if not all((master, slave, fields)):
        raise ValueError('must provide value for arguments (master -> idmap, slave -> idmap, fields -> list of field names')
    
    compareCompositeStrategy = compareMapValues if assertCommonFields else aggregatedCompareComposites
    masterKeys = set(listFields(master))
    slaveKeys = set(listFields(slave))
    diffmaster = {}
    diffslave = {}
    diffcommonFields = {}
    diffcommon = {'details' : None,
                  'summary' : None}
    unchanged = {}
    
    diffmasterKeys = masterKeys - slaveKeys #deleted keys
    diffslaveKeys = slaveKeys - masterKeys #added
    commonKeys = masterKeys & slaveKeys #same or modified, checking later

    commonMaster = selectFields(master, commonKeys)#common keys, master details
    commonSlave = selectFields(slave, commonKeys)#common keys, slave details
    
    for key in commonKeys:
        commonMasterItem = commonMaster[key] if not flatten else flattenmap(commonMaster[key])
        commonSlaveItem = commonSlave[key] if not flatten else flattenmap(commonSlave[key])
        #Note, the result of flatten is a map, never an object, so the fields names can contain "." in the fully qualified attribute name with no issues
        diffMap = compareCompositeStrategy(selectFields(commonMasterItem, fields, ignore=False, default='', match=selectFields.MATCH.PREFIX), selectFields(commonSlaveItem, fields, ignore=False, default=''))
        if diffMap:
            diffcommonFields[key] = diffMap
    
    diffcommonKeys = diffcommonFields.keys()
    unchangedKeys = commonKeys - set(diffcommonKeys)
    diffcommon['summary'] = diffcommonFields
    if detailed:
        diffmaster = selectFields(master, diffmasterKeys)#deleted details
        diffslave = selectFields(slave, diffslaveKeys)#added details
        unchanged = selectFields(master, unchangedKeys)#unchanged details
        
        diffcommonDetails = {}
        changeTemplate = 'was: [%s] -> now: [%s]'
        for key in diffcommonKeys:
            commonMasterItem = commonMaster[key] if not flatten else flattenmap(commonMaster[key])#template
            changeTemplateItem = selectFields(commonMasterItem, fields, ignore=False, default='', match=selectFields.MATCH.PREFIX)#select only desired fields
            for field in diffcommonFields[key].keys():
                setField(changeTemplateItem, field, changeTemplate%(diffcommonFields[key][field]))#overwrite with <field> = 'was <> now <>' for the changed fields
            diffcommonDetails[key] = changeTemplateItem
        
        diffcommon['details'] = diffcommonDetails#human readable, report friendly modification details
    
    if not detailed:
        return diffmasterKeys, diffslaveKeys, diffcommonKeys, unchangedKeys
    
    return diffmaster, diffslave, diffcommon, unchanged#deleted, added, modified, unchanged

def aggregatedCompareComposites(master, slave, prettify=False):
    '''
    wrapper or compareComposite, shaping results into a map of {<fieldsName> : (valueBefore, valueAfter)}
    
    @return: map of {<fieldsName> : (<valueBefore>, <valueAfter>)}
    '''
    diffMap = {}
    deleted, added, modified, unchanged = compareComposites(master, slave, prettify)
    [diffMap.update([(deletedFieldKey, (getField(master, deletedFieldKey), 'N/A'))]) for deletedFieldKey in deleted]
    [diffMap.update([(addedFieldKey, ('N/A', getField(slave, addedFieldKey)))]) for addedFieldKey in added]
    [diffMap.update([(modifiedFieldKey, modified[modifiedFieldKey])]) for modifiedFieldKey in modified]
    
    return diffMap
    

def compareComposites(master, slave, prettify=True):
    '''
    compares two objects or maps, reporting the deleted, added, modified values within <fields> range, and unchanged fields
    
    @return: diffmaster, diffslave, diffcommonFields, unchanged, which is deleted fields, added fields, modified common fields, and unchanged fields respectively
    '''
    master = flattenmap(master)
    slave = flattenmap(slave)
    masterKeys = set(listFields(master))
    slaveKeys = set(listFields(slave))
    diffmaster = {}
    diffslave = {}
    diffcommonFields = {}
    diffcommon = {}
    unchanged = {}
    changeTemplate = 'was: [%s] -> now: [%s]'
    diffmasterKeys = masterKeys - slaveKeys #deleted keys
    diffslaveKeys = slaveKeys - masterKeys #added
    commonKeys = masterKeys & slaveKeys #same or modified, checking later

    commonMaster = selectFields(master, commonKeys)#common keys, master details
    commonSlave = selectFields(slave, commonKeys)#common keys, slave details
    
    for key in commonKeys:
        masterfield = commonMaster[key]
        slavefield = commonSlave[key]
        if masterfield != slavefield:
            diffcommonFields[key] = (masterfield, slavefield) if not prettify else changeTemplate%(masterfield, slavefield)
    
    diffcommonKeys = diffcommonFields.keys()
    unchangedKeys = commonKeys - set(diffcommonKeys)
    diffmaster = selectFields(master, diffmasterKeys)#deleted details
    diffslave = selectFields(slave, diffslaveKeys)#added details
    unchanged = selectFields(master, unchangedKeys)#unchanged details
    
    return diffmaster, diffslave, diffcommonFields, unchanged#deleted, added, modified, unchanged
    
def compareMapValues(master, slave):
    '''
    compare two map values, assuming key sets are equal. Report the diff in the format: <key> : (<master value>, <modified slave value>)
    '''
    diffMap = {}
    if master.keys() != slave.keys():
        raise ValueError('mismatched key sets, possible wrong use of function')
    for masterPair, slavePair in zip(sorted(master.items(), key=lambda pair: pair[0]), sorted(slave.items(), key=lambda pair: pair[0])):
        if masterPair[1] != slavePair[1]: diffMap[masterPair[0]] = (masterPair[1], slavePair[1])#diffMap<key> = (original value, modified value)
    
    return diffMap


