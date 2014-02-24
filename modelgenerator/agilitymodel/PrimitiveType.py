
from core.base.enum import Enum

PrimitiveType = Enum(**{'binary': 'binary', 'string': 'string', 'encrypted': 'encrypted', 'numeric': 'numeric', 'bool': 'bool', 'date': 'date', 'integer': 'integer'})
