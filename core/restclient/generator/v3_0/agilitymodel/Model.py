from base.Model import ModelBase
from actions.Model import ModelActions

class Model(ModelBase, ModelActions):
    '''
    classdocs
    '''
    def __init__(self, buildmodel=None, price=None, resources=[], architecture=None, properties=[], cloud=None, modelid=None):
        '''
        Constructor
        @param buildmodel: buildmodel minOccurs=0
        @type buildmodel: boolean
        @param price: price minOccurs=0
        @type price: double
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param modelid: modelid minOccurs=0
        @type modelid: string
        '''
        ModelBase.__init__(self, buildmodel=buildmodel, price=price, resources=resources, architecture=architecture, properties=properties, cloud=cloud, modelid=modelid)
