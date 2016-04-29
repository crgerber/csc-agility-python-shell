from core.agility.v3_3.agilitymodel.base.Deployment import DeploymentBase

class SolutionDeploymentBase(DeploymentBase):
    '''
    classdocs
    '''
    def __init__(self, solution=None, artifacts=[], artifactversions=[]):
        DeploymentBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'solution': {'native': False, 'name': 'solution', 'minOccurs': '0', 'type': 'Link'}, 'artifacts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifacts', 'minOccurs': '0', 'type': 'Link'}, 'artifactVersions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifactversions', 'minOccurs': '0', 'type': 'Artifact'}})
        self.solution = solution
        self.artifacts = artifacts
        self.artifactversions = artifactversions 
