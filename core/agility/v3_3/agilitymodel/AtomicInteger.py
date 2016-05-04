from base.AtomicInteger import AtomicIntegerBase
from actions.AtomicInteger import AtomicIntegerActions

class AtomicInteger(AtomicIntegerBase, AtomicIntegerActions):
    '''
    classdocs
    '''
    def __init__(self, pkey=None, allowwrap=None, minatomicvalue=None, uppercase=None, value=None, width=None, base=None, maxatomicvalue=None):
        '''
        Constructor
        @param pkey: pkey minOccurs=0
        @type pkey: string
        @param allowwrap: allowwrap minOccurs=0
        @type allowwrap: boolean
        @param minatomicvalue: minatomicvalue minOccurs=0
        @type minatomicvalue: long
        @param uppercase: uppercase minOccurs=0
        @type uppercase: boolean
        @param value: value minOccurs=0
        @type value: string
        @param width: width minOccurs=0
        @type width: byte
        @param base: base minOccurs=0
        @type base: byte
        @param maxatomicvalue: maxatomicvalue minOccurs=0
        @type maxatomicvalue: long
        '''
        AtomicIntegerBase.__init__(self, pkey=pkey, allowwrap=allowwrap, minatomicvalue=minatomicvalue, uppercase=uppercase, value=value, width=width, base=base, maxatomicvalue=maxatomicvalue)
