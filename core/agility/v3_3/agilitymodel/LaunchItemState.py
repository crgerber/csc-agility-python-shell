
from core.base.enum import Enum

LaunchItemState = Enum(**{'Starting': 'Starting', 'Ordered': 'Ordered', 'Stopping': 'Stopping', 'OrderProvisioning': 'OrderProvisioning', 'DeployPending': 'DeployPending', 'Degraded': 'Degraded', 'Deploying': 'Deploying', 'Running': 'Running', 'Deployed': 'Deployed', 'OrderPending': 'OrderPending', 'Unknown': 'Unknown', 'Released': 'Released', 'Rejected': 'Rejected', 'Failed': 'Failed', 'Paused': 'Paused', 'Unprovisioned': 'Unprovisioned', 'OrderFailed': 'OrderFailed', 'Deleting': 'Deleting', 'DeployFailed': 'DeployFailed', 'Stopped': 'Stopped'})
