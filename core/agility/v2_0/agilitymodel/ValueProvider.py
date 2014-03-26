from core.agility.v2_0.agilitymodel.base.ValueProvider import ValueProviderBase
from core.agility.v2_0.agilitymodel.actions.ValueProvider import ValueProviderActions

class ValueProvider(ValueProviderBase, ValueProviderActions):
    '''
    classdocs
    '''
    def __init__(self, classname=None, displayName=None):
        '''
        Constructor
        @param classname: classname minOccurs=0
        @type classname: string
        @param displayName: displayName minOccurs=0
        @type displayName: string
        '''
        ValueProviderBase.__init__(self, classname=classname, displayName=displayName)
