
from core.base.enum import Enum

State = Enum(**{'Unknown': 'Unknown', 'Starting': 'Starting', 'Stopping': 'Stopping', 'Failed': 'Failed', 'Paused': 'Paused', 'Degraded': 'Degraded', 'Running': 'Running', 'Stopped': 'Stopped', 'Destroyed': 'Destroyed'})
