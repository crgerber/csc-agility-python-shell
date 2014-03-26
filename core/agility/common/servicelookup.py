'''
Created on Nov 30, 2012

Basically a compensation for non straight forward or miss-spelled asset<->service name mappings

@author: dawood
'''
from collections import defaultdict
from core.base.enum import Enum
import re

SERVICE_ACTION = Enum(**{'GET' : 'get',
                         'SEARCH' : 'search'})

def lookup(asset, action=SERVICE_ACTION.GET):
    serviceName = None
    if action == SERVICE_ACTION.GET:
        serviceNameOrPattern = SERVICE_GET_NAMES[asset]
    elif action == SERVICE_ACTION.SEARCH:
        serviceNameOrPattern = SERVICE_SEARCH_NAMES[asset]        
    if serviceNameOrPattern is None: 
        raise RuntimeError('No %s service for asset %s'%(action, asset))
    if re.match('.*%\(.*\)s.*', serviceNameOrPattern):
        serviceName = serviceNameOrPattern%{'assetName' : asset}
    return serviceName or serviceNameOrPattern

lookup.ACTION = SERVICE_ACTION


SERVICE_GET_NAMES = defaultdict(lambda: 'get%(assetName)s')

SERVICE_GET_NAMES['assettype'] = "getAssetType"
SERVICE_GET_NAMES['networkservice'] = "getNetworkService"
SERVICE_GET_NAMES['blueprint_workload'] = "getWorkload"
SERVICE_GET_NAMES['package'] = "getPackage"
SERVICE_GET_NAMES['image'] = "getImage"
SERVICE_GET_NAMES['address'] = "getAddress"
SERVICE_GET_NAMES['storerelease'] = "getRelease"
SERVICE_GET_NAMES['deployer'] = "getDeployer"
SERVICE_GET_NAMES['targetcloud'] = "getTargetCloud"
SERVICE_GET_NAMES['configuration_repository'] = "getRepository"
SERVICE_GET_NAMES['repository'] = "getRepository"
SERVICE_GET_NAMES['blueprint'] = "getBlueprint"
SERVICE_GET_NAMES['security'] = None
SERVICE_GET_NAMES['propertygroup'] = "getPropertyDefinitionGroup"
SERVICE_GET_NAMES['container'] = "getContainer"
SERVICE_GET_NAMES['search'] = "getSearchFields"
SERVICE_GET_NAMES['storeproducttype'] = "getProductType"
SERVICE_GET_NAMES['custom'] = "getAsset"
SERVICE_GET_NAMES['launchitem'] = "getLaunchItem"
SERVICE_GET_NAMES['ldapgroup'] = "getMapping"
SERVICE_GET_NAMES['addressrange'] = "getAddressRange"
SERVICE_GET_NAMES['solution'] = "getSolution"
SERVICE_GET_NAMES['auth'] = "getAuthentication"
SERVICE_GET_NAMES['scriptlanguage'] = "getScriptLanguage"
SERVICE_GET_NAMES['domain'] = "getDomain"
SERVICE_GET_NAMES['tree'] = "getDesignTreeNode"
SERVICE_GET_NAMES['servicebindingtype'] = "getType"
SERVICE_GET_NAMES['runtime'] = "getRuntime"
SERVICE_GET_NAMES['environment'] = "getEnvironment"
SERVICE_GET_NAMES['launchitemdeployment'] = "getDeployment"
SERVICE_GET_NAMES['setup'] = "getConfiguation"
SERVICE_GET_NAMES['paas'] = "getPlatformService"
SERVICE_GET_NAMES['storecatalog'] = "getCatalog"
SERVICE_GET_NAMES['os'] = "getOperatingSystem"
SERVICE_GET_NAMES['user'] = "getUser"
SERVICE_GET_NAMES['volumestoragesnapshot'] = "getVolumeStorageSnapshot"
SERVICE_GET_NAMES['solutiondeployment'] = "getSolutionDeployment"
SERVICE_GET_NAMES['connection'] = "getConnection"
SERVICE_GET_NAMES['configuration_artifacttype'] = "getArtifactType"
SERVICE_GET_NAMES['designdeployer'] = "getDeployer"
SERVICE_GET_NAMES['volumestorage'] = "getVolumeStorage"
SERVICE_GET_NAMES['blueprint_designcontainer'] = "getDesignContainer"
SERVICE_GET_NAMES['artifactattachment'] = "getAttachment"
SERVICE_GET_NAMES['global_'] = "getGlobalContainer"
SERVICE_GET_NAMES['storecategory'] = "getCategory"
SERVICE_GET_NAMES['networkservicetype'] = "getNetworkServiceType"
SERVICE_GET_NAMES['environmenttype'] = "getEnvironmentType"
SERVICE_GET_NAMES['policy'] = "getPolicy"
SERVICE_GET_NAMES['storeedition'] = "getEdition"
SERVICE_GET_NAMES['location'] = "getLocation"
SERVICE_GET_NAMES['configuration_artifact'] = "getArtifact"
SERVICE_GET_NAMES['network'] = "getNetwork"
SERVICE_GET_NAMES['scriptclasspath'] = "getScriptClasspath"
SERVICE_GET_NAMES['template'] = "getTemplate"
SERVICE_GET_NAMES['paastype'] = "getPlatformServiceType"
SERVICE_GET_NAMES['script'] = "getScript"
SERVICE_GET_NAMES['task'] = "getTask"
SERVICE_GET_NAMES['cloudtype'] = "getCloudType"
SERVICE_GET_NAMES['topology'] = "getTopology"
SERVICE_GET_NAMES['model'] = "getModel"
SERVICE_GET_NAMES['designcontainer'] = "getDesignContainer"
SERVICE_GET_NAMES['storeproduct'] = "getProduct"
SERVICE_GET_NAMES['permissiontype'] = "getPermissionType"
SERVICE_GET_NAMES['project'] = "getProject"
SERVICE_GET_NAMES['compute'] = "getInstance"
SERVICE_GET_NAMES['storeproductadapter'] = "getProductAdapter"
SERVICE_GET_NAMES['volume'] = "getVolume"
SERVICE_GET_NAMES['attachment'] = "getAttachmentMulti"
SERVICE_GET_NAMES['artifact'] = "getArtifact"
SERVICE_GET_NAMES['storage'] = "getStorage"
SERVICE_GET_NAMES['stack'] = "getStack"
SERVICE_GET_NAMES['artifacttype'] = "getType"
SERVICE_GET_NAMES['alias'] = "getAlias"
SERVICE_GET_NAMES['projectrole'] = "getProjectRole"
SERVICE_GET_NAMES['configuration_resource'] = "getResource"
SERVICE_GET_NAMES['propertytype'] = "getPropertyType"
SERVICE_GET_NAMES['authtype'] = "getAuthenticationType"
SERVICE_GET_NAMES['networkinterface'] = "getNetwork"
SERVICE_GET_NAMES['onboard'] = "getOnboardMeta"
SERVICE_GET_NAMES['customcontainer'] = "getCustomContainer"
SERVICE_GET_NAMES['credential'] = "getCredential"
SERVICE_GET_NAMES['cloud'] = "getCloud"
SERVICE_GET_NAMES['dhcpoptions'] = "getDhcpOptions"
SERVICE_GET_NAMES['usergroup'] = "getUserGroup"


#ASSET_SERVICE_MAP = defaultdict(lambda: 'get%(assetName)s')
#ASSET_SERVICE_MAP['Compute'] = 'getInstance'

SERVICE_SEARCH_NAMES = {'cloud': 'searchClouds',
 'compute': 'searchInstances',
 'container': 'searchContainers',
 'credential': None,
 'environment': 'searchEnvironments',
 'image': 'searchImages',
 'model': None,
 'network': None,
 'networkService': None,
 'package': 'searchPackages',
 'policy': 'searchPolicies',
 'project': 'searchProjects',
 'script': 'searchScripts',
 'stack': 'searchStacks',
 'template': 'searchTemplates',
 'topology': 'searchTopologies',
 'user': 'searchUsers',
 'userGroup': 'searchUserGroups',
 'volume': None} 

