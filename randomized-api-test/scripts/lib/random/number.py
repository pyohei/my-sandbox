# -*- Coding: utf-8 -*-

""" Randomize Number

"""

import random


def pick_up(min_num, max_num, decimal_num=0):
    if min_num > max_num:
        raise ValueError('Min number is over max')
    rand_num = random.uniform(min_num, max_num)
    if not rand_num:
        return int(rand_num)
    return round(rand_num, decimal_num)

if __name__ == '__main__':
    print pick_up(1, 3)
    print pick_up(1.2, 3, 4)
