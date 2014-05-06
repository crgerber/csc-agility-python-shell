from core.agility.v2_0.agilitymodel.base.Envelope import EnvelopeBase
from core.agility.v2_0.agilitymodel.actions.Envelope import EnvelopeActions

class Envelope(EnvelopeBase, EnvelopeActions):
    '''
    classdocs
    '''
    def __init__(self, pendingAsset=list(), Asset=list(), version='', productVersion=''):
        '''
        Constructor
        @param pendingAsset: pendingAsset minOccurs=0 maxOccurs=unbounded
        @type pendingAsset: Asset
        @param Asset: Asset minOccurs=0 maxOccurs=unbounded
        @type Asset: Asset
        @param version: version
        @type version: string
        @param productVersion: productVersion
        @type productVersion: string
        '''
        EnvelopeBase.__init__(self, pendingAsset=pendingAsset, Asset=Asset, version=version, productVersion=productVersion)
