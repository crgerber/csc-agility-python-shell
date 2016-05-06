from core.agility.v3_3.agilitymodel.base.Taxonomy import TaxonomyBase
from core.agility.v3_3.agilitymodel.actions.Taxonomy import TaxonomyActions

class Taxonomy(TaxonomyBase, TaxonomyActions):
    '''
    classdocs
    '''
    def __init__(self, mgmtscriptgroup=None, children=[], displayname=None, id=None, name=''):
        '''
        Constructor
        @param mgmtscriptgroup: mgmtscriptgroup minOccurs=0
        @type mgmtscriptgroup: Link
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: Taxonomy
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param id: id minOccurs=0
        @type id: int
        @param name: name
        @type name: string
        '''
        TaxonomyBase.__init__(self, mgmtscriptgroup=mgmtscriptgroup, children=children, displayname=displayname, id=id, name=name)
