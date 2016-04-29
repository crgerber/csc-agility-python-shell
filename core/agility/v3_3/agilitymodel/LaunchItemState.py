
from core.base.enum import Enum

LaunchItemState = Enum(**{'Deleting': 'Deleting', 'DeployPending': 'DeployPending', 'Ordered': 'Ordered', 'Starting': 'Starting', 'OrderFailed': 'OrderFailed', 'Failed': 'Failed', 'Rejected': 'Rejected', 'Degraded': 'Degraded', 'OrderProvisioning': 'OrderProvisioning', 'Unprovisioned': 'Unprovisioned', 'Deploying': 'Deploying', 'DeployFailed': 'DeployFailed', 'Deployed': 'Deployed', 'Paused': 'Paused', 'OrderPending': 'OrderPending', 'Running': 'Running', 'Stopping': 'Stopping', 'Stopped': 'Stopped', 'Released': 'Released', 'Unknown': 'Unknown'})
