from core.agility.v3_3.agilitymodel.base.Template import TemplateBase
from core.agility.v3_3.agilitymodel.actions.Template import TemplateActions

class Template(TemplateBase, TemplateActions):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, image=None, instances=[], accesslists=[], cloud=None, configurationresources=[], servicebindings=[], stats=None, accessuri=None, factory=None, environment=None, hostnameprefix=None, location=None, variables=[], resources=[], credential=None, srcconnections=[], destconnections=[], packages=[], stack=None, topology=None, releasedisks=None, project=None, volumes=[], model=None, onboarded=None):
        '''
        Constructor
        @param numinstances: numinstances
        @type numinstances: int
        @param image: image minOccurs=0
        @type image: Link
        @param instances: instances minOccurs=0 maxOccurs=unbounded
        @type instances: Link
        @param accesslists: accesslists minOccurs=0 maxOccurs=unbounded
        @type accesslists: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param configurationresources: configurationresources minOccurs=0 maxOccurs=unbounded
        @type configurationresources: Link
        @param servicebindings: servicebindings minOccurs=0 maxOccurs=unbounded
        @type servicebindings: Link
        @param stats: stats minOccurs=0
        @type stats: TemplateStats
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param factory: factory minOccurs=0
        @type factory: boolean
        @param environment: environment minOccurs=0
        @type environment: Link
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param location: location minOccurs=0
        @type location: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param topology: topology minOccurs=0
        @type topology: Link
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param project: project minOccurs=0
        @type project: Link
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Link
        @param model: model minOccurs=0
        @type model: string
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        '''
        TemplateBase.__init__(self, numinstances=numinstances, image=image, instances=instances, accesslists=accesslists, cloud=cloud, configurationresources=configurationresources, servicebindings=servicebindings, stats=stats, accessuri=accessuri, factory=factory, environment=environment, hostnameprefix=hostnameprefix, location=location, variables=variables, resources=resources, credential=credential, srcconnections=srcconnections, destconnections=destconnections, packages=packages, stack=stack, topology=topology, releasedisks=releasedisks, project=project, volumes=volumes, model=model, onboarded=onboarded)
