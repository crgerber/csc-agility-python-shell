from core.agility.v3_3.agilitymodel.base.Subgroup import SubgroupBase
from core.agility.v3_3.agilitymodel.actions.Subgroup import SubgroupActions

class Subgroup(SubgroupBase, SubgroupActions):
    '''
    classdocs
    '''
    def __init__(self, groupid=None, userid=None, groupname=None):
        '''
        Constructor
        @param groupid: groupid minOccurs=0
        @type groupid: string
        @param userid: userid minOccurs=0
        @type userid: string
        @param groupname: groupname minOccurs=0
        @type groupname: string
        '''
        SubgroupBase.__init__(self, groupid=groupid, userid=userid, groupname=groupname)
