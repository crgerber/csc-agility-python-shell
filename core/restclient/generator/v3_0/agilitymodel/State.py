
from core.base.enum import Enum

State = Enum(**{'Destroyed': 'Destroyed', 'Unknown': 'Unknown', 'Paused': 'Paused', 'Failed': 'Failed', 'Running': 'Running', 'Stopped': 'Stopped', 'Stopping': 'Stopping', 'Degraded': 'Degraded', 'Starting': 'Starting'})
