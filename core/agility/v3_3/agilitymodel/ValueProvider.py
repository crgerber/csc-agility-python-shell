from core.agility.v3_3.agilitymodel.base.ValueProvider import ValueProviderBase
from core.agility.v3_3.agilitymodel.actions.ValueProvider import ValueProviderActions

class ValueProvider(ValueProviderBase, ValueProviderActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, classname=None):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param classname: classname minOccurs=0
        @type classname: string
        '''
        ValueProviderBase.__init__(self, displayname=displayname, classname=classname)
