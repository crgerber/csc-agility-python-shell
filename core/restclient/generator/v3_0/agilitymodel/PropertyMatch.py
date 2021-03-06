from base.PropertyMatch import PropertyMatchBase
from actions.PropertyMatch import PropertyMatchActions

class PropertyMatch(PropertyMatchBase, PropertyMatchActions):
    '''
    classdocs
    '''
    def __init__(self, matches='', name='', value=''):
        '''
        Constructor
        @param matches: matches
        @type matches: string
        @param name: name
        @type name: string
        @param value: value
        @type value: string
        '''
        PropertyMatchBase.__init__(self, matches=matches, name=name, value=value)
