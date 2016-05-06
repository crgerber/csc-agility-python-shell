from core.agility.v3_3.agilitymodel.base.Subgroup import SubgroupBase
from core.agility.v3_3.agilitymodel.actions.Subgroup import SubgroupActions

class Subgroup(SubgroupBase, SubgroupActions):
    '''
    classdocs
    '''
    def __init__(self, groupname=None, userid=None, groupid=None):
        '''
        Constructor
        @param groupname: groupname minOccurs=0
        @type groupname: string
        @param userid: userid minOccurs=0
        @type userid: string
        @param groupid: groupid minOccurs=0
        @type groupid: string
        '''
        SubgroupBase.__init__(self, groupname=groupname, userid=userid, groupid=groupid)
