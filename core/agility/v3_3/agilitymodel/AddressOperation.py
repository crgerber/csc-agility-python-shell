
from core.base.enum import Enum

AddressOperation = Enum(**{'unreserveAddress': 'unreserveAddress', 'allocateAddress': 'allocateAddress', 'getAvailableAddresses': 'getAvailableAddresses', 'acquireAddressIfAvailable': 'acquireAddressIfAvailable', 'removeAddress': 'removeAddress', 'reserveAddress': 'reserveAddress', 'releaseAddress': 'releaseAddress', 'removeAddressIfAvailable': 'removeAddressIfAvailable', 'assignAddress': 'assignAddress'})
