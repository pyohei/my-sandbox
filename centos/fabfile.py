# coding: cp932

""" KFC system deploy 

"""

from fabric.api import run
from fabric.api import env

env.hosts = ['192.168.99.1:49222']
env.user = 'vagrant'
env.password = 'vagrant'

def test():
    print run('ls /')
