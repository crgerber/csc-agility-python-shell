from base.ProjectCreateRequest import ProjectCreateRequestBase
from actions.ProjectCreateRequest import ProjectCreateRequestActions

class ProjectCreateRequest(ProjectCreateRequestBase, ProjectCreateRequestActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], location=None, name='', projecttemplate=None, description=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: AssetProperty
        @param location: location
        @type location: Link
        @param name: name
        @type name: string
        @param projecttemplate: projecttemplate
        @type projecttemplate: Link
        @param description: description minOccurs=0
        @type description: string
        '''
        ProjectCreateRequestBase.__init__(self, properties=properties, location=location, name=name, projecttemplate=projecttemplate, description=description)
