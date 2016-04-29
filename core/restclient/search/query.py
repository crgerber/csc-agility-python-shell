'''
Created on Oct 29, 2012

@author: dawood
'''
from core.base.enum import Enum
class AgilityQuery(object):
    '''
    Query object, serializes itself into a lucene friendly query string
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        self.ENUM = Enum()
        self.template = Enum()
        self.params = Enum()
        self.template.fields = 'fields=%(fields)s'
        self.params.fields = []#join on comma
        self.template.offset = 'offset=%(offset)s'
        self.params.offset = 0 #pagination offset
        self.template.limit = 'limit=%(limit)s'
        self.params.limit=20 #pagination limit, max per page
        
        self.template.fieldName_searchTerm = 'qterm.field.%(fieldName)s=%(searchTerm)s'
        self.params.fieldName = ''
        self.params.searchTerm = ''
        self.template.fieldName_groupByValues = 'filter.group.%(fieldName)s=%(groupByValues)s'
        self.params.groupByValues = []#join on comma
#        self.getGroupByValues = lambda: ','.join(self._groupByValues)
        self.ENUM.ORDER_BY = Enum(**{'asc' : 'ASC', 'desc' : 'DESC'})
        self.template.fieldName_order = 'orderBy=%(fieldName)s %(order)s'
        self.params.order = self.ENUM.ORDER_BY.asc
        self.template.containerId = 'containerId=%(containerId)s'
        self.params.containerId = ''
        self.ENUM.VERSION_OPTIONS = Enum(**{'in_progress' : 'VERSION_INPROGRESS_OPT',
                                'head' : 'VERSION_HEAD_OPT',
                                'in_progress_head' : 'VERSION_INPROGRESS_HEAD_OPT',
                                'all' : 'VERSION_ALL_OPT',
                                'na': 'VERSION_NA_OPT'})
        
        self.template.version = 'versionOpt=%(version)s'
        self.params.version = self.ENUM.VERSION_OPTIONS.all
        self.template.deleted = 'deleteOpt=%(deleted)s'
        self.params.deleted = 'DELETED_FALSE_OPT'
        self.ENUM.USAGE_PERMISSION = Enum(**{'use' : 'use', 'view' : 'view'})
        self.template.usage = 'usage=%(usage)s'
        self.params.usage = self.ENUM.USAGE_PERMISSION.use
        
        self.params.__dict__.update(kwargs)
        
    def compile(self):
        return self._compileTemplates()
    
    def clearDefaults(self, fields=None):
        if fields is None:
            fields = ['usage', 'limit', 'order', 'version', 'deleted']
        [setattr(self.params, field, '') for field in fields] 
    
    def _compileTemplates(self):
        templateQueries = []
        for templateName, templateStr in list(self.template.__dict__.items()):
            templateParams = {}
            fieldNames = templateName.split('_')
            for fieldName in fieldNames:
                fieldValue = getattr(self.params, fieldName, '')
                if not fieldValue: break
                
                if isinstance(fieldValue, bool):
                    if fieldValue: fieldValue = "true"
                    else: fieldValue = "false"
                elif isinstance(fieldValue, list) or isinstance(fieldValue, tuple):
                    fieldValue = ",".join(fieldValue)
                elif not isinstance(fieldValue, str):
                    fieldValue = str(fieldValue)
                else:
                    fieldValue = fieldValue
                templateParams[fieldName] = fieldValue
            else:
                #template satisfied; no breaks
                subQuery = templateStr%templateParams
                templateQueries.append(subQuery)
        queries = {}
        [queries.update([(templateQuery.split('=')[0], templateQuery.split('=')[1])]) for templateQuery in templateQueries]
        return queries
    
    def __str__(self):
        return str(self._compileTemplates())
    
    __repr__ = __str__