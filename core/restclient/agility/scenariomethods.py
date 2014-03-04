'''
Created on Apr 10, 2013

@author: dawood
'''
from core.pyworx import scripting

import logging
COMPONENT_NAME = 'agility-client.scenarios'
from logger import getLogger
logger = getLogger(COMPONENT_NAME)

def cloneTemplate(sourceTemplate, replaceFields=None, parent=None, prefix='Clone%(idx)s of %(name)s'):
    '''
    
    @param sourceTemplate: source template, or self if invoked as a method of a template object
    @param replaceFields: dictionary of name value pairs of fields to replace
    @param parent: target parent, project or environment objects, default to the source template parent
    @param prefix: cloned template naming format, idx is an incremental counter that must not be removed, <name> can be exchanged for any first level attribute of the source template, e.g. id, hostname, ..., etc
    '''
    from agilityshell import agility
    FIELDS_TO_CLEAR = ['assetPath', 'created', 'creator', 'detailedAssetPath', 'id', 'lastModified', 'onboarded', 'uuid']#+ all nested entry IDs
    COMPONENT_FIELDS_TO_DELETE = {
                                  'resources' : ['id', 'uuid'],
                                  'policyAssignment' : ['id', 'uuid'],
                                  'volumes' : ['id', 'uuid']
                                  }
    replaceFields = replaceFields or {}
    sourceTemplate._topLevel = True #if template object comes from search results, it won't be topLevel, since it's a child of Assetlist
    for component, fields in COMPONENT_FIELDS_TO_DELETE.items():
        for idx, res in enumerate(sourceTemplate.get(component, [])):
            for field in fields:
                fieldFQN = '%s.%s.%s'%(component, idx,field)
                try:
                    scripting.popField(sourceTemplate, fieldFQN, nestedById=False)
                except KeyError, ex:
                    logger.warn('Field [%s] does not exist'%fieldFQN)
    
    
    parent = parent or sourceTemplate.parent
    if parent.typeName == 'Project':
        createTemplate = agility.project.createTemplate
        getSiblings = agility.project.getTemplates
    elif parent.typeName == 'Environment':
        createTemplate = agility.environment.createTemplate
        getSiblings = agility.environment.getTemplatesXML
    elif parent.typeName == 'Topology':
        createTemplate = agility.topology.createChildTemplate
        getSiblings = agility.topology.getChildTemplates
    else:
        raise RuntimeError('Unsupported Parent type: %s'%parent.typeName)

    if 'name' not in replaceFields:
        limit = 10000#a ridiculously large upper bound for the loop searching for a unique name for the teamplate
        counter = range(1, limit)
        counter.insert(0, '')
        siblings = getSiblings(parent.id)
        sourceTemplateFields = scripting.selectFields(sourceTemplate)
        newname = ''
        for idx in counter:
            sourceTemplateFields.update([('idx', str(idx))])
            newname = prefix%sourceTemplateFields
            if not any(map(lambda s: s.name == newname, siblings)):
                break
        else:
            raise RuntimeError('Found more than [%s] clones within the parent container'%limit)
        
        replaceFields.update({'name' : newname})
    #else: client code has provided a name for the clone
    
    xml, dct = sourceTemplate.createXMLTemplate(deleteFields=FIELDS_TO_CLEAR, 
                                     replaceFields=replaceFields, returnXMLOnly=False)


    result = createTemplate(parent.id, data=xml)
    return result

def getParentProject(computeInstance, details=False):
    '''
    Walks up the container hierarchy retrieving parents of a compute instance until the parent project is found
    
    @param details: if True, a Project Asset would be returned, else a Project Link is returned
    '''
    from core.restclient.v2_0.agilitymodel.Link import Link
    parentLink = computeInstance.template.load().parent if isinstance(computeInstance.template, Link) else computeInstance.template.parent
    while(parentLink.typeName != 'Project'):
        parent = parentLink.load()
        parentLink = parent.parent
    return parentLink.load() if details else parentLink
