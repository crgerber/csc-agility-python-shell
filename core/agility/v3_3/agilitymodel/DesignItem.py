from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase
from core.agility.v3_3.agilitymodel.actions.DesignItem import DesignItemActions

class DesignItem(DesignItemBase, DesignItemActions):
    '''
    classdocs
    '''
    def __init__(self, anyorderposition=None, manualordercont=None, manualorderposition=None, dirty=False, variable=[], errorinfo=[], anyordercont=None, fixedordercont=None, layoutinfo=[], fixedorderposition=None, path=None, layout=None, logicalid=None):
        '''
        Constructor
        @param anyorderposition: anyorderposition minOccurs=0
        @type anyorderposition: integer
        @param manualordercont: manualordercont minOccurs=0
        @type manualordercont: Link
        @param manualorderposition: manualorderposition minOccurs=0
        @type manualorderposition: integer
        @param dirty: dirty
        @type dirty: boolean
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param errorinfo: errorinfo minOccurs=0 maxOccurs=unbounded
        @type errorinfo: ErrorInfo
        @param anyordercont: anyordercont minOccurs=0
        @type anyordercont: Link
        @param fixedordercont: fixedordercont minOccurs=0
        @type fixedordercont: Link
        @param layoutinfo: layoutinfo minOccurs=0 maxOccurs=unbounded
        @type layoutinfo: NameValuePair
        @param fixedorderposition: fixedorderposition minOccurs=0
        @type fixedorderposition: integer
        @param path: path minOccurs=0
        @type path: string
        @param layout: layout minOccurs=0
        @type layout: string
        @param logicalid: logicalid minOccurs=0
        @type logicalid: string
        '''
        DesignItemBase.__init__(self, anyorderposition=anyorderposition, manualordercont=manualordercont, manualorderposition=manualorderposition, dirty=dirty, variable=variable, errorinfo=errorinfo, anyordercont=anyordercont, fixedordercont=fixedordercont, layoutinfo=layoutinfo, fixedorderposition=fixedorderposition, path=path, layout=layout, logicalid=logicalid)
