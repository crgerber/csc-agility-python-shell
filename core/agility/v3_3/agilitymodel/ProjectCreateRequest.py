from core.agility.v3_3.agilitymodel.base.ProjectCreateRequest import ProjectCreateRequestBase
from core.agility.v3_3.agilitymodel.actions.ProjectCreateRequest import ProjectCreateRequestActions

class ProjectCreateRequest(ProjectCreateRequestBase, ProjectCreateRequestActions):
    '''
    classdocs
    '''
    def __init__(self, projecttemplate=None, location=None, name='', description=None, properties=[]):
        '''
        Constructor
        @param projecttemplate: projecttemplate
        @type projecttemplate: Link
        @param location: location
        @type location: Link
        @param name: name
        @type name: string
        @param description: description minOccurs=0
        @type description: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        '''
        ProjectCreateRequestBase.__init__(self, projecttemplate=projecttemplate, location=location, name=name, description=description, properties=properties)
