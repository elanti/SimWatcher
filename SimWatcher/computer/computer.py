class computer(object):
    """
    Representation of the HPC machines used for the simulations

    This class collects several information about the different HPC machines.
    """
    def __init__(self, config):
        self.name = config['fullname']
        self.address = config['address']
        self.username = config['username']
        self.scheduler = config['scheduler']
        self.need_ssh_tunnel = config['need_ssh_tunnel']

    def get_info(self):
        """
        Print information about computer instance
        """
        print('Computer name      : ', self.name)
        print('Login address      : ', self.address)
        print('Username           : ', self.username)
        print('Computer scheduler : ', self.scheduler)
        print('Need ssh tunnel    : ', self.need_ssh_tunnel)
        print('--------------------')


if __name__ == '__main__':
    print('In main...')
    config = {'fullname': 'Piz Daint',
              'address': 'daint.cscs.ch',
              'username': 'lanti',
              'scheduler': 'SLURM',
              'need_ssh_tunnel': True}

    daint = computer(config)
    daint.get_info()
