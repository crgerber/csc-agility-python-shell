from core.agility.v3_3.agilitymodel.base.Package import PackageBase
from core.agility.v3_3.agilitymodel.actions.Package import PackageActions

class Package(PackageBase, PackageActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=[], startup=[], shutdown=[], metavariable=[], variable=[], dependency=[], install=[], operational=[], reconfigure=[]):
        '''
        Constructor
        @param operatingsystem: operatingsystem minOccurs=0 maxOccurs=unbounded
        @type operatingsystem: string
        @param startup: startup minOccurs=0 maxOccurs=unbounded
        @type startup: Link
        @param shutdown: shutdown minOccurs=0 maxOccurs=unbounded
        @type shutdown: Link
        @param metavariable: metavariable minOccurs=0 maxOccurs=unbounded
        @type metavariable: ScriptPropertyReference
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: PropertyDefinition
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param install: install minOccurs=0 maxOccurs=unbounded
        @type install: Link
        @param operational: operational minOccurs=0 maxOccurs=unbounded
        @type operational: Link
        @param reconfigure: reconfigure minOccurs=0 maxOccurs=unbounded
        @type reconfigure: Link
        '''
        PackageBase.__init__(self, operatingsystem=operatingsystem, startup=startup, shutdown=shutdown, metavariable=metavariable, variable=variable, dependency=dependency, install=install, operational=operational, reconfigure=reconfigure)
