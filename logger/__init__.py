import sys
import logging
import os

this = sys.modules[__name__]
logger = None#only a stub to make IDE happy during development
ROOT_LOGGER_NAME = 'agilityshell'#default value, will be overridden during configuration

def configRootLogger(rootloggerName, logpath, logfile, level=logging.INFO, console=True):
    '''
    Configures the logging application-wide by exposing module level symbols to be imported by other modules
    
    Note: it is important to call this method as early in the initialization life cycle
    '''
    logger = logging.getLogger(rootloggerName)
    logger.setLevel(level)
    # create file handler which logs even debug messages
    
    #fh = logging.handlers.TimedRotatingFileHandler(LOG_FILE_NAME, when='D', interval=1, backupCount=5, encoding=None, delay=False, utc=False)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fullpath = os.path.join(logpath, logfile)
    if console:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)        
        logger.addHandler(ch)
    
    if not os.path.isdir(logpath):
        os.makedirs(logpath)
    fh = logging.FileHandler(fullpath)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    #expose some symbols for other modules to import
    this.ROOT_LOGGER_NAME = rootloggerName
    this.LOG_PATH = logpath
    this.LOG_FILE_NAME = '%s.log' % rootloggerName
    this.logger = logger

def getLogger(component, rootloggerName=None):
    rootloggerName = rootloggerName or this.ROOT_LOGGER_NAME
    return logging.getLogger('%s.%s'%(rootloggerName, component))