
from core.base.enum import Enum

ServiceState = Enum(**{'Failed': 'Failed', 'Running': 'Running', 'Unprovisioned': 'Unprovisioned', 'Stopping': 'Stopping', 'Stopped': 'Stopped', 'Degraded': 'Degraded', 'Starting': 'Starting'})
