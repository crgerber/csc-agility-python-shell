from core.agility.v3_3.agilitymodel.base.Project import ProjectBase

class ProjectTemplateBase(ProjectBase):
    '''
    classdocs
    '''
    def __init__(self, readyforuse=None, projecttype=None):
        ProjectBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'readyForUse': {'name': 'readyforuse', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'projectType': {'name': 'projecttype', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.readyforuse = readyforuse
        self.projecttype = projecttype 
