# -*- Coding: utf-8 -*-

"""Creater of api parameter.

"""

import random

__COVER_RATE__ = 0.0001


class Creater(object):

    def __init__(self, parser):
        self.parser = parser
        self.api_params = None
        self.api_count = 0

    def create(self):
        parameter = self.parser.parse()
        api_params = self.__awk_api_param(parameter)
        self.api_count = self.__count_api_pattern(api_params)
        # Write for test..
        n = 0
        param_store = []
        while n < self.api_count:
            api_param = self.__choice_api_param(parameter,
                                                api_params)
            if api_param in param_store:
                print 'Same'
                continue
            param_store.append(api_param)
            n += 1
        return param_store

    def __awk_api_param(self, parameter):
        count_elements = {}
        total_pattern = 1
        for k, v in parameter.items():
            # Including not parameter
            count_elements[k] = len(v['api_values'])
            total_pattern = total_pattern * count_elements[k]
        self.api_count = total_pattern * (__COVER_RATE__ / 100.0)
        return count_elements

    def __count_api_pattern(self, api_params):
        """Count parameter to make for api automation test."""
        # This module is not good for me...
        return self.api_count

    def __choice_api_param(self, parameter, api_params):
        # If you extend, I wnat you to implement list shuffule function.
        api_requests = []
        for k, v in api_params.items():
            choice_no = random.randint(0, v)
            if not choice_no:
                continue
            api_key = parameter[k]['api_key']
            api_value = parameter[k]['api_values'][choice_no-1]
            api_requests.append('{0}={1}'.format(api_key, api_value))
        return '&'.join(api_requests)
