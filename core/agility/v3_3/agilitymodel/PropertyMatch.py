from core.agility.v3_3.agilitymodel.base.PropertyMatch import PropertyMatchBase
from core.agility.v3_3.agilitymodel.actions.PropertyMatch import PropertyMatchActions

class PropertyMatch(PropertyMatchBase, PropertyMatchActions):
    '''
    classdocs
    '''
    def __init__(self, name='', value='', matches=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param value: value
        @type value: string
        @param matches: matches
        @type matches: string
        '''
        PropertyMatchBase.__init__(self, name=name, value=value, matches=matches)
