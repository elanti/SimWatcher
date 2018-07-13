from ssh import client
from computer import configReader

config_file = 'computer/computer_config.json'
computers = configReader.computerArray(config_file)

ssh_clients = []
for computer in computers:
    computer.get_info()
    ssh_clients.append(client.sshClient(computer))

for ssh_client in ssh_clients:
    output = ssh_client.sendCommand('squeue -u {}'.format(computer.username))
    print(output['stdout'])
