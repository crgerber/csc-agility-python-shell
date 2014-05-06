from core.agility.v2_0.agilitymodel.base.Package import PackageBase
from core.agility.v2_0.agilitymodel.actions.Package import PackageActions

class Package(PackageBase, PackageActions):
    '''
    classdocs
    '''
    def __init__(self, shutdown=list(), metaVariable=list(), startup=list(), operational=list(), dependency=list(), install=list(), reconfigure=list(), variable=list(), operatingSystem=list()):
        '''
        Constructor
        @param shutdown: shutdown minOccurs=0 maxOccurs=unbounded
        @type shutdown: Link
        @param metaVariable: metaVariable minOccurs=0 maxOccurs=unbounded
        @type metaVariable: ScriptPropertyReference
        @param startup: startup minOccurs=0 maxOccurs=unbounded
        @type startup: Link
        @param operational: operational minOccurs=0 maxOccurs=unbounded
        @type operational: Link
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param install: install minOccurs=0 maxOccurs=unbounded
        @type install: Link
        @param reconfigure: reconfigure minOccurs=0 maxOccurs=unbounded
        @type reconfigure: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param operatingSystem: operatingSystem minOccurs=0 maxOccurs=unbounded
        @type operatingSystem: string
        '''
        PackageBase.__init__(self, shutdown=shutdown, metaVariable=metaVariable, startup=startup, operational=operational, dependency=dependency, install=install, reconfigure=reconfigure, variable=variable, operatingSystem=operatingSystem)
