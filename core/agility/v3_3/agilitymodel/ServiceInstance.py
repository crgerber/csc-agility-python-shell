from core.agility.v3_3.agilitymodel.base.ServiceInstance import ServiceInstanceBase
from core.agility.v3_3.agilitymodel.actions.ServiceInstance import ServiceInstanceActions

class ServiceInstance(ServiceInstanceBase, ServiceInstanceActions):
    '''
    classdocs
    '''
    def __init__(self, service=None, firewallrule=[], dependency=[], instanceid='', variables=[], srcconnections=[], dependent=[], state=None, stoptime=None, starttime=None, provider=None, destconnections=[], configuration=[], laststartedorstoppedbyuser=None):
        '''
        Constructor
        @param service: service minOccurs=0
        @type service: Link
        @param firewallrule: firewallrule minOccurs=0 maxOccurs=unbounded
        @type firewallrule: AccessList
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param instanceid: instanceid
        @type instanceid: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param dependent: dependent minOccurs=0 maxOccurs=unbounded
        @type dependent: Link
        @param state: state
        @type state: ServiceState
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param provider: provider minOccurs=0
        @type provider: Link
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param configuration: configuration minOccurs=0 maxOccurs=unbounded
        @type configuration: AssetProperty
        @param laststartedorstoppedbyuser: laststartedorstoppedbyuser minOccurs=0
        @type laststartedorstoppedbyuser: Link
        '''
        ServiceInstanceBase.__init__(self, service=service, firewallrule=firewallrule, dependency=dependency, instanceid=instanceid, variables=variables, srcconnections=srcconnections, dependent=dependent, state=state, stoptime=stoptime, starttime=starttime, provider=provider, destconnections=destconnections, configuration=configuration, laststartedorstoppedbyuser=laststartedorstoppedbyuser)
