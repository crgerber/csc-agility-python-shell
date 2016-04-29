from core.agility.v3_3.agilitymodel.base.Model import ModelBase
from core.agility.v3_3.agilitymodel.actions.Model import ModelActions

class Model(ModelBase, ModelActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], price=None, buildmodel=None, resources=[], cloud=None, modelid=None, architecture=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param price: price minOccurs=0
        @type price: double
        @param buildmodel: buildmodel minOccurs=0
        @type buildmodel: boolean
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param modelid: modelid minOccurs=0
        @type modelid: string
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        '''
        ModelBase.__init__(self, properties=properties, price=price, buildmodel=buildmodel, resources=resources, cloud=cloud, modelid=modelid, architecture=architecture)
