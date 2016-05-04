
from core.base.enum import Enum

ImportMode = Enum(**{'CreateOrUpdate': 'CreateOrUpdate', 'Create': 'Create', 'Sync': 'Sync', 'Update': 'Update', 'Lookup': 'Lookup', 'Delete': 'Delete'})
