
from core.base.enum import Enum

DeploymentState = Enum(**{'Unknown': 'Unknown', 'Starting': 'Starting', 'Deployed': 'Deployed', 'Failed': 'Failed', 'Released': 'Released', 'Running': 'Running', 'Stopping': 'Stopping', 'Stopped': 'Stopped'})
