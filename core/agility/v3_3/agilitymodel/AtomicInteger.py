from core.agility.v3_3.agilitymodel.base.AtomicInteger import AtomicIntegerBase
from core.agility.v3_3.agilitymodel.actions.AtomicInteger import AtomicIntegerActions

class AtomicInteger(AtomicIntegerBase, AtomicIntegerActions):
    '''
    classdocs
    '''
    def __init__(self, base=None, maxatomicvalue=None, uppercase=None, width=None, allowwrap=None, pkey=None, value=None, minatomicvalue=None):
        '''
        Constructor
        @param base: base minOccurs=0
        @type base: byte
        @param maxatomicvalue: maxatomicvalue minOccurs=0
        @type maxatomicvalue: long
        @param uppercase: uppercase minOccurs=0
        @type uppercase: boolean
        @param width: width minOccurs=0
        @type width: byte
        @param allowwrap: allowwrap minOccurs=0
        @type allowwrap: boolean
        @param pkey: pkey minOccurs=0
        @type pkey: string
        @param value: value minOccurs=0
        @type value: string
        @param minatomicvalue: minatomicvalue minOccurs=0
        @type minatomicvalue: long
        '''
        AtomicIntegerBase.__init__(self, base=base, maxatomicvalue=maxatomicvalue, uppercase=uppercase, width=width, allowwrap=allowwrap, pkey=pkey, value=value, minatomicvalue=minatomicvalue)
