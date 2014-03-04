from core.restclient.v2_0.agilitymodel.base.DesignContainer import DesignContainerBase

class BlueprintBase(DesignContainerBase):
    '''
    classdocs
    '''
    def __init__(self, connection=list(), errorLevel=None, topology=list()):
        DesignContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'connection': {'maxOccurs': 'unbounded', 'type': 'DesignConnection', 'name': 'connection', 'minOccurs': '0', 'native': False}, 'errorLevel': {'type': 'ErrorLevel', 'name': 'errorLevel', 'native': False}, 'topology': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'topology', 'minOccurs': '0', 'native': False}})
        self.connection = connection
        self.errorLevel = errorLevel
        self.topology = topology 
