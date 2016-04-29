from core.agility.v3_3.agilitymodel.base.Template import TemplateBase
from core.agility.v3_3.agilitymodel.actions.Template import TemplateActions

class Template(TemplateBase, TemplateActions):
    '''
    classdocs
    '''
    def __init__(self, instances=[], numinstances=None, stats=None, credential=None, volumes=[], project=None, accessuri=None, servicebindings=[], cloud=None, packages=[], variables=[], location=None, model=None, destconnections=[], releasedisks=None, configurationresources=[], factory=None, accesslists=[], hostnameprefix=None, srcconnections=[], environment=None, onboarded=None, topology=None, stack=None, image=None, resources=[]):
        '''
        Constructor
        @param instances: instances minOccurs=0 maxOccurs=unbounded
        @type instances: Link
        @param numinstances: numinstances
        @type numinstances: int
        @param stats: stats minOccurs=0
        @type stats: TemplateStats
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Link
        @param project: project minOccurs=0
        @type project: Link
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param servicebindings: servicebindings minOccurs=0 maxOccurs=unbounded
        @type servicebindings: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param location: location minOccurs=0
        @type location: string
        @param model: model minOccurs=0
        @type model: string
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param configurationresources: configurationresources minOccurs=0 maxOccurs=unbounded
        @type configurationresources: Link
        @param factory: factory minOccurs=0
        @type factory: boolean
        @param accesslists: accesslists minOccurs=0 maxOccurs=unbounded
        @type accesslists: Link
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param environment: environment minOccurs=0
        @type environment: Link
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        @param topology: topology minOccurs=0
        @type topology: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param image: image minOccurs=0
        @type image: Link
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        '''
        TemplateBase.__init__(self, instances=instances, numinstances=numinstances, stats=stats, credential=credential, volumes=volumes, project=project, accessuri=accessuri, servicebindings=servicebindings, cloud=cloud, packages=packages, variables=variables, location=location, model=model, destconnections=destconnections, releasedisks=releasedisks, configurationresources=configurationresources, factory=factory, accesslists=accesslists, hostnameprefix=hostnameprefix, srcconnections=srcconnections, environment=environment, onboarded=onboarded, topology=topology, stack=stack, image=image, resources=resources)
