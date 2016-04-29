
from core.base.enum import Enum

ImportMode = Enum(**{'Delete': 'Delete', 'Create': 'Create', 'Update': 'Update', 'CreateOrUpdate': 'CreateOrUpdate', 'Lookup': 'Lookup', 'Sync': 'Sync'})
