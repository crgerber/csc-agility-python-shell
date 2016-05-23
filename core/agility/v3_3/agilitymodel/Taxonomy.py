from core.agility.v3_3.agilitymodel.base.Taxonomy import TaxonomyBase
from core.agility.v3_3.agilitymodel.actions.Taxonomy import TaxonomyActions

class Taxonomy(TaxonomyBase, TaxonomyActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', displayname=None, children=[], mgmtscriptgroup=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param name: name
        @type name: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: Taxonomy
        @param mgmtscriptgroup: mgmtscriptgroup minOccurs=0
        @type mgmtscriptgroup: Link
        '''
        TaxonomyBase.__init__(self, id=id, name=name, displayname=displayname, children=children, mgmtscriptgroup=mgmtscriptgroup)
