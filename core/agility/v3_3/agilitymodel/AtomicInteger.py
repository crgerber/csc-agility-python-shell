from core.agility.v3_3.agilitymodel.base.AtomicInteger import AtomicIntegerBase
from core.agility.v3_3.agilitymodel.actions.AtomicInteger import AtomicIntegerActions

class AtomicInteger(AtomicIntegerBase, AtomicIntegerActions):
    '''
    classdocs
    '''
    def __init__(self, width=None, value=None, maxatomicvalue=None, pkey=None, minatomicvalue=None, uppercase=None, allowwrap=None, base=None):
        '''
        Constructor
        @param width: width minOccurs=0
        @type width: byte
        @param value: value minOccurs=0
        @type value: string
        @param maxatomicvalue: maxatomicvalue minOccurs=0
        @type maxatomicvalue: long
        @param pkey: pkey minOccurs=0
        @type pkey: string
        @param minatomicvalue: minatomicvalue minOccurs=0
        @type minatomicvalue: long
        @param uppercase: uppercase minOccurs=0
        @type uppercase: boolean
        @param allowwrap: allowwrap minOccurs=0
        @type allowwrap: boolean
        @param base: base minOccurs=0
        @type base: byte
        '''
        AtomicIntegerBase.__init__(self, width=width, value=value, maxatomicvalue=maxatomicvalue, pkey=pkey, minatomicvalue=minatomicvalue, uppercase=uppercase, allowwrap=allowwrap, base=base)
