from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ContainerBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, blueprint=[], stack=[], container=[], containerright=[], package=[], project=[], script=[], policy=[], customcontainer=[], customitem=[], application=[], credential=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'blueprint': {'name': 'blueprint', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'script': {'name': 'script', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'stack': {'name': 'stack', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'containerRight': {'name': 'containerright', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'package': {'name': 'package', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'project': {'name': 'project', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'container': {'name': 'container', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'policy': {'name': 'policy', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'credential': {'name': 'credential', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'customItem': {'name': 'customitem', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'application': {'name': 'application', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'customContainer': {'name': 'customcontainer', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.blueprint = blueprint
        self.stack = stack
        self.container = container
        self.containerright = containerright
        self.package = package
        self.project = project
        self.script = script
        self.policy = policy
        self.customcontainer = customcontainer
        self.customitem = customitem
        self.application = application
        self.credential = credential 
