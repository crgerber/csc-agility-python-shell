from base.ValueProvider import ValueProviderBase
from actions.ValueProvider import ValueProviderActions

class ValueProvider(ValueProviderBase, ValueProviderActions):
    '''
    classdocs
    '''
    def __init__(self, classname=None, displayname=None):
        '''
        Constructor
        @param classname: classname minOccurs=0
        @type classname: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        '''
        ValueProviderBase.__init__(self, classname=classname, displayname=displayname)
