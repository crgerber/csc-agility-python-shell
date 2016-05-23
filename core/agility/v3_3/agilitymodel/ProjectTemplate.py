from core.agility.v3_3.agilitymodel.base.ProjectTemplate import ProjectTemplateBase
from core.agility.v3_3.agilitymodel.actions.ProjectTemplate import ProjectTemplateActions

class ProjectTemplate(ProjectTemplateBase, ProjectTemplateActions):
    '''
    classdocs
    '''
    def __init__(self, readyforuse=None, projecttype=None):
        '''
        Constructor
        @param readyforuse: readyforuse minOccurs=0
        @type readyforuse: boolean
        @param projecttype: projecttype minOccurs=0
        @type projecttype: Link
        '''
        ProjectTemplateBase.__init__(self, readyforuse=readyforuse, projecttype=projecttype)
