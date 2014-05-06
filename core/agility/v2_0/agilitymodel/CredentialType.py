
from core.base.enum import Enum

CredentialType = Enum(**{'Username/Password': 'Username/Password', 'Encrypt/Decrypt': 'Encrypt/Decrypt', 'Certificate with Private Key': 'Certificate with Private Key', 'SSH': 'SSH', 'Certificate/PK': 'Certificate/PK'})
