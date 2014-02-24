'''
Created on Nov 15, 2012

@author: dawood
'''
import os
import stat
from core.plugin import AgilityShellHook
from ssh2 import Connection as sshConnection

class SSH(AgilityShellHook):
    def __init__(self, agility):
        AgilityShellHook.__init__(self, agility)

    def executeBashScript(self, computeId, scriptBody, usePublicAddress=True, useSSHKey=False):
        #@todo: add timeout to sshConnection
        TYPE_SSH = 'SSH'
        TYPE_USERPASS = 'Username/Password'
        compute = self._agility.compute.getInstance(computeId)
        credentials = [compute.credential] if not isinstance(compute.credential, list) else compute.credential
            
        #getCredential returns the ssh-keys, while getCredentials2 returns the password
        credentialList = [self._agility.credential.getCredential(credential.id) for credential in credentials]
        credentialPassList = [self._agility.credential.getCredential2(credential.id) for credential in credentialList if (credential.credentialType == TYPE_USERPASS)]
        selectedCredentialList = filter(lambda cred: cred.credentialType == TYPE_SSH, credentialList) if useSSHKey else credentialPassList
        
        selectedCredential = selectedCredentialList.pop()
        netAddress = compute.publicAddress if usePublicAddress else compute.privateAddress
        keyFileName = None
        password = None
        if useSSHKey: 
            keyFileName = '%s.key'%netAddress
            with open(keyFileName, 'w') as keyFile:
                keyFile.write(selectedCredential.privateKey)
                os.chmod(keyFileName, stat.S_IRUSR | stat.S_IWUSR)
        else:
            username = selectedCredential.name
            password = selectedCredential.privateKey        
        
        sshConn = sshConnection(netAddress, username=username, password=password, private_key=keyFileName)
        _stdout = sshConn.execute(scriptBody)
        return _stdout
    
    
    def getSSHConnection(self, host, username, password=None, keyFile=None):
        myssh = sshConnection(host=host, username=username, password=password, private_key=keyFile)
    #    myssh.put('ssh.py')
    #    myssh.close()    
        return myssh