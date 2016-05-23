from core.agility.v3_3.agilitymodel.base.Repository import RepositoryBase
from core.agility.v3_3.agilitymodel.actions.Repository import RepositoryActions

class Repository(RepositoryBase, RepositoryActions):
    '''
    classdocs
    '''
    def __init__(self, size=None, cloud=None, properties=[], repositorytype=None, path=None, usage=[], locations=[]):
        '''
        Constructor
        @param size: size minOccurs=0
        @type size: long
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param repositorytype: repositorytype minOccurs=0
        @type repositorytype: string
        @param path: path minOccurs=0
        @type path: string
        @param usage: usage minOccurs=0 maxOccurs=unbounded
        @type usage: RepositoryUsage
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: string
        '''
        RepositoryBase.__init__(self, size=size, cloud=cloud, properties=properties, repositorytype=repositorytype, path=path, usage=usage, locations=locations)
