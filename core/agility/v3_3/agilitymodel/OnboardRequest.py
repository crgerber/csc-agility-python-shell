from core.agility.v3_3.agilitymodel.base.OnboardRequest import OnboardRequestBase
from core.agility.v3_3.agilitymodel.actions.OnboardRequest import OnboardRequestActions

class OnboardRequest(OnboardRequestBase, OnboardRequestActions):
    '''
    classdocs
    '''
    def __init__(self, reboot=None, credential=None, mgmtport=None, assetproperties=[], instance=[], operatingsystem=None, targetlocation=None, networkpolicy=[], mgmtprotocol=None, cloud=None, packages=[], variables=[]):
        '''
        Constructor
        @param reboot: reboot minOccurs=0
        @type reboot: boolean
        @param credential: credential
        @type credential: Credential
        @param mgmtport: mgmtport minOccurs=0
        @type mgmtport: int
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Link
        @param operatingsystem: operatingsystem minOccurs=0
        @type operatingsystem: string
        @param targetlocation: targetlocation
        @type targetlocation: Link
        @param networkpolicy: networkpolicy minOccurs=0 maxOccurs=unbounded
        @type networkpolicy: Link
        @param mgmtprotocol: mgmtprotocol minOccurs=0
        @type mgmtprotocol: string
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        OnboardRequestBase.__init__(self, reboot=reboot, credential=credential, mgmtport=mgmtport, assetproperties=assetproperties, instance=instance, operatingsystem=operatingsystem, targetlocation=targetlocation, networkpolicy=networkpolicy, mgmtprotocol=mgmtprotocol, cloud=cloud, packages=packages, variables=variables)
