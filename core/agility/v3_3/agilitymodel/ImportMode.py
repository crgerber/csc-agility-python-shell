
from core.base.enum import Enum

ImportMode = Enum(**{'CreateOrUpdate': 'CreateOrUpdate', 'Lookup': 'Lookup', 'Create': 'Create', 'Sync': 'Sync', 'Update': 'Update', 'Delete': 'Delete'})
