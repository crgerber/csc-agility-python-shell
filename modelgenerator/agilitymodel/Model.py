from base.Model import ModelBase
from actions.Model import ModelActions

class Model(ModelBase, ModelActions):
    '''
    classdocs
    '''
    def __init__(self, price=None, architecture=None, resources=list(), buildModel=None):
        '''
        Constructor
        @param price: price minOccurs=0
        @type price: double
        @param architecture: architecture minOccurs=0
        @type architecture: Architecture
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param buildModel: buildModel minOccurs=0
        @type buildModel: boolean
        '''
        ModelBase.__init__(self, price=price, architecture=architecture, resources=resources, buildModel=buildModel)
