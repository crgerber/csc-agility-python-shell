#Load your demo
#demo = a.tools.demo.loadDemo('examples/smart.py', 'Dynamic Proxies', autoExec=True)
# <demo> auto
#importing the agility object
from agilityshell import agility as a
from agilityinit import query
from logger import logger
# <demo> --- stop ---
#Load a top level container
container = a.container.listDetails()
#Wrap the container in a dynamic proxy
smart = a.tools.smart.proxy(container)[0]
#Explore the attribute with DOT + TAB
#smart.
#smart.assetPath        smart.creator          smart.get              smart.name             smart.removable        smart.top
#smart.assetType        smart.customContainer  smart.id               smart.package          smart.save             smart.typeName
#smart.containerRight   smart.description      smart.latest           smart.policy           smart.script           smart.uuid
#smart.created          smart.domain           smart.lockType         smart.project          smart.stack            smart.version
# <demo> --- stop ---
#Note the child assets are loaded with special names id<ID>
#smart.project.
#smart.project.append     smart.project.id15       smart.project.id4        smart.project.save       smart.project.useid
#smart.project.autoload   smart.project.id2        smart.project.id9        smart.project.typeName   
#smart.project.get        smart.project.id3        smart.project.recursive  smart.project.usehref
# <demo> --- stop ---
#You can turn autoload off from this level on if you want
smart.project.autoload = False
# <demo> --- stop ---
#smart.project.id2.
#smart.project.id2.get       smart.project.id2.name      smart.project.id2.save      
#smart.project.id2.href      smart.project.id2.position  smart.project.id2.type      
#smart.project.id2.id        smart.project.id2.rel       smart.project.id2.typeName  
# <demo> --- stop ---
#Let's just keep it on for now
smart.project.autoload = True
#Feeling Lucky!
print((smart.project.id15.stack.id34.template.id610.topology.id15))
# <demo> --- stop ---
#That is a topology in a JSON like representation
t = smart.project.id15.stack.id34.template.id610.topology.id15
# <demo> --- stop ---
#Print a component 
print((smart.project.id15))
# <demo> --- stop ---
#Explore further down the tree
#smart.project.id15.
#smart.project.id15.anyOrder      smart.project.id15.domain        smart.project.id15.name          smart.project.id15.stack
#smart.project.id15.assetPath     smart.project.id15.get           smart.project.id15.package       smart.project.id15.top
#smart.project.id15.assetType     smart.project.id15.id            smart.project.id15.parent        smart.project.id15.typeName
#smart.project.id15.created       smart.project.id15.lastModified  smart.project.id15.removable     smart.project.id15.uuid
#smart.project.id15.creator       smart.project.id15.latest        smart.project.id15.save          smart.project.id15.version
#smart.project.id15.description   smart.project.id15.lockType      smart.project.id15.script        
# <demo> --- stop ---
#and further down
print((smart.project.id15.stack.id34))
# <demo> --- stop ---
#That is a stack object there
stack = smart.project.id15.stack.id34
# <demo> --- stop ---
#You can navigate the tree using NAME instead of ID as well
container = a.container.listDetails()
smart = a.tools.smart.proxy(container, useid=False)[0]
#smart.project.name
#smart.project.nameAgility_Factory         smart.project.nameF5_VE                   smart.project.nameUnauthorized_Instances
#smart.project.nameAgility_Platform        smart.project.nameJBoss                   
print((smart.project.nameAgility_Platform.policy.nameAgilityCollector_In.id))
