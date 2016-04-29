from core.agility.v3_3.agilitymodel.base.DistNodePackage import DistNodePackageBase
from core.agility.v3_3.agilitymodel.actions.DistNodePackage import DistNodePackageActions

class DistNodePackage(DistNodePackageBase, DistNodePackageActions):
    '''
    classdocs
    '''
    def __init__(self, version=None, name=None, status=None, id=None):
        '''
        Constructor
        @param version: version minOccurs=0
        @type version: string
        @param name: name minOccurs=0
        @type name: string
        @param status: status minOccurs=0
        @type status: string
        @param id: id minOccurs=0
        @type id: int
        '''
        DistNodePackageBase.__init__(self, version=version, name=name, status=status, id=id)
