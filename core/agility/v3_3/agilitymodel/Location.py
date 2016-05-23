from core.agility.v3_3.agilitymodel.base.Location import LocationBase
from core.agility.v3_3.agilitymodel.actions.Location import LocationActions

class Location(LocationBase, LocationActions):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], parentlocation=None, cloud=None, properties=[], sublocations=[], hosts=[], networks=[], storageroot=None, visible=None):
        '''
        Constructor
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Link
        @param parentlocation: parentlocation minOccurs=0
        @type parentlocation: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param sublocations: sublocations minOccurs=0 maxOccurs=unbounded
        @type sublocations: Link
        @param hosts: hosts minOccurs=0 maxOccurs=unbounded
        @type hosts: Host
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param storageroot: storageroot minOccurs=0
        @type storageroot: boolean
        @param visible: visible minOccurs=0
        @type visible: boolean
        '''
        LocationBase.__init__(self, repositories=repositories, parentlocation=parentlocation, cloud=cloud, properties=properties, sublocations=sublocations, hosts=hosts, networks=networks, storageroot=storageroot, visible=visible)
