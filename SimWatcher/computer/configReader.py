#!/usr/bin/env python
import json
from .computer import computer


class computerArray(object):
    def __init__(self, config_file):
        """
        """
        self.config_file = config_file
        with open(self.config_file) as jsonfile:
            global_config = json.load(jsonfile)

        self.computers = []
        for machine in global_config:
            self.computers.append(computer(global_config[machine]))

    def __iter__(self):
        """
        Make the computerArray object iterable
        """
        return iter(self.computers)
