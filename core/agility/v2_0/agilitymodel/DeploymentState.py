
from core.base.enum import Enum

DeploymentState = Enum(**{'Failed': 'Failed', 'Unknown': 'Unknown', 'Released': 'Released', 'Running': 'Running', 'Stopped': 'Stopped', 'Stopping': 'Stopping', 'Starting': 'Starting', 'Deployed': 'Deployed'})
