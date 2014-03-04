from core.restclient.v2_0.agilitymodel.base.DesignItem import DesignItemBase
from core.restclient.v2_0.agilitymodel.actions.DesignItem import DesignItemActions

class DesignItem(DesignItemBase, DesignItemActions):
    '''
    classdocs
    '''
    def __init__(self, errorInfo=list(), fixedOrderCont=None, anyOrderCont=None, layoutInfo=list(), manualOrderCont=None, variable=list(), dirty=False, manualOrderPosition=None, path=None, logicalId=None, fixedOrderPosition=None, layout=None, anyOrderPosition=None):
        '''
        Constructor
        @param errorInfo: errorInfo minOccurs=0 maxOccurs=unbounded
        @type errorInfo: ErrorInfo
        @param fixedOrderCont: fixedOrderCont minOccurs=0
        @type fixedOrderCont: Link
        @param anyOrderCont: anyOrderCont minOccurs=0
        @type anyOrderCont: Link
        @param layoutInfo: layoutInfo minOccurs=0 maxOccurs=unbounded
        @type layoutInfo: NameValuePair
        @param manualOrderCont: manualOrderCont minOccurs=0
        @type manualOrderCont: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param dirty: dirty
        @type dirty: boolean
        @param manualOrderPosition: manualOrderPosition minOccurs=0
        @type manualOrderPosition: integer
        @param path: path minOccurs=0
        @type path: string
        @param logicalId: logicalId minOccurs=0
        @type logicalId: string
        @param fixedOrderPosition: fixedOrderPosition minOccurs=0
        @type fixedOrderPosition: integer
        @param layout: layout minOccurs=0
        @type layout: string
        @param anyOrderPosition: anyOrderPosition minOccurs=0
        @type anyOrderPosition: integer
        '''
        DesignItemBase.__init__(self, errorInfo=errorInfo, fixedOrderCont=fixedOrderCont, anyOrderCont=anyOrderCont, layoutInfo=layoutInfo, manualOrderCont=manualOrderCont, variable=variable, dirty=dirty, manualOrderPosition=manualOrderPosition, path=path, logicalId=logicalId, fixedOrderPosition=fixedOrderPosition, layout=layout, anyOrderPosition=anyOrderPosition)
