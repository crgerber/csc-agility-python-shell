from core.agility.v3_3.agilitymodel.base.OnboardRequest import OnboardRequestBase
from core.agility.v3_3.agilitymodel.actions.OnboardRequest import OnboardRequestActions

class OnboardRequest(OnboardRequestBase, OnboardRequestActions):
    '''
    classdocs
    '''
    def __init__(self, credential=None, networkpolicy=[], assetproperties=[], variables=[], reboot=None, instance=[], mgmtport=None, mgmtprotocol=None, targetlocation=None, packages=[], operatingsystem=None, cloud=None):
        '''
        Constructor
        @param credential: credential
        @type credential: Credential
        @param networkpolicy: networkpolicy minOccurs=0 maxOccurs=unbounded
        @type networkpolicy: Link
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param reboot: reboot minOccurs=0
        @type reboot: boolean
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Link
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param targetlocation: targetlocation
        @type targetlocation: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        OnboardRequestBase.__init__(self, credential=credential, networkpolicy=networkpolicy, assetproperties=assetproperties, variables=variables, reboot=reboot, instance=instance, mgmtport=mgmtport, mgmtprotocol=mgmtprotocol, targetlocation=targetlocation, packages=packages, operatingsystem=operatingsystem, cloud=cloud)
