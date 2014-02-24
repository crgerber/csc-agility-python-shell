'''
Created on Nov 30, 2012

@author: dawood
'''
from agilityshell import agility
from logger import logger
from core.base.enum import Enum
__all__ = ['assignedResources', 'diffAssignedResources', 'diffAssignedDisks', 'disks', 'nics', 'processors', 'memory']


RESOURCE_TYPES = Enum(**{'ETHERNET_ADAPTER' : 'Ethernet Adapter',
                         'DISK_DRIVE' : 'Disk Drive',
                         'PROCESSOR' : 'Processor', 
                         'MEMORY' : 'Memory'
                         })
#aliases
getField = agility.tools.scripting.getField
selectFields = agility.tools.scripting.selectFields
#building blocks
asList = lambda r: r if isinstance(r, (tuple, list)) else [r]
resourcesOf = lambda compute, resourceType=RESOURCE_TYPES.DISK_DRIVE: [r for r in compute.get('resources', default=[], wrapper=asList) if getField(r, 'resourceType', '') == resourceType]
disks = lambda compute: resourcesOf(compute, RESOURCE_TYPES.DISK_DRIVE)
nics = lambda compute: resourcesOf(compute, RESOURCE_TYPES.ETHERNET_ADAPTER)
processors = lambda compute: resourcesOf(compute, RESOURCE_TYPES.PROCESSOR)
memory = lambda compute: resourcesOf(compute, RESOURCE_TYPES.MEMORY)
    
def assignedResources(computeList, resourceType=RESOURCE_TYPES.DISK_DRIVE, removeEmpty=True):
    '''
    returns a map of compute.id : list of resource entries where resourceType == 'Disk Drive'
    '''
    compute_disks = {}
    [compute_disks.update([(compute.id, resourcesOf(compute, resourceType))]) for compute in computeList]
    if removeEmpty:
        compute_disks = dict(filter(lambda item: item[1], compute_disks.items()))
    return compute_disks

assignedResources.TYPES = RESOURCE_TYPES

def diffAssignedResources(computeMaster, computeSlave, resourceType=RESOURCE_TYPES.DISK_DRIVE, fields=None):
    master_compute_resources = assignedResources(computeMaster, resourceType=resourceType, removeEmpty=True)
    slave_compute_resources = assignedResources(computeSlave, resourceType=resourceType, removeEmpty=True)
    fieldSource = 'super-set' if not fields else ''
    if not fields:
        filedSet = set([])
        [filedSet.add(f) 
         for resourceList in master_compute_resources.values() 
            for r in resourceList 
                for f in selectFields(r) 
                    if r.get('resourceType', None)==resourceType]
        fields = [f for f in filedSet]
    logger.info('Using %s fields: %s', fieldSource, fields)
    new, deleted, modified, unchanged = agility.tools.report.diff.compare(master_compute_resources, slave_compute_resources, fields)
    logger.info('%s Diff results: New [%s], Deleted [%s], Modified [%s], Unchanged [%s]', resourceType, len(new), len(deleted), len(modified['details']), len(unchanged))
    return new, deleted, modified['details'], unchanged

diffAssignedDisks = lambda computeMaster, computeSlave: diffAssignedResources(computeMaster, computeSlave, resourceType=RESOURCE_TYPES.DISK_DRIVE, fields=['assetPath', 'name', 'resourceType', 'top', 'lifecycleVersion', 'units', 'id', 'quantity'])
