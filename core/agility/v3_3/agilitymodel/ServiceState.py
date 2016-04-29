
from core.base.enum import Enum

ServiceState = Enum(**{'Running': 'Running', 'Starting': 'Starting', 'Failed': 'Failed', 'Degraded': 'Degraded', 'Stopping': 'Stopping', 'Stopped': 'Stopped', 'Unprovisioned': 'Unprovisioned'})
