#Load your demo
#xml  = a.tools.demo.loadDemo('examples/xmlobjects.py', 'Agility Search', autoExec=True)
# <demo> auto
#importing the agility object
from agilityshell import agility as a
from logger import logger
#Load Compute assets from a snapshot
#Exact result as the call: a.compute.listDetails()
compute = a.tools.snapshot.loadSnapshot('../cba_snapshots/environments/', 'Compute', '10.231.219.132')
# <demo> --- stop ---
#Use Python builtins naturally with your data structures 
print((len(compute)))
# <demo> --- stop ---
#XML is parsed into Smart Objects, Pop an instance and inspect its type
instance = compute[0]
print((type(instance)))
# <demo> --- stop ---
#Smart Objects are iterable, let's print all the attribute names of our instance
for attr in instance: print(attr)
# <demo> --- stop ---
#Or use DOT + TAB to browse
#instance.
#instance.assetPath         instance.id                instance.properties        instance.template
#instance.assetType         instance.instanceId        instance.publicAddress     instance.top
#instance.cloud             instance.lifecycleVersion  instance.save              instance.typeName
#instance.get               instance.name              instance.stack             instance.uuid
#instance.hostname          instance.onboarded         instance.state             
# <demo> --- stop ---
#Asset Complex Attributes are objects themselves
print((instance.properties.name))
# <demo> --- stop ---
#Or print the complex attribute, note the familiar JSON like representation
print((instance.properties))
# <demo> --- stop ---
#Smart object are subscriptable by attribute name if you want, comes in handy in generic scripts
attributeName = 'state'
print((instance[attributeName]))
# <demo> --- stop ---
#Smart objects respond natively to logical operators, a deep comparison takes place behind the scenes
instance1 = compute[1]
#is there resources assigned?
print(('resources' in instance))
#are two instances equal?
print((instance == instance1))
# <demo> --- stop ---
##Common scripting tasks are offered by the Scripting Plugin
#For example, transform the List of Object into a Map with ID as Key
computeMap = a.tools.scripting.idmap(compute)
print((list(computeMap.keys())[:10]))
# <demo> --- stop ---
#The magic of Python is available in the shell, e.g. My all time favorite: List Comprehension
#Print a quick nice SAMPLE report
report = ['id: [%s], name: %s, state: %s'%(c.id, c.name, c.state) for c in compute[:10]]
for entry in report: print(entry)
# <demo> --- stop ---
#Perform complex offline filtering if you wish
with_resources = [c for c in compute if getattr(c, 'resources', None)]
print((len(with_resources)))
# <demo> --- stop ---
#Additional Plugins can be made available, realizing commonly used Scenarios
#a.tools.scripting.scenarios.
#a.tools.scripting.scenarios.assignedResources      a.tools.scripting.scenarios.memory
#a.tools.scripting.scenarios.diffAssignedDisks      a.tools.scripting.scenarios.nics
#a.tools.scripting.scenarios.diffAssignedResources  a.tools.scripting.scenarios.processors
#a.tools.scripting.scenarios.disks
# <demo> --- stop ---
#You think the names are long and silly, go ahead and create aliases interactively
getResources = a.tools.scripting.scenarios.assignedResources
# <demo> --- stop ---
#If a function requires an Enumeration of values, it is right there as a property of the function itself
#getResources.TYPES.
#getResources.TYPES.DISK_DRIVE        getResources.TYPES.MEMORY            getResources.TYPES.keys
#getResources.TYPES.ETHERNET_ADAPTER  getResources.TYPES.PROCESSOR         getResources.TYPES.values
# <demo> --- stop ---
#Let's retrieve a map of instance-id -> assigned Disks
computeDisks = getResources(compute, getResources.TYPES.DISK_DRIVE)
#If you've missed that result, you can catch up by using the special '_' variable_
# <demo> --- stop ---
#What about an aggregate report of instance id and number of assigned disks
report = [(id, len(disks)) for id, disks in list(computeDisks.items())]
for entry in report: print(entry)
# <demo> --- stop ---
#Or any kind of reports actually
report = ['compute: [%s], name: %s, state: %s: disks: %s'%(id, computeMap[id].name, computeMap[id].state, ['%s : %s %s'%(d.name, d.quantity, d.units) for d in disks]) for id, disks in list(computeDisks.items())]
for entry in report: print(entry)