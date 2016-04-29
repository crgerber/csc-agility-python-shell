
from core.base.enum import Enum

DeploymentState = Enum(**{'Deployed': 'Deployed', 'Running': 'Running', 'Unknown': 'Unknown', 'Failed': 'Failed', 'Stopping': 'Stopping', 'Stopped': 'Stopped', 'Released': 'Released', 'Starting': 'Starting'})
