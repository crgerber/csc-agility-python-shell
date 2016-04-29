
from core.base.enum import Enum

CredentialType = Enum(**{'SSH': 'SSH', 'Certificate with Private Key': 'Certificate with Private Key', 'Encrypt/Decrypt': 'Encrypt/Decrypt', 'Username/Password': 'Username/Password', 'Certificate/PK': 'Certificate/PK'})
