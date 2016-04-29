from core.agility.v3_3.agilitymodel.base.Repository import RepositoryBase
from core.agility.v3_3.agilitymodel.actions.Repository import RepositoryActions

class Repository(RepositoryBase, RepositoryActions):
    '''
    classdocs
    '''
    def __init__(self, path=None, size=None, repositorytype=None, properties=[], cloud=None, usage=[], locations=[]):
        '''
        Constructor
        @param path: path minOccurs=0
        @type path: string
        @param size: size minOccurs=0
        @type size: long
        @param repositorytype: repositorytype minOccurs=0
        @type repositorytype: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param usage: usage minOccurs=0 maxOccurs=unbounded
        @type usage: RepositoryUsage
        @param locations: locations minOccurs=0 maxOccurs=unbounded
        @type locations: string
        '''
        RepositoryBase.__init__(self, path=path, size=size, repositorytype=repositorytype, properties=properties, cloud=cloud, usage=usage, locations=locations)
