from base.DistNodePackage import DistNodePackageBase
from actions.DistNodePackage import DistNodePackageActions

class DistNodePackage(DistNodePackageBase, DistNodePackageActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, version=None, id=None, name=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param version: version minOccurs=0
        @type version: string
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        DistNodePackageBase.__init__(self, status=status, version=version, id=id, name=name)
