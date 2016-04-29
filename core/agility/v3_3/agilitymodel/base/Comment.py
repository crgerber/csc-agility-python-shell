from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class CommentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, comment=None, createdon=None, user=None, updatedon=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'native': True, 'name': 'comment', 'minOccurs': '0', 'type': 'string'}, 'createdOn': {'native': True, 'name': 'createdon', 'minOccurs': '0', 'type': 'date'}, 'user': {'native': False, 'name': 'user', 'minOccurs': '0', 'type': 'Link'}, 'updatedOn': {'native': True, 'name': 'updatedon', 'minOccurs': '0', 'type': 'date'}})
        self.comment = comment
        self.createdon = createdon
        self.user = user
        self.updatedon = updatedon 
