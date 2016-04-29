from core.agility.v3_3.agilitymodel.base.NameValuePair import NameValuePairBase
from core.agility.v3_3.agilitymodel.actions.NameValuePair import NameValuePairActions

class NameValuePair(NameValuePairBase, NameValuePairActions):
    '''
    classdocs
    '''
    def __init__(self, name='', value=None, id=None):
        '''
        Constructor
        @param name: name
        @type name: string
        @param value: value minOccurs=0
        @type value: string
        @param id: id minOccurs=0
        @type id: int
        '''
        NameValuePairBase.__init__(self, name=name, value=value, id=id)
