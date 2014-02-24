'''
Created on Apr 23, 2013

@author: dawood
'''

from agilityshell import agility as a
from agilityshell import query
from logger import logger

projectroles = a.tools.scripting.idmap(a.projectrole.listDetails(), keyField='name')
projectroleOwner = projectroles['Owner']