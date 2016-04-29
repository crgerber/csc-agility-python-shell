#Load your demo
#search  = a.tools.demo.loadDemo('examples/search.py', 'Agility Search', autoExec=True)
# <demo> auto
#importing the agility object
from agilityshell import agility as a
from agilityinit import query
from logger import logger
# <demo> --- stop ---
#Create a query object
q = query()
# <demo> --- stop ---
#Discover the available params
#q.params.
#q.params.containerId    q.params.fields         q.params.limit          q.params.searchTerm     q.params.version
#q.params.deleted        q.params.groupByValues  q.params.offset         q.params.usage          
#q.params.fieldName      q.params.keys           q.params.order          q.params.values 
# <demo> --- stop ---
#Perform a simple query, using only fieldName and searchTerm
q.params.fieldName = 'name'
q.params.searchTerm = 'ScriptTesting-1'
# <demo> --- stop ---
#Compile the query if you want to inspect the result query_params
print((q.compile()))
# <demo> --- stop ---
#Invoke any search API (compute.searchInstances in our example) passing the query_params
result = a.compute.searchInstances(**q.compile())
print(('Result size [%s]'%len(result)))
instance = result.pop()

# <demo> --- stop ---
print(instance)
# <demo> --- stop ---
#Verfiy that the search produced the expected result
print((instance.name))
