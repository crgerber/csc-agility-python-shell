from core.agility.v3_3.agilitymodel.base.Package import PackageBase
from core.agility.v3_3.agilitymodel.actions.Package import PackageActions

class Package(PackageBase, PackageActions):
    '''
    classdocs
    '''
    def __init__(self, shutdown=[], metavariable=[], startup=[], operational=[], dependency=[], install=[], reconfigure=[], variable=[], operatingsystem=[]):
        '''
        Constructor
        @param shutdown: shutdown minOccurs=0 maxOccurs=unbounded
        @type shutdown: Link
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
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
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        '''
        PackageBase.__init__(self, shutdown=shutdown, metavariable=metavariable, startup=startup, operational=operational, dependency=dependency, install=install, reconfigure=reconfigure, variable=variable, operatingsystem=operatingsystem)
