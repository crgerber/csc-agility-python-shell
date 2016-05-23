from core.agility.v3_3.agilitymodel.base.ServiceInstance import ServiceInstanceBase
from core.agility.v3_3.agilitymodel.actions.ServiceInstance import ServiceInstanceActions

class ServiceInstance(ServiceInstanceBase, ServiceInstanceActions):
    '''
    classdocs
    '''
    def __init__(self, starttime=None, instanceid='', srcconnections=[], provider=None, stoptime=None, configuration=[], dependent=[], dependency=[], state=None, variables=[], firewallrule=[], destconnections=[], service=None, laststartedorstoppedbyuser=None):
        '''
        Constructor
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param instanceid: instanceid
        @type instanceid: string
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param provider: provider minOccurs=0
        @type provider: Link
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param configuration: configuration minOccurs=0 maxOccurs=unbounded
        @type configuration: AssetProperty
        @param dependent: dependent minOccurs=0 maxOccurs=unbounded
        @type dependent: Link
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param state: state
        @type state: ServiceState
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param firewallrule: firewallrule minOccurs=0 maxOccurs=unbounded
        @type firewallrule: AccessList
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param service: service minOccurs=0
        @type service: Link
        @param laststartedorstoppedbyuser: laststartedorstoppedbyuser minOccurs=0
        @type laststartedorstoppedbyuser: Link
        '''
        ServiceInstanceBase.__init__(self, starttime=starttime, instanceid=instanceid, srcconnections=srcconnections, provider=provider, stoptime=stoptime, configuration=configuration, dependent=dependent, dependency=dependency, state=state, variables=variables, firewallrule=firewallrule, destconnections=destconnections, service=service, laststartedorstoppedbyuser=laststartedorstoppedbyuser)
