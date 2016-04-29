from core.agility.v3_3.agilitymodel.base.DesignItem import DesignItemBase
from core.agility.v3_3.agilitymodel.actions.DesignItem import DesignItemActions

class DesignItem(DesignItemBase, DesignItemActions):
    '''
    classdocs
    '''
    def __init__(self, layoutinfo=[], errorinfo=[], path=None, dirty=False, anyorderposition=None, anyordercont=None, fixedordercont=None, fixedorderposition=None, layout=None, manualorderposition=None, manualordercont=None, logicalid=None, variable=[]):
        '''
        Constructor
        @param layoutinfo: layoutinfo minOccurs=0 maxOccurs=unbounded
        @type layoutinfo: NameValuePair
        @param errorinfo: errorinfo minOccurs=0 maxOccurs=unbounded
        @type errorinfo: ErrorInfo
        @param path: path minOccurs=0
        @type path: string
        @param dirty: dirty
        @type dirty: boolean
        @param anyorderposition: anyorderposition minOccurs=0
        @type anyorderposition: integer
        @param anyordercont: anyordercont minOccurs=0
        @type anyordercont: Link
        @param fixedordercont: fixedordercont minOccurs=0
        @type fixedordercont: Link
        @param fixedorderposition: fixedorderposition minOccurs=0
        @type fixedorderposition: integer
        @param layout: layout minOccurs=0
        @type layout: string
        @param manualorderposition: manualorderposition minOccurs=0
        @type manualorderposition: integer
        @param manualordercont: manualordercont minOccurs=0
        @type manualordercont: Link
        @param logicalid: logicalid minOccurs=0
        @type logicalid: string
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        '''
        DesignItemBase.__init__(self, layoutinfo=layoutinfo, errorinfo=errorinfo, path=path, dirty=dirty, anyorderposition=anyorderposition, anyordercont=anyordercont, fixedordercont=fixedordercont, fixedorderposition=fixedorderposition, layout=layout, manualorderposition=manualorderposition, manualordercont=manualordercont, logicalid=logicalid, variable=variable)
