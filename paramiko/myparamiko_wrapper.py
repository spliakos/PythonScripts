#!/usr/bin/python

from StringIO import StringIO
import paramiko
import getpass

class SshClient:
    "A wrapper of paramiko.SSHClient"
    TIMEOUT = 4

    def __init__(self, host, port, username, password, key=None, passphrase=None):
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key is not None:
            key = paramiko.RSAKey.from_private_key(StringIO(key), password=passphrase)
        self.client.connect(host, port, username=username, password=password, pkey=key, timeout=self.TIMEOUT)

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute(self, command, sudo=False):
        feed_password = False
        if sudo and self.username != "root":
            command = "sudo -S -p '' %s" % command
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}

if __name__ == "__main__":
    user = "spliakos"
    passwd = getpass.getpass("Password for %s: " % user)
    command = raw_input("Please enter command that you would like to run. Do not include sudo in the command: ")

    with open('server_list') as f:
       content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    for server in content:
       client = SshClient(host=server, port=22, username=user, password=passwd)
       try:
          print "Executing command at %s\n" % server
          ret = client.execute(command, sudo=True)
          print "  ".join(ret["out"]), "  E ".join(ret["err"]), ret["retval"]
       finally:
          client.close()

