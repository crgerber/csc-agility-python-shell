from .base.Location import LocationBase
from .actions.Location import LocationActions

class Location(LocationBase, LocationActions):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], properties=[], visible=None, hosts=[], cloud=None, storageroot=None, networks=[], sublocations=[]):
        '''
        Constructor
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param visible: visible minOccurs=0
        @type visible: boolean
        @param hosts: hosts minOccurs=0 maxOccurs=unbounded
        @type hosts: Host
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param storageroot: storageroot minOccurs=0
        @type storageroot: boolean
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param sublocations: sublocations minOccurs=0 maxOccurs=unbounded
        @type sublocations: Link
        '''
        LocationBase.__init__(self, repositories=repositories, properties=properties, visible=visible, hosts=hosts, cloud=cloud, storageroot=storageroot, networks=networks, sublocations=sublocations)
