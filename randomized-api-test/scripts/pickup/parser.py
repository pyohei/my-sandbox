# -*- Coding: utf-8 -*-

"""Parameter parser.

Parse parameter.
"""


class Parser(object):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def parse(self):
        return self.__parse_locally()

    def __parse_locally(self):
        """Parse locally.

        *ATTENTION*
            This module is not created in generally.
            When you use this, be careful to change this module!
        """
        request_patterns = {}
        canditates = self.params.values()
        for n, parameter in enumerate(canditates):
            detail = self.__parse_detail(parameter)
            request_patterns[n] = detail
        return request_patterns

    def __parse_detail(self, parameter):
        """Parse each parameter.

        *ATTENTION*
            This module is not created in generally.
            When you use this, be careful to change this module!
        """
        # Below is temporary valueables.
        key_name = 'o_name'
        choice_name = 'c_names'
        min_name = 'min_num'
        max_name = 'max_num'
        api_param = {}
        if key_name not in parameter:
            raise KeyError('Not api parameter key.')
        api_param['api_key'] = parameter[key_name]
        if choice_name in parameter:
            api_param['api_values'] = parameter[choice_name]
            return api_param
        if min_name not in parameter:
            raise KeyError('Not api parameter min_name.')
        if max_name not in parameter:
            raise KeyError('Not api parameter max_name.')
        # ******** CHANGE **********
        # You may change to accept float type
        # **************************
        min_num = int(parameter[min_name])
        max_num = int(parameter[max_name])
        api_param['api_values'] = [min_num-1,
                                   min_num,
                                   (min_num+max_num)/2,
                                   max_num,
                                   max_num+1]
        return api_param
