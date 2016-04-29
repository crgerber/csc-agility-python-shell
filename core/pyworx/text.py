'''
Created on Dec 5, 2012

@author: dawood
'''
import re
import string
import builtins as builtin

printable = set(string.printable)
letters = set(string.ascii_letters)
re_letters = '[a-zA-Z]'
digits = set(string.digits)
re_digits = '[0-9]'
initials = set(letters)
initials.add('_')
allowed = initials.union(digits)
re_allowed = '%s|%s|%s'%(re_letters, re_digits, '_')
illegal = printable.difference(allowed)

validSymbol = lambda txt, prefix='': re.sub('^[\W|\d]|\W+?', '_', prefix + txt)
isValidSymbol = lambda txt: re.match('^\W|.*\W+.*', txt) is None

python_keywords = set(['and', 'del', 'from','not', 'while',
'as', 'elif', 'global', 'or', 'with',
'assert', 'else', 'if', 'pass', 'yield',
'break', 'except', 'import', 'print',
'class', 'exec', 'in', 'raise',
'continue', 'finally', 'is', 'return',
'def', 'for', 'lambda', 'try'])

privateFilter = lambda name: not name.startswith('_')
callableFilter = lambda attr: not hasattr(attr, '__call__')
python_builtin = set(filter(callableFilter, list(filter(privateFilter, dir(builtin)))))

isValidPythonSymbol = lambda txt, execludeBuiltin=True: isValidSymbol(txt) and txt not in (python_keywords.union(python_builtin if execludeBuiltin else set()))
validPythonSymbol = lambda txt, execludeBuiltin=True: txt if isValidPythonSymbol(txt, execludeBuiltin) else validSymbol(txt) if isValidPythonSymbol(validSymbol(txt), execludeBuiltin) else  validSymbol(txt) + '_'