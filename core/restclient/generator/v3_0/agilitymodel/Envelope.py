from base.Envelope import EnvelopeBase
from actions.Envelope import EnvelopeActions

class Envelope(EnvelopeBase, EnvelopeActions):
    '''
    classdocs
    '''
    def __init__(self, pendingasset=[], asset=[], version='', productversion=''):
        '''
        Constructor
        @param pendingasset: pendingasset minOccurs=0 maxOccurs=unbounded
        @type pendingasset: Asset
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param version: version
        @type version: string
        @param productversion: productversion
        @type productversion: string
        '''
        EnvelopeBase.__init__(self, pendingasset=pendingasset, asset=asset, version=version, productversion=productversion)
