#!/usr/bin/env python


class computer(object):
    def __init__(self, config):
        """
        """
        self.name = config['fullname']
        self.address = config['address']
        self.username = config['username']
        self.scheduler = config['scheduler']

    def get_info(self):
        """
        """
        print('Computer name: ', self.name)
        print('Login address: ', self.address)
        print('Username: ', self.username)
        print('Computer scheduler: ', self.scheduler)
        print('-----------------------------')
