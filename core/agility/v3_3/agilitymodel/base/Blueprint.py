from core.agility.v3_3.agilitymodel.base.DesignContainer import DesignContainerBase

class BlueprintBase(DesignContainerBase):
    '''
    classdocs
    '''
    def __init__(self, errorlevel=None, topology=[], connection=[]):
        DesignContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'errorLevel': {'native': False, 'name': 'errorlevel', 'type': 'ErrorLevel'}, 'topology': {'maxOccurs': 'unbounded', 'native': False, 'name': 'topology', 'minOccurs': '0', 'type': 'Link'}, 'connection': {'maxOccurs': 'unbounded', 'native': False, 'name': 'connection', 'minOccurs': '0', 'type': 'DesignConnection'}})
        self.errorlevel = errorlevel
        self.topology = topology
        self.connection = connection 
