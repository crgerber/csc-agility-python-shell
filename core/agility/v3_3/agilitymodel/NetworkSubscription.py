from core.agility.v3_3.agilitymodel.base.NetworkSubscription import NetworkSubscriptionBase
from core.agility.v3_3.agilitymodel.actions.NetworkSubscription import NetworkSubscriptionActions

class NetworkSubscription(NetworkSubscriptionBase, NetworkSubscriptionActions):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, subscriptionid=None, id=None, networkprovider=None):
        '''
        Constructor
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param subscriptionid: subscriptionid minOccurs=0
        @type subscriptionid: string
        @param id: id minOccurs=0
        @type id: int
        @param networkprovider: networkprovider minOccurs=0
        @type networkprovider: Link
        '''
        NetworkSubscriptionBase.__init__(self, cloud=cloud, subscriptionid=subscriptionid, id=id, networkprovider=networkprovider)
