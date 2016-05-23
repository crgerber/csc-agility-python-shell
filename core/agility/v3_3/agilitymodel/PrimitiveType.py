
from core.base.enum import Enum

PrimitiveType = Enum(**{'string': 'string', 'numeric': 'numeric', 'integer': 'integer', 'encrypted': 'encrypted', 'bool': 'bool', 'binary': 'binary', 'date': 'date'})
