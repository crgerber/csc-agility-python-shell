'''
Created on Oct 26, 2012

@author: dawood
'''
import sys
import collections

import v2_0.methods as v2_0
import v3_0.methods as v3_0
import v2_0.agilitymodel as v2_0_model
import v3_0.agilitymodel as v3_0_model


current = v3_0

Version = collections.namedtuple('Version', ['v2_0', 'v3_0', 'current'])
client = Version(v2_0=v2_0, v3_0=v3_0, current=v3_0)
Model = collections.namedtuple('Model', ['v2_0', 'v3_0', 'current'])
model = Model(v2_0=v2_0_model, v3_0=v3_0_model, current=v3_0_model)
_activeVersion = 'v3_0'

def setAPIVersion(apiversion):
    this = sys.modules[__name__]
    _apiversion = apiversion.replace('.', '_')
    if hasattr(this.client, _apiversion):
        this._activeVersion = _apiversion
    else:
        raise ValueError('Invalid API Version: [%s]'%apiversion)

def getClient(apiversion=None):
    this = sys.modules[__name__]
    return getattr(this.client, apiversion.replace('.', '_') if apiversion else this._activeVersion)

def getModel(apiversion=None):
    this = sys.modules[__name__]
    return getattr(this.model, apiversion.replace('.', '_') if apiversion else this._activeVersion)

LOGGER_NAME = 'agility-client'

