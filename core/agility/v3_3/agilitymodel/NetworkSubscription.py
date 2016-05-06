from core.agility.v3_3.agilitymodel.base.NetworkSubscription import NetworkSubscriptionBase
from core.agility.v3_3.agilitymodel.actions.NetworkSubscription import NetworkSubscriptionActions

class NetworkSubscription(NetworkSubscriptionBase, NetworkSubscriptionActions):
    '''
    classdocs
    '''
    def __init__(self, networkprovider=None, subscriptionid=None, id=None, cloud=None):
        '''
        Constructor
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        @param subscriptionid: subscriptionid minOccurs=0
        @type subscriptionid: string
        @param id: id minOccurs=0
        @type id: int
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        NetworkSubscriptionBase.__init__(self, networkprovider=networkprovider, subscriptionid=subscriptionid, id=id, cloud=cloud)
