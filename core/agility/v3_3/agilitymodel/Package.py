from core.agility.v3_3.agilitymodel.base.Package import PackageBase
from core.agility.v3_3.agilitymodel.actions.Package import PackageActions

class Package(PackageBase, PackageActions):
    '''
    classdocs
    '''
    def __init__(self, startup=[], reconfigure=[], operational=[], dependency=[], shutdown=[], operatingsystem=[], metavariable=[], install=[], variable=[]):
        '''
        Constructor
        @param startup: startup minOccurs=0 maxOccurs=unbounded
        @type startup: Link
        @param reconfigure: reconfigure minOccurs=0 maxOccurs=unbounded
        @type reconfigure: Link
        @param operational: operational minOccurs=0 maxOccurs=unbounded
        @type operational: Link
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param shutdown: shutdown minOccurs=0 maxOccurs=unbounded
        @type shutdown: Link
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
        @param install: install minOccurs=0 maxOccurs=unbounded
        @type install: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        '''
        PackageBase.__init__(self, startup=startup, reconfigure=reconfigure, operational=operational, dependency=dependency, shutdown=shutdown, operatingsystem=operatingsystem, metavariable=metavariable, install=install, variable=variable)
