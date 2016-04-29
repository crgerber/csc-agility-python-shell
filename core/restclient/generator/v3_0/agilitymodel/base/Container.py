from .VersionedItem import VersionedItemBase

class ContainerBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, blueprint=[], credential=[], container=[], package=[], script=[], customcontainer=[], customitem=[], containerright=[], project=[], application=[], policy=[], stack=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'blueprint': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'blueprint', 'minOccurs': '0', 'native': False}, 'credential': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'container': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'container', 'minOccurs': '0', 'native': False}, 'script': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'script', 'minOccurs': '0', 'native': False}, 'package': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'package', 'minOccurs': '0', 'native': False}, 'customContainer': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'customcontainer', 'minOccurs': '0', 'native': False}, 'customItem': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'customitem', 'minOccurs': '0', 'native': False}, 'containerRight': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'containerright', 'minOccurs': '0', 'native': False}, 'project': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'project', 'minOccurs': '0', 'native': False}, 'application': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'application', 'minOccurs': '0', 'native': False}, 'policy': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'policy', 'minOccurs': '0', 'native': False}, 'stack': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}})
        self.blueprint = blueprint
        self.credential = credential
        self.container = container
        self.package = package
        self.script = script
        self.customcontainer = customcontainer
        self.customitem = customitem
        self.containerright = containerright
        self.project = project
        self.application = application
        self.policy = policy
        self.stack = stack 
