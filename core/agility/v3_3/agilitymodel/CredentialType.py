
from core.base.enum import Enum

CredentialType = Enum(**{'Certificate with Private Key': 'Certificate with Private Key', 'Username/Password': 'Username/Password', 'Encrypt/Decrypt': 'Encrypt/Decrypt', 'Certificate/PK': 'Certificate/PK', 'SSH': 'SSH'})
