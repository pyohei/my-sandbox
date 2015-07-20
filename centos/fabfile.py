# coding: cp932

""" KFC system deploy 

Deproyment script.
"""

import os
from os import path
import shutil

from fabric.api import run
from fabric.api import cd
from fabric.api import env
from fabric.api import sudo
from fabric.api import local
from fabric.contrib import files

env.hosts = ['192.168.99.1:49122']
env.user = 'vagrant'
env.password = 'vagrant'

def test():
    print '--- TEST RUN ---'
    try:
        run('cd /tmp')
        run('touch test.txt')
        run('ls -al')
        run('pwd')
        run('git --help')
    except:
        pass
    print '--- TEST EXIT ---'

def deploy():
    print '--- START DEPLOY ---'
    if not files.exists('deploy'):
        __mkdir('deploy')
    with cd('deploy'):
        if not files.exists('figureskate-judging'):
            __clone(
                'https://github.com/pyohei/figureskate-judging.git', submodule=True)
        with cd('figureskate-judging/src'):
            run('git pull')
            sudo('rsync --delete -a -v -r ./ /var/www/web/')
    print '--- FINISH DEPLOY ---'

def setup_devenv():
    servers = ['web', 'mysql']
    filepath = path.dirname(path.abspath(__file__))
    devpath = path.join(filepath, 'devserver')
    if path.exists(devpath):
        raise OSError('You already have development directory!')
    os.mkdir(devpath)

    try:
        for s in servers:
            make_directory(devpath, s)
        for s in servers:
            start_vagrant(devpath, s)
    except Exception as e:
        print e
        for s in servers:
            rollback(s)

def make_base():
    pass

def make_directory(devpath, dirname):
    filepath = path.dirname(path.abspath(__file__))
    devpath = path.join(filepath, 'devserver')
    serverpath = path.join(devpath, dirname)
    os.mkdir(serverpath)
    init_vagrant(devpath, dirname)
    vagrantfilepath = path.join(
        filepath, 'vagrant', dirname, 'Vagrantfile')
    shutil.copy(vagrantfilepath, serverpath)

def init_vagrant(devpath, dirname):
    serverpath = path.join(devpath, dirname)
    os.chdir(serverpath)
    local('vagrant init')

def start_vagrant(devpath, dirname):
    """
    serverpath = path.join(devpath, dirname)
    os.chdir(serverpath)
    local('vagrant up')
    """
    pass

def rollback(dirname):
    print 'rollback %s' % dirname

def __mkdir(path, force=False):
    command = 'mkdir '
    if force:
        command += '-p '
    command += path
    run(command)

def __clone(path, submodule=False):
    command = 'git clone '
    if submodule:
        command += '--recursive '
    command += path
    run(command)
