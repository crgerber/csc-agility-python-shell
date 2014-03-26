from core.agility.v3_0.agilitymodel.base.Deployment import DeploymentBase

class SolutionDeploymentBase(DeploymentBase):
    '''
    classdocs
    '''
    def __init__(self, artifacts=[], solution=None, artifactversions=[]):
        DeploymentBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifacts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'artifacts', 'minOccurs': '0', 'native': False}, 'solution': {'type': 'Link', 'name': 'solution', 'minOccurs': '0', 'native': False}, 'artifactVersions': {'maxOccurs': 'unbounded', 'type': 'Artifact', 'name': 'artifactversions', 'minOccurs': '0', 'native': False}})
        self.artifacts = artifacts
        self.solution = solution
        self.artifactversions = artifactversions 
