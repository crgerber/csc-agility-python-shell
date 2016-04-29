'''
Created on Oct 26, 2012

@author: dawood
'''
import sys
import collections

from core.agility.v2_0 import methods as v2_0
from core.agility.v3_0 import methods as v3_0
from core.agility.v3_3 import methods as v3_3
from core.agility.v2_0 import agilitymodel as v2_0_model
from core.agility.v3_0 import agilitymodel as v3_0_model
from core.agility.v3_3 import agilitymodel as v3_3_model

current = v3_3

Version = collections.namedtuple('Version', ['v2_0', 'v3_0', 'v3_3', 'current'])
client = Version(v2_0=v2_0, v3_0=v3_0, v3_3=v3_3, current=v3_3)
Model = collections.namedtuple('Model', ['v2_0', 'v3_0', 'v3_3', 'current'])
model = Model(v2_0=v2_0_model, v3_0=v3_0_model, v3_3=v3_3_model, current=v3_3_model)

_activeVersion = 'v3_3'

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

