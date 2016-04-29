from core.agility.v3_3.agilitymodel.base.ServiceInstance import ServiceInstanceBase
from core.agility.v3_3.agilitymodel.actions.ServiceInstance import ServiceInstanceActions

class ServiceInstance(ServiceInstanceBase, ServiceInstanceActions):
    '''
    classdocs
    '''
    def __init__(self, laststartedorstoppedbyuser=None, dependent=[], destconnections=[], dependency=[], instanceid='', state=None, provider=None, starttime=None, configuration=[], srcconnections=[], service=None, stoptime=None, firewallrule=[], variables=[]):
        '''
        Constructor
        @param laststartedorstoppedbyuser: laststartedorstoppedbyuser minOccurs=0
        @type laststartedorstoppedbyuser: Link
        @param dependent: dependent minOccurs=0 maxOccurs=unbounded
        @type dependent: Link
        @param destconnections: destconnections minOccurs=0 maxOccurs=unbounded
        @type destconnections: Link
        @param dependency: dependency minOccurs=0 maxOccurs=unbounded
        @type dependency: Link
        @param instanceid: instanceid
        @type instanceid: string
        @param state: state
        @type state: ServiceState
        @param provider: provider minOccurs=0
        @type provider: Link
        @param starttime: starttime minOccurs=0
        @type starttime: date
        @param configuration: configuration minOccurs=0 maxOccurs=unbounded
        @type configuration: AssetProperty
        @param srcconnections: srcconnections minOccurs=0 maxOccurs=unbounded
        @type srcconnections: Link
        @param service: service minOccurs=0
        @type service: Link
        @param stoptime: stoptime minOccurs=0
        @type stoptime: date
        @param firewallrule: firewallrule minOccurs=0 maxOccurs=unbounded
        @type firewallrule: AccessList
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        ServiceInstanceBase.__init__(self, laststartedorstoppedbyuser=laststartedorstoppedbyuser, dependent=dependent, destconnections=destconnections, dependency=dependency, instanceid=instanceid, state=state, provider=provider, starttime=starttime, configuration=configuration, srcconnections=srcconnections, service=service, stoptime=stoptime, firewallrule=firewallrule, variables=variables)
