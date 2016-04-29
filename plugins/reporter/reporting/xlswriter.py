'''
Created on Nov 26, 2012

@author: dawood
'''
from tempfile import TemporaryFile
from xlwt import Workbook
from agilityshell import agility
import os
import reporting
COMPONENT_NAME = reporting.LOGGER_NAME
import logger
logger = logger.getLogger(COMPONENT_NAME)

selectFields = agility.tools.scripting.selectFields
listFields = agility.tools.scripting.listFields

class ExcelReport(object):
    def __init__(self, reportFileName, reportDir='reports'):
        self.reportDir = reportDir
        self.reportFileName = reportFileName
        self.workbook = None
        self.worksheets = {}

    def writeWorkSheet(self, data, fields, worksheetName):
        if not self.workbook:
            self.workbook = newWorkBook(data, fields, worksheetName)
        else:
            self.worksheets[worksheetName] = newWorkSheet(self.workbook, data, fields, worksheetName)
            
    def save(self):
        if not self.workbook:
            raise RuntimeError('save() called on an empty report')
        reportFilePath = '%s.xls'%os.path.join(self.reportDir, self.reportFileName)
        logger.info('Report %s created successfully', reportFilePath)
        self.workbook.save(reportFilePath)
        
def newWorkBook(data, fields=None, worksheetName='Sheet 1'):
    workbook = Workbook()
    worksheet = newWorkSheet(workbook, data, fields, worksheetName)
    return workbook

def newWorkSheet(workbook, data, fields=None, worksheetName='Sheet 1'):
    worksheet = workbook.add_sheet(worksheetName)
    return writeData(worksheet, data, fields)
    
def writeData(worksheet, data, fields=None):
    default = ''
    colNamesSet = set()
    if not fields:
        [colNamesSet.add(key) for row in data for key in listFields(row)]
    fields = fields or sorted(colNamesSet)
    data = [selectFields(item, fields=fields, ignore=False, default=default) for item in data]
    data.insert(0, dict(list(zip(fields, fields))))#column names
    for r, row in enumerate(data):
        for c, col in enumerate(fields):
            worksheet.write(r, c, label=row.get(col, default))
    return worksheet