from core.agility.v2_0.agilitymodel.base.Taxonomy import TaxonomyBase
from core.agility.v2_0.agilitymodel.actions.Taxonomy import TaxonomyActions

class Taxonomy(TaxonomyBase, TaxonomyActions):
    '''
    classdocs
    '''
    def __init__(self, children=list(), displayName=None, id=None, name=''):
        '''
        Constructor
        @param children: children minOccurs=0 maxOccurs=unbounded
        @type children: Taxonomy
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param id: id minOccurs=0
        @type id: int
        @param name: name
        @type name: string
        '''
        TaxonomyBase.__init__(self, children=children, displayName=displayName, id=id, name=name)
