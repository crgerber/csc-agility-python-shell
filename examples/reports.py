#demo = a.tools.demo.loadDemo('examples/reports.py', 'Agility Search', autoExec=True)
# <demo> auto
#importing the agility object
from agilityshell import agility as a
from agilityshell import query
from logger import logger
# <demo> --- stop ---
#Load a snapshot of asset <Compute> from the snapshots folder
compute_before = a.tools.snapshot.loadSnapshot('../cba_snapshots/environments/', 'Compute', '10.231.219.132')
# <demo> --- stop ---
#All native python operations can be used within the Shell
print((len(compute_before)))
# <demo> --- stop ---
#Load another copy of the compute list
compute_after = a.tools.snapshot.loadSnapshot('../cba_snapshots/environments/', 'Compute', '10.231.219.132')
# <demo> --- stop ---
#Simulate some changes
#1. A compute instance doesn't exist after the upgrade
del compute_after[50]
# <demo> --- stop ---
#2. An instance name has changed
compute_after[100].name += 'BIG CHANGE'
# <demo> --- stop ---
#3. Simulate new instance after the upgrade by deleting one from before
del compute_before[150]
# <demo> --- stop ---
#Check the Help on a function from the reports Plugin, or even peek at the code
#Type: a.tools.report.diffReport?
#Type: a.tools.report.diffReport??
# <demo> --- stop ---
#Create a Diff Report in Excel format
a.tools.report.diffReport(compute_before, compute_after, fields=['id', 'name'], reportFileName='compute_diff')
# <demo> --- stop ---
#Create separate ADDED, DELETED, MODIFIED, UNCHANGED CSV reports
a.tools.report.diffReport(compute_before, compute_after, fields=['id', 'name'], reportFileName='compute_diff', format='csv')
# <demo> --- stop ---
#use Python's functional programming features to filter data offline
with_resources = [c for c in compute_before if getattr(c, 'resources', None)]
# <demo> --- stop ---
#Use a scripted scenario to obtain a list of assigned resources of type <Disk Drive> to compute instances
disk_assignment_before = a.tools.scripting.scenarios.assignedResources(compute_before, resourceType=a.tools.scripting.scenarios.assignedResources.TYPES.DISK_DRIVE)
print((len(disk_assignment_before)))
# <demo> --- stop ---
#The scenario script can extract a list of any assigned resources. Enums are attached to methods that use them for ease of use
print((a.tools.scripting.scenarios.assignedResources.TYPES))
# <demo> --- stop ---
#Extract the same data from the "after" list
disk_assignment_after = a.tools.scripting.scenarios.assignedResources(compute_after, a.tools.scripting.scenarios.assignedResources.TYPES.DISK_DRIVE)
# <demo> --- stop ---
#define fields to compare and use the reporting compare function
fields = ['assetPath', 'name', 'resourceType', 'top', 'lifecycleVersion', 'units', 'id', 'quantity']
new, deleted, modified, unchanged = a.tools.report.diff.compare(disk_assignment_before, disk_assignment_after, fields)
# <demo> --- stop ---
#Use the logger within your scripts
logger.info('Diff results: New [%s], Deleted [%s], Modified [%s], Unchanged [%s]', len(new), len(deleted), len(modified['details']), len(unchanged))
# <demo> --- stop ---
#Or define a scenario and use it to get the same task done
#Type: a.tools.scripting.scenarios.diffAssignedResources??
#Load your demo
#reports = a.tools.demo.loadDemo('examples/reports.py', 'Agility Reporting', autoExec=True)
#reformat the list of objects to a map with id as key
computemap = a.tools.scripting.idmap(compute_before)
# <demo> --- stop ---
#Flatten an object
flat = a.tools.scripting.flattenmap(computemap['479'])
print((list(flat.keys())))
# <demo> --- stop ---
#A sample of the scripting plugin to do some data drilling
print((a.tools.scripting.selectFieldsWithValueRegex(flat, 'Unknown', flatten=True)))
# <demo> --- stop ---
#Use the scripting methods to list the available features
print((a.tools.scripting.listFields(a.tools.scripting)))
# <demo> --- stop ---
