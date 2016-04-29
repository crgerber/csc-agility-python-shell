
from core.base.enum import Enum

State = Enum(**{'Failed': 'Failed', 'Destroyed': 'Destroyed', 'Paused': 'Paused', 'Unknown': 'Unknown', 'Running': 'Running', 'Degraded': 'Degraded', 'Stopping': 'Stopping', 'Stopped': 'Stopped', 'Starting': 'Starting'})
