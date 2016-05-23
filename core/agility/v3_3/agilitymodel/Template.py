from core.agility.v3_3.agilitymodel.base.Template import TemplateBase
from core.agility.v3_3.agilitymodel.actions.Template import TemplateActions

class Template(TemplateBase, TemplateActions):
    '''
    classdocs
    '''
    def __init__(self, topology=None, accessuri=None, hostnameprefix=None, onboarded=None, location=None, configurationresources=[], destconnections=[], model=None, accesslists=[], releasedisks=None, factory=None, cloud=None, variables=[], resources=[], numinstances=None, credential=None, environment=None, servicebindings=[], srcconnections=[], packages=[], stack=None, project=None, instances=[], stats=None, volumes=[], image=None):
        '''
        Constructor
        @param topology: topology minOccurs=0
        @type topology: Link
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param hostnameprefix: hostnameprefix minOccurs=0
        @type hostnameprefix: string
        @param onboarded: onboarded minOccurs=0
        @type onboarded: boolean
        @param location: location minOccurs=0
        @type location: string
        @param configurationresources: configurationresources minOccurs=0 maxOccurs=unbounded
        @type configurationresources: Link
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param model: model minOccurs=0
        @type model: string
        @param accesslists: accesslists minOccurs=0 maxOccurs=unbounded
        @type accesslists: Link
        @param releasedisks: releasedisks minOccurs=0
        @type releasedisks: boolean
        @param factory: factory minOccurs=0
        @type factory: boolean
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: Resource
        @param numinstances: numinstances
        @type numinstances: int
        @param credential: credential minOccurs=0
        @type credential: Credential
        @param environment: environment minOccurs=0
        @type environment: Link
        @param servicebindings: servicebindings minOccurs=0 maxOccurs=unbounded
        @type servicebindings: Link
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param stack: stack minOccurs=0
        @type stack: Link
        @param project: project minOccurs=0
        @type project: Link
        @param instances: instances minOccurs=0 maxOccurs=unbounded
        @type instances: Link
        @param stats: stats minOccurs=0
        @type stats: TemplateStats
        @param volumes: volumes minOccurs=0 maxOccurs=unbounded
        @type volumes: Link
        @param image: image minOccurs=0
        @type image: Link
        '''
        TemplateBase.__init__(self, topology=topology, accessuri=accessuri, hostnameprefix=hostnameprefix, onboarded=onboarded, location=location, configurationresources=configurationresources, destconnections=destconnections, model=model, accesslists=accesslists, releasedisks=releasedisks, factory=factory, cloud=cloud, variables=variables, resources=resources, numinstances=numinstances, credential=credential, environment=environment, servicebindings=servicebindings, srcconnections=srcconnections, packages=packages, stack=stack, project=project, instances=instances, stats=stats, volumes=volumes, image=image)
