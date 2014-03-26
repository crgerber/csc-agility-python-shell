__author__ = 'dawood'

rejected_specs = ['https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IVariable.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IWorkflow.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IConfigurationRepository.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IUserGroup.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IInputVariables.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IStoreProductType.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ITemplate.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/INetwork.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IResource.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IArtifact.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IAuthToken.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IImage.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/script/ISessionFactory.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IBlueprint.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IEULA.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/script/SessionContext.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IServiceFactory.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IStorageSnapshot.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IConfiguration.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ISolution.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/script/ISession.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/script/Agility.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IAssetTypeSearch.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IVariableValues.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IVersion.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ILdapGroup.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IBeanAssetType.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IService.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IPackage.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IReconfigure.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IManage.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IAuthGroup.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IAttachment.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/Context.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IInstance.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ILaunchItem.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IContainer.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ILaunchItemDeployment.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IPolicyAssignment.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ExportOptions.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IDeployment.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IArtifactAttachment.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/Context.TopologyOrderType.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IRepository.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ICredential.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/script/SessionContext.SessionMode.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ICloud.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IStack.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/Context.ArtifactOrderType.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/ITopology.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IAuthentication.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/ObjectFactory.html', 'https://54.206.19.70:8443/javadoc/scripting/com/servicemesh/agility/api/service/IRepository.Entry.html']
