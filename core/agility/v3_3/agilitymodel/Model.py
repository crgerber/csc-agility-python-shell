from core.agility.v3_3.agilitymodel.base.Model import ModelBase
from core.agility.v3_3.agilitymodel.actions.Model import ModelActions

class Model(ModelBase, ModelActions):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, properties=[], buildmodel=None, price=None, resources=[], modelid=None, architecture=None):
        '''
        Constructor
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param buildmodel: buildmodel minOccurs=0
        @type buildmodel: boolean
        @param price: price minOccurs=0
        @type price: double
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param modelid: modelid minOccurs=0
        @type modelid: string
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        '''
        ModelBase.__init__(self, cloud=cloud, properties=properties, buildmodel=buildmodel, price=price, resources=resources, modelid=modelid, architecture=architecture)
