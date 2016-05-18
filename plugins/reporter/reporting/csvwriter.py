'''
Created on Nov 1, 2012

@author: dawood
'''
from agilityshell import agility
import os
import csv
import logging
import reporting
COMPONENT_NAME = reporting.LOGGER_NAME
import logger
logger = logger.getLogger(COMPONENT_NAME)

def writeCSVFile(rows, reportFileName, reportDir='reports', fields=None, delimiter="|"):
    reportFilePath = os.path.join(reportDir, reportFileName)
    if not os.path.exists(reportDir):
        os.makedirs(reportDir)
    csv.register_dialect('excel', delimiter=delimiter)
    colNamesSet = set()
    if not fields:
        [colNamesSet.add(key) for row in rows for key in agility.tools.scripting.listFields(row)]
    cols = fields or colNamesSet
    
    logger.info("cols:=%s"%cols) 
    
    with open(reportFilePath, 'w') as reportFile:
        reportWriter = csv.DictWriter(reportFile, cols, dialect='excel', extrasaction='ignore')
        reportWriter.writeheader()
        reportWriter.writerows(rows)
        logger.info('Report %s created successfully', reportFilePath)