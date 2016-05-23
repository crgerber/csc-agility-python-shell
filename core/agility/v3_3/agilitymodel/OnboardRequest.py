from core.agility.v3_3.agilitymodel.base.OnboardRequest import OnboardRequestBase
from core.agility.v3_3.agilitymodel.actions.OnboardRequest import OnboardRequestActions

class OnboardRequest(OnboardRequestBase, OnboardRequestActions):
    '''
    classdocs
    '''
    def __init__(self, targetlocation=None, operatingsystem=None, instance=[], networkpolicy=[], packages=[], cloud=None, variables=[], mgmtprotocol=None, mgmtport=None, reboot=None, assetproperties=[], credential=None):
        '''
        Constructor
        @param targetlocation: targetlocation
        @type targetlocation: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Link
        @param networkpolicy: networkpolicy minOccurs=0 maxOccurs=unbounded
        @type networkpolicy: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param reboot: reboot minOccurs=0
        @type reboot: boolean
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param credential: credential
        @type credential: Credential
        '''
        OnboardRequestBase.__init__(self, targetlocation=targetlocation, operatingsystem=operatingsystem, instance=instance, networkpolicy=networkpolicy, packages=packages, cloud=cloud, variables=variables, mgmtprotocol=mgmtprotocol, mgmtport=mgmtport, reboot=reboot, assetproperties=assetproperties, credential=credential)
