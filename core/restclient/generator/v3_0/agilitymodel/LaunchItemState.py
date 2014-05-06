
from core.base.enum import Enum

LaunchItemState = Enum(**{'Ordered': 'Ordered', 'Failed': 'Failed', 'Unknown': 'Unknown', 'DeployPending': 'DeployPending', 'Deleting': 'Deleting', 'Rejected': 'Rejected', 'Paused': 'Paused', 'Released': 'Released', 'Running': 'Running', 'Stopped': 'Stopped', 'Deploying': 'Deploying', 'DeployFailed': 'DeployFailed', 'Stopping': 'Stopping', 'OrderFailed': 'OrderFailed', 'Degraded': 'Degraded', 'OrderProvisioning': 'OrderProvisioning', 'Starting': 'Starting', 'OrderPending': 'OrderPending', 'Deployed': 'Deployed'})
