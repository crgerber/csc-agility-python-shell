from core.agility.v3_3.agilitymodel.base.IpPermission import IpPermissionBase
from core.agility.v3_3.agilitymodel.actions.IpPermission import IpPermissionActions

class IpPermission(IpPermissionBase, IpPermissionActions):
    '''
    classdocs
    '''
    def __init__(self, ipprotocol=None, subgroup=[], cidrblock=[], toport=None, fromport=None):
        '''
        Constructor
        @param ipprotocol: ipprotocol minOccurs=0
        @type ipprotocol: string
        @param subgroup: subgroup minOccurs=0 maxOccurs=unbounded
        @type subgroup: Subgroup
        @param cidrblock: cidrblock minOccurs=0 maxOccurs=unbounded
        @type cidrblock: string
        @param toport: toport minOccurs=0
        @type toport: int
        @param fromport: fromport minOccurs=0
        @type fromport: int
        '''
        IpPermissionBase.__init__(self, ipprotocol=ipprotocol, subgroup=subgroup, cidrblock=cidrblock, toport=toport, fromport=fromport)
