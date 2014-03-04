from core.restclient.v2_0.agilitymodel.base import AgilityModelBase

class LinkActions(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def load(self):
        from agilityshell import agility
        href = getattr(self, 'href', None)
        if href is None:
            return self
        return agility.tools.xml.parse(agility.cfg.conn.request(href).read(), assetType=AgilityModelBase._extractTypeName(self, self._asMap()))
