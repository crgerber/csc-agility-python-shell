from core.agility.v3_0.agilitymodel.base.DesignItem import DesignItemBase
from core.agility.v3_0.agilitymodel.actions.DesignItem import DesignItemActions

class DesignItem(DesignItemBase, DesignItemActions):
    '''
    classdocs
    '''
    def __init__(self, errorinfo=[], fixedordercont=None, anyordercont=None, layoutinfo=[], manualordercont=None, variable=[], dirty=False, manualorderposition=None, path=None, logicalid=None, fixedorderposition=None, layout=None, anyorderposition=None):
        '''
        Constructor
        @param errorinfo: errorinfo minOccurs=0 maxOccurs=unbounded
        @type errorinfo: ErrorInfo
        @param fixedordercont: fixedordercont minOccurs=0
        @type fixedordercont: Link
        @param anyordercont: anyordercont minOccurs=0
        @type anyordercont: Link
        @param layoutinfo: layoutinfo minOccurs=0 maxOccurs=unbounded
        @type layoutinfo: NameValuePair
        @param manualordercont: manualordercont minOccurs=0
        @type manualordercont: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param dirty: dirty
        @type dirty: boolean
        @param manualorderposition: manualorderposition minOccurs=0
        @type manualorderposition: integer
        @param path: path minOccurs=0
        @type path: string
        @param logicalid: logicalid minOccurs=0
        @type logicalid: string
        @param fixedorderposition: fixedorderposition minOccurs=0
        @type fixedorderposition: integer
        @param layout: layout minOccurs=0
        @type layout: string
        @param anyorderposition: anyorderposition minOccurs=0
        @type anyorderposition: integer
        '''
        DesignItemBase.__init__(self, errorinfo=errorinfo, fixedordercont=fixedordercont, anyordercont=anyordercont, layoutinfo=layoutinfo, manualordercont=manualordercont, variable=variable, dirty=dirty, manualorderposition=manualorderposition, path=path, logicalid=logicalid, fixedorderposition=fixedorderposition, layout=layout, anyorderposition=anyorderposition)
