from base.Control import ControlBase
from actions.Control import ControlActions

class Control(ControlBase, ControlActions):
    '''
    classdocs
    '''
    def __init__(self, drilldowncontext=None, properties=[], description='', name='', path='', type='', id=None, allowedcontexts=''):
        '''
        Constructor
        @param drilldowncontext: drilldowncontext minOccurs=0
        @type drilldowncontext: PageContext
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param description: description
        @type description: string
        @param name: name
        @type name: string
        @param path: path
        @type path: string
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param allowedcontexts: allowedcontexts
        @type allowedcontexts: string
        '''
        ControlBase.__init__(self, drilldowncontext=drilldowncontext, properties=properties, description=description, name=name, path=path, type=type, id=id, allowedcontexts=allowedcontexts)
