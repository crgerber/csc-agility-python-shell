from core.agility.v3_3.agilitymodel.base.VersionedItem import VersionedItemBase

class ContainerBase(VersionedItemBase):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[], credential=[], package=[], blueprint=[], script=[], containerright=[], policy=[], project=[], container=[], stack=[], customitem=[], application=[]):
        VersionedItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customContainer': {'maxOccurs': 'unbounded', 'native': False, 'name': 'customcontainer', 'minOccurs': '0', 'type': 'Link'}, 'credential': {'maxOccurs': 'unbounded', 'native': False, 'name': 'credential', 'minOccurs': '0', 'type': 'Link'}, 'package': {'maxOccurs': 'unbounded', 'native': False, 'name': 'package', 'minOccurs': '0', 'type': 'Link'}, 'blueprint': {'maxOccurs': 'unbounded', 'native': False, 'name': 'blueprint', 'minOccurs': '0', 'type': 'Link'}, 'script': {'maxOccurs': 'unbounded', 'native': False, 'name': 'script', 'minOccurs': '0', 'type': 'Link'}, 'containerRight': {'maxOccurs': 'unbounded', 'native': False, 'name': 'containerright', 'minOccurs': '0', 'type': 'Link'}, 'policy': {'maxOccurs': 'unbounded', 'native': False, 'name': 'policy', 'minOccurs': '0', 'type': 'Link'}, 'project': {'maxOccurs': 'unbounded', 'native': False, 'name': 'project', 'minOccurs': '0', 'type': 'Link'}, 'container': {'maxOccurs': 'unbounded', 'native': False, 'name': 'container', 'minOccurs': '0', 'type': 'Link'}, 'stack': {'maxOccurs': 'unbounded', 'native': False, 'name': 'stack', 'minOccurs': '0', 'type': 'Link'}, 'customItem': {'maxOccurs': 'unbounded', 'native': False, 'name': 'customitem', 'minOccurs': '0', 'type': 'Link'}, 'application': {'maxOccurs': 'unbounded', 'native': False, 'name': 'application', 'minOccurs': '0', 'type': 'Link'}})
        self.customcontainer = customcontainer
        self.credential = credential
        self.package = package
        self.blueprint = blueprint
        self.script = script
        self.containerright = containerright
        self.policy = policy
        self.project = project
        self.container = container
        self.stack = stack
        self.customitem = customitem
        self.application = application 
