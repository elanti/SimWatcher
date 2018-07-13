import os
import paramiko
import computer


class sshClient(object):
    def __init__(self, computer):
        self.client = paramiko.SSHClient()
        self.client._policy = paramiko.WarningPolicy()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.config = {}
        if computer.need_ssh_tunnel:
            ssh_config = paramiko.SSHConfig()
            user_config_file = os.path.expanduser("~/.ssh/config")
            if os.path.exists(user_config_file):
                with open(user_config_file) as f:
                    ssh_config.parse(f)

                user_config = ssh_config.lookup(computer.address)
                for key in ('hostname', 'username'):
                    if key in user_config:
                        self.config[key] = user_config[key]

                self.config['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])
        else:
            self.config['hostname'] = computer.address
            self.config['username'] = computer.username

    def sendCommand(self, command):
        output = {'stdout': [],
                  'stderr': []}

        self.client.connect(**self.config)
        stdin, stdout, stderr = self.client.exec_command(command)
        for line in stdout.readlines():
            output['stdout'].append(line)
        for line in stderr.readlines():
            output['stderr'].append(line)
        self.client.close()
        return output
