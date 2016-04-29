from core.agility.v3_3.agilitymodel.base.Control import ControlBase
from core.agility.v3_3.agilitymodel.actions.Control import ControlActions

class Control(ControlBase, ControlActions):
    '''
    classdocs
    '''
    def __init__(self, path='', properties=[], description='', allowedcontexts='', drilldowncontext=None, name='', id=None, type=''):
        '''
        Constructor
        @param path: path
        @type path: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param description: description
        @type description: string
        @param allowedcontexts: allowedcontexts
        @type allowedcontexts: string
        @param drilldowncontext: drilldowncontext minOccurs=0
        @type drilldowncontext: PageContext
        @param name: name
        @type name: string
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        ControlBase.__init__(self, path=path, properties=properties, description=description, allowedcontexts=allowedcontexts, drilldowncontext=drilldowncontext, name=name, id=id, type=type)
