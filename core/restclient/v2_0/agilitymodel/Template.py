from core.restclient.v2_0.agilitymodel.base.Template import TemplateBase
from core.restclient.v2_0.agilitymodel.actions.Template import TemplateActions

class Template(TemplateBase, TemplateActions):
    '''
    classdocs
    '''
    def __init__(self, credential=None, onboarded=None, numInstances=None, volumes=list(), hostnamePrefix=None, image=None, resources=list(), factory=None, srcConnections=list(), instances=list(), accessUri=None, location=None, accessLists=list(), destConnections=list(), variables=list(), model=None, packages=list(), configurationResources=list(), stack=None, cloud=None, topology=None):
        '''
        Constructor
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        @param numInstances: numInstances
        @type numInstances: int
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Link
        @param hostnamePrefix: hostnamePrefix minOccurs=0
        @type hostnamePrefix: string
        @param image: image minOccurs=0
        @type image: Link
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param factory: factory minOccurs=0
        @type factory: boolean
        @param srcConnections: srcConnections minOccurs=0 maxOccurs=unbounded
        @type srcConnections: Link
        @param instances: instances minOccurs=0 maxOccurs=unbounded
        @type instances: Link
        @param accessUri: accessUri minOccurs=0
        @type accessUri: string
        @param location: location minOccurs=0
        @type location: string
        @param accessLists: accessLists minOccurs=0 maxOccurs=unbounded
        @type accessLists: Link
        @param destConnections: destConnections minOccurs=0 maxOccurs=unbounded
        @type destConnections: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param model: model minOccurs=0
        @type model: string
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param configurationResources: configurationResources minOccurs=0 maxOccurs=unbounded
        @type configurationResources: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param topology: topology minOccurs=0
        @type topology: Link
        '''
        TemplateBase.__init__(self, credential=credential, onboarded=onboarded, numInstances=numInstances, volumes=volumes, hostnamePrefix=hostnamePrefix, image=image, resources=resources, factory=factory, srcConnections=srcConnections, instances=instances, accessUri=accessUri, location=location, accessLists=accessLists, destConnections=destConnections, variables=variables, model=model, packages=packages, configurationResources=configurationResources, stack=stack, cloud=cloud, topology=topology)
