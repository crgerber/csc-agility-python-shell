from core.agility.v3_3.agilitymodel.base.Location import LocationBase
from core.agility.v3_3.agilitymodel.actions.Location import LocationActions

class Location(LocationBase, LocationActions):
    '''
    classdocs
    '''
    def __init__(self, repositories=[], sublocations=[], parentlocation=None, storageroot=None, networks=[], visible=None, properties=[], cloud=None, hosts=[]):
        '''
        Constructor
        @param repositories: repositories minOccurs=0 maxOccurs=unbounded
        @type repositories: Link
        @param sublocations: sublocations minOccurs=0 maxOccurs=unbounded
        @type sublocations: Link
        @param parentlocation: parentlocation minOccurs=0
        @type parentlocation: Link
        @param storageroot: storageroot minOccurs=0
        @type storageroot: boolean
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param visible: visible minOccurs=0
        @type visible: boolean
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param hosts: hosts minOccurs=0 maxOccurs=unbounded
        @type hosts: Host
        '''
        LocationBase.__init__(self, repositories=repositories, sublocations=sublocations, parentlocation=parentlocation, storageroot=storageroot, networks=networks, visible=visible, properties=properties, cloud=cloud, hosts=hosts)
