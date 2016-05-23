from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkSubscriptionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, cloud=None, subscriptionid=None, networkprovider=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'subscriptionId': {'name': 'subscriptionid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networkProvider': {'name': 'networkprovider', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.id = id
        self.cloud = cloud
        self.subscriptionid = subscriptionid
        self.networkprovider = networkprovider 
