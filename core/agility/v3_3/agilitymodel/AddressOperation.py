
from core.base.enum import Enum

AddressOperation = Enum(**{'removeAddressIfAvailable': 'removeAddressIfAvailable', 'removeAddress': 'removeAddress', 'releaseAddress': 'releaseAddress', 'assignAddress': 'assignAddress', 'getAvailableAddresses': 'getAvailableAddresses', 'unreserveAddress': 'unreserveAddress', 'reserveAddress': 'reserveAddress', 'acquireAddressIfAvailable': 'acquireAddressIfAvailable', 'allocateAddress': 'allocateAddress'})
