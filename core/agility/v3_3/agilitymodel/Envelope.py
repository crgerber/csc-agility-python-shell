from core.agility.v3_3.agilitymodel.base.Envelope import EnvelopeBase
from core.agility.v3_3.agilitymodel.actions.Envelope import EnvelopeActions

class Envelope(EnvelopeBase, EnvelopeActions):
    '''
    classdocs
    '''
    def __init__(self, version='', pendingasset=[], asset=[], productversion=''):
        '''
        Constructor
        @param version: version
        @type version: string
        @param pendingasset: pendingasset minOccurs=0 maxOccurs=unbounded
        @type pendingasset: Asset
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param productversion: productversion
        @type productversion: string
        '''
        EnvelopeBase.__init__(self, version=version, pendingasset=pendingasset, asset=asset, productversion=productversion)
