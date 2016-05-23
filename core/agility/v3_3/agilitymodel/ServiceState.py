
from core.base.enum import Enum

ServiceState = Enum(**{'Starting': 'Starting', 'Stopping': 'Stopping', 'Failed': 'Failed', 'Unprovisioned': 'Unprovisioned', 'Degraded': 'Degraded', 'Running': 'Running', 'Stopped': 'Stopped'})
