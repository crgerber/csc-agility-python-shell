
from core.base.enum import Enum

AddressOperation = Enum(**{'getAvailableAddresses': 'getAvailableAddresses', 'reserveAddress': 'reserveAddress', 'unreserveAddress': 'unreserveAddress', 'removeAddress': 'removeAddress', 'allocateAddress': 'allocateAddress', 'releaseAddress': 'releaseAddress', 'removeAddressIfAvailable': 'removeAddressIfAvailable', 'acquireAddressIfAvailable': 'acquireAddressIfAvailable', 'assignAddress': 'assignAddress'})
