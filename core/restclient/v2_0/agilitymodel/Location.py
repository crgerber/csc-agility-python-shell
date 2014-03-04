from core.restclient.v2_0.agilitymodel.base.Location import LocationBase
from core.restclient.v2_0.agilitymodel.actions.Location import LocationActions

class Location(LocationBase, LocationActions):
    '''
    classdocs
    '''
    def __init__(self, repositories=list(), properties=list(), visible=None, hosts=list(), cloud=None, storageRoot=None, networks=list(), sublocations=list()):
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
        @param storageRoot: storageRoot minOccurs=0
        @type storageRoot: boolean
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param sublocations: sublocations minOccurs=0 maxOccurs=unbounded
        @type sublocations: Link
        '''
        LocationBase.__init__(self, repositories=repositories, properties=properties, visible=visible, hosts=hosts, cloud=cloud, storageRoot=storageRoot, networks=networks, sublocations=sublocations)
