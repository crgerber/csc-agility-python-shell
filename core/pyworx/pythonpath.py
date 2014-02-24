'''
Created on Nov 23, 2012

@author: dawood
'''
import os
import sys
CUSTOM_SYSPATH = []

def addPaths(pathlist, basedir=''):
    [addPath(path.strip(), basedir=basedir, index=index) for index, path in enumerate(pathlist)]
    
def addPath(path, basedir='', index=1, absolute=False):
    '''
    adds a absolute(path) or absolute(basedir/path) to python system paths
    
    @param path: path can be relative or absolute, a relative path can be relative to a base dir, or to current working dir
    @param basedir: base directory of a relative path argument, basedir/path will be added to python system path after conversion of basedir into absolute path if necessary
    @param index: list index to insert the new path into
    @param absolute: if true, bypasses absolute path conversion, if basedir is provided, absolute arg is ignored
    '''
    if basedir:
        path = os.path.join(basedir, path)
        absolute = os.path.isabs(basedir)
    else:
        absolute = absolute or os.path.isabs(path)

    fullpath = os.path.realpath(os.path.abspath(path)) if not absolute else os.path.realpath(path)
    if fullpath not in sys.path:
        #For troubleshooting purposes
        CUSTOM_SYSPATH.insert(index, fullpath)
        sys.path.insert(index, fullpath)