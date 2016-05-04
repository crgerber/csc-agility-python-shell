from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkSubscriptionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, networkprovider=None, subscriptionid=None, id=None, cloud=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'subscriptionId': {'type': 'string', 'name': 'subscriptionid', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'networkProvider': {'type': 'Link', 'name': 'networkprovider', 'minOccurs': '0', 'native': False}})
        self.networkprovider = networkprovider
        self.subscriptionid = subscriptionid
        self.id = id
        self.cloud = cloud 
