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

# Servers
SERVERS = ['web', 'mysql']
VM_NAME = 'devserver'

def setup_devenv():
    basepath = path.dirname(path.abspath(__file__))
    vmpath = path.join(basepath, VM_NAME)
    __make_base(vmpath)
    # 
    try:
        for s in SERVERS:
            __init_vagrant(
            __make_directory(devpath, s)
    except:
        shutil.rmtree(basepath)
        raise OSError(
                'Having Error in your directory')
    try:
        up_servers = []
        for s in SERVERS:
            __start_vagrant(devpath, s)
            up_servers.append(s)
    except Exception as e:
        # vagrant destroy
        print 'ERROR: %s' % e
        for s in up_servers:
            __rollback(s)
        shutil.rmtree(basepath)

def __make_base(vmpath):
    if path.exists(vmpath):
        raise OSError(
                'You already have development directory!(%s)' % (VM_NAME))
    os.mkdir(vmpath)

def __make_directory(devpath, dirname):
    filepath = path.dirname(path.abspath(__file__))
    devpath = path.join(filepath, 'devserver')
    serverpath = path.join(devpath, dirname)
    os.mkdir(serverpath)
    init_vagrant(devpath, dirname)
    vagrantfilepath = path.join(
        filepath, 'vagrant', dirname, 'Vagrantfile')
    shutil.copy(vagrantfilepath, serverpath)

def __init_vagrant(basepath, vmpath, server):
    try:
        serverpath = path.join(vmpath, server)
        os.mkdir(serverpath)

        vagrantpath = path.join(
            basepath, 'vagrant', server, 'Vagrantfile')
        
        shutil.copy(vagrantpath, serverpath)

        os.chdir(serverpath)
    except:
        pass

    local('vagrant init')

def __start_vagrant(devpath, dirname):
    """
    serverpath = path.join(devpath, dirname)
    os.chdir(serverpath)
    local('vagrant up')
    """
    pass

def __rollback(dirname):
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
