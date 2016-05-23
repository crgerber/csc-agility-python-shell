from core.agility.v3_3.agilitymodel.base.DistNodePackage import DistNodePackageBase
from core.agility.v3_3.agilitymodel.actions.DistNodePackage import DistNodePackageActions

class DistNodePackage(DistNodePackageBase, DistNodePackageActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, status=None, version=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        @param status: status minOccurs=0
        @type status: string
        @param version: version minOccurs=0
        @type version: string
        '''
        DistNodePackageBase.__init__(self, id=id, name=name, status=status, version=version)
