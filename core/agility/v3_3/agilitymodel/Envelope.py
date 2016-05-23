from core.agility.v3_3.agilitymodel.base.Envelope import EnvelopeBase
from core.agility.v3_3.agilitymodel.actions.Envelope import EnvelopeActions

class Envelope(EnvelopeBase, EnvelopeActions):
    '''
    classdocs
    '''
    def __init__(self, productversion='', pendingasset=[], version='', asset=[]):
        '''
        Constructor
        @param productversion: productversion
        @type productversion: string
        @param pendingasset: pendingasset minOccurs=0 maxOccurs=unbounded
        @type pendingasset: Asset
        @param version: version
        @type version: string
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        '''
        EnvelopeBase.__init__(self, productversion=productversion, pendingasset=pendingasset, version=version, asset=asset)
