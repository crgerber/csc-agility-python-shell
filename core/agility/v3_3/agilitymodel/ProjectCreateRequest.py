from core.agility.v3_3.agilitymodel.base.ProjectCreateRequest import ProjectCreateRequestBase
from core.agility.v3_3.agilitymodel.actions.ProjectCreateRequest import ProjectCreateRequestActions

class ProjectCreateRequest(ProjectCreateRequestBase, ProjectCreateRequestActions):
    '''
    classdocs
    '''
    def __init__(self, name='', description=None, projecttemplate=None, location=None, properties=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param description: description minOccurs=0
        @type description: string
        @param projecttemplate: projecttemplate
        @type projecttemplate: Link
        @param location: location
        @type location: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        '''
        ProjectCreateRequestBase.__init__(self, name=name, description=description, projecttemplate=projecttemplate, location=location, properties=properties)
