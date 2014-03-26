from core.agility.v2_0.agilitymodel.base.OnboardRequest import OnboardRequestBase
from core.agility.v2_0.agilitymodel.actions.OnboardRequest import OnboardRequestActions

class OnboardRequest(OnboardRequestBase, OnboardRequestActions):
    '''
    classdocs
    '''
    def __init__(self, credential=None, networkPolicy=list(), assetProperties=list(), variables=list(), reboot=None, instance=list(), targetLocation=None, packages=list(), operatingSystem=None, cloud=None):
        '''
        Constructor
        @param credential: credential
        @type credential: Credential
        @param networkPolicy: networkPolicy minOccurs=0 maxOccurs=unbounded
        @type networkPolicy: Link
        @param assetProperties: assetProperties minOccurs=0 maxOccurs=unbounded
        @type assetProperties: AssetProperty
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param reboot: reboot minOccurs=0
        @type reboot: boolean
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Link
        @param targetLocation: targetLocation
        @type targetLocation: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param operatingSystem: operatingSystem minOccurs=0
        @type operatingSystem: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        OnboardRequestBase.__init__(self, credential=credential, networkPolicy=networkPolicy, assetProperties=assetProperties, variables=variables, reboot=reboot, instance=instance, targetLocation=targetLocation, packages=packages, operatingSystem=operatingSystem, cloud=cloud)
