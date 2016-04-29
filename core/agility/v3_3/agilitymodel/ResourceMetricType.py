
from core.base.enum import Enum

ResourceMetricType = Enum(**{'workload': 'workload', 'disk': 'disk', 'memory': 'memory', 'cost': 'cost', 'vcpu': 'vcpu', 'inetaddr': 'inetaddr'})
