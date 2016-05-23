from core.agility.v3_3.agilitymodel.base.Deployment import DeploymentBase

class SolutionDeploymentBase(DeploymentBase):
    '''
    classdocs
    '''
    def __init__(self, artifacts=[], artifactversions=[], solution=None):
        DeploymentBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifacts': {'name': 'artifacts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'artifactVersions': {'name': 'artifactversions', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Artifact'}, 'solution': {'name': 'solution', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.artifacts = artifacts
        self.artifactversions = artifactversions
        self.solution = solution 
