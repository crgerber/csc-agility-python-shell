from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkSubscriptionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, subscriptionid=None, id=None, networkprovider=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'networkProvider': {'native': False, 'name': 'networkprovider', 'minOccurs': '0', 'type': 'Link'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'subscriptionId': {'native': True, 'name': 'subscriptionid', 'minOccurs': '0', 'type': 'string'}})
        self.cloud = cloud
        self.subscriptionid = subscriptionid
        self.id = id
        self.networkprovider = networkprovider 
