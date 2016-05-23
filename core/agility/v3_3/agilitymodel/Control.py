from core.agility.v3_3.agilitymodel.base.Control import ControlBase
from core.agility.v3_3.agilitymodel.actions.Control import ControlActions

class Control(ControlBase, ControlActions):
    '''
    classdocs
    '''
    def __init__(self, path='', name='', description='', allowedcontexts='', id=None, drilldowncontext=None, type='', properties=[]):
        '''
        Constructor
        @param path: path
        @type path: string
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param allowedcontexts: allowedcontexts
        @type allowedcontexts: string
        @param id: id
        @type id: int
        @param drilldowncontext: drilldowncontext minOccurs=0
        @type drilldowncontext: PageContext
        @param type: type
        @type type: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        '''
        ControlBase.__init__(self, path=path, name=name, description=description, allowedcontexts=allowedcontexts, id=id, drilldowncontext=drilldowncontext, type=type, properties=properties)
