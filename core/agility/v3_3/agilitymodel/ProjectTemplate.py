from core.agility.v3_3.agilitymodel.base.ProjectTemplate import ProjectTemplateBase
from core.agility.v3_3.agilitymodel.actions.ProjectTemplate import ProjectTemplateActions

class ProjectTemplate(ProjectTemplateBase, ProjectTemplateActions):
    '''
    classdocs
    '''
    def __init__(self, projecttype=None, readyforuse=None):
        '''
        Constructor
        @param projecttype: projecttype minOccurs=0
        @type projecttype: Link
        @param readyforuse: readyforuse minOccurs=0
        @type readyforuse: boolean
        '''
        ProjectTemplateBase.__init__(self, projecttype=projecttype, readyforuse=readyforuse)
