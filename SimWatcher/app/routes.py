from flask import render_template, request
from SimWatcher.app import app
from SimWatcher.ssh import client
from SimWatcher.computer import configReader

config_file = 'computer/computer_config.json'
computers = configReader.computerArray(config_file)
computer_names = [comp.name for comp in computers]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/my_simulations', methods=('GET', 'POST'))
def my_simulations():
    if request.method == 'POST':
        simulations = get_list_simulation()
    else:
        simulations = []*len(computer_names)

    return render_template(
        'my_simulations.html',
        simulations=simulations,
        computers=computer_names,
    )


def get_list_simulation():
    ssh_clients = []
    for computer in computers:
        computer.get_info()
        ssh_clients.append(client.sshClient(computer))

    simulations_txt = []
    for ind, ssh_client in enumerate(ssh_clients):
        command = "squeue -u {} -o '%.18i %.25j %.2t %.10M'".format(computers[ind].username)
        output = ssh_client.sendCommand(command)
        simulations_txt.append(output['stdout'][1:])

    simulations = []
    for runs in simulations_txt:
        if len(runs) == 0:
            simulations.append([])
        else:
            sims = []
            for entry in runs:
                sims.append(entry.split())
            simulations.append(sims)

    return simulations
