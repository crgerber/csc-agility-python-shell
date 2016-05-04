from core.agility.v3_3.agilitymodel.base.Project import ProjectBase

class ProjectTemplateBase(ProjectBase):
    '''
    classdocs
    '''
    def __init__(self, readyforuse=None, projecttype=None):
        ProjectBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectType': {'type': 'Link', 'name': 'projecttype', 'minOccurs': '0', 'native': False}, 'readyForUse': {'type': 'boolean', 'name': 'readyforuse', 'minOccurs': '0', 'native': True}})
        self.readyforuse = readyforuse
        self.projecttype = projecttype 
