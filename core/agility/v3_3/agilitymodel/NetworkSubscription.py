from core.agility.v3_3.agilitymodel.base.NetworkSubscription import NetworkSubscriptionBase
from core.agility.v3_3.agilitymodel.actions.NetworkSubscription import NetworkSubscriptionActions

class NetworkSubscription(NetworkSubscriptionBase, NetworkSubscriptionActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, cloud=None, subscriptionid=None, networkprovider=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param subscriptionid: subscriptionid minOccurs=0
        @type subscriptionid: string
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        '''
        NetworkSubscriptionBase.__init__(self, id=id, cloud=cloud, subscriptionid=subscriptionid, networkprovider=networkprovider)
