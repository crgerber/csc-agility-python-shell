from core.agility.v3_3.agilitymodel.base.Project import ProjectBase

class ProjectTemplateBase(ProjectBase):
    '''
    classdocs
    '''
    def __init__(self, projecttype=None, readyforuse=None):
        ProjectBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectType': {'native': False, 'name': 'projecttype', 'minOccurs': '0', 'type': 'Link'}, 'readyForUse': {'native': True, 'name': 'readyforuse', 'minOccurs': '0', 'type': 'boolean'}})
        self.projecttype = projecttype
        self.readyforuse = readyforuse 
