from core.agility.v3_3.agilitymodel.base.DesignContainer import DesignContainerBase

class BlueprintBase(DesignContainerBase):
    '''
    classdocs
    '''
    def __init__(self, topology=[], errorlevel=None, connection=[]):
        DesignContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'topology': {'name': 'topology', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'errorLevel': {'name': 'errorlevel', 'native': False, 'type': 'ErrorLevel'}, 'connection': {'name': 'connection', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'DesignConnection'}})
        self.topology = topology
        self.errorlevel = errorlevel
        self.connection = connection 
