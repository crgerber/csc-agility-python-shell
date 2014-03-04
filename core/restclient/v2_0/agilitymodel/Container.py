from core.restclient.v2_0.agilitymodel.base.Container import ContainerBase
from core.restclient.v2_0.agilitymodel.actions.Container import ContainerActions

class Container(ContainerBase, ContainerActions):
    '''
    classdocs
    '''
    def __init__(self, blueprint=list(), credential=list(), container=list(), package=list(), script=list(), customContainer=list(), customItem=list(), containerRight=list(), project=list(), application=list(), policy=list(), stack=list()):
        '''
        Constructor
        @param blueprint: blueprint minOccurs=0 maxOccurs=unbounded
        @type blueprint: Link
        @param credential: credential minOccurs=0 maxOccurs=unbounded
        @type credential: Link
        @param container: container minOccurs=0 maxOccurs=unbounded
        @type container: Link
        @param package: package minOccurs=0 maxOccurs=unbounded
        @type package: Link
        @param script: script minOccurs=0 maxOccurs=unbounded
        @type script: Link
        @param customContainer: customContainer minOccurs=0 maxOccurs=unbounded
        @type customContainer: Link
        @param customItem: customItem minOccurs=0 maxOccurs=unbounded
        @type customItem: Link
        @param containerRight: containerRight minOccurs=0 maxOccurs=unbounded
        @type containerRight: Link
        @param project: project minOccurs=0 maxOccurs=unbounded
        @type project: Link
        @param application: application minOccurs=0 maxOccurs=unbounded
        @type application: Link
        @param policy: policy minOccurs=0 maxOccurs=unbounded
        @type policy: Link
        @param stack: stack minOccurs=0 maxOccurs=unbounded
        @type stack: Link
        '''
        ContainerBase.__init__(self, blueprint=blueprint, credential=credential, container=container, package=package, script=script, customContainer=customContainer, customItem=customItem, containerRight=containerRight, project=project, application=application, policy=policy, stack=stack)
