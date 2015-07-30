# coding: utf-8

""" KFC system deploy.

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
from fabric.api import lcd
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
    """Script deploy."""
    print '--- START DEPLOY ---'
    if not files.exists('deploy'):
        __mkdir('deploy')
    with cd('deploy'):
        if not files.exists('figureskate-judging'):
            __clone(
                'https://github.com/pyohei/figureskate-judging.git',
                submodule=True)
        with cd('figureskate-judging/src'):
            run('git pull')
            sudo('rsync --delete -a -v -r ./ /var/www/web/')
    print '--- FINISH DEPLOY ---'

# Servers
SERVERS = ['web', 'mysql']
VM_NAME = 'devserver'


def setup_devenv():
    uninstall = __chk_uninstall()
    if uninstall:
        raise OSError('You must install below command¥n %s' % (
            '¥n'.join(uninstall)))
    basepath = path.dirname(path.abspath(__file__))
    vmpath = path.join(basepath, VM_NAME)
    __make_base(vmpath)
    try:
        for s in SERVERS:
            __copy_vagrantfile(basepath, vmpath, s)
    except:
        print '[ERROR] setup vagrant'
        shutil.rmtree(vmpath)
        raise OSError(
            'Having Error in your directory')
    try:
        up_servers = []
        for s in SERVERS:
            up_servers.append(s)
            __start_vagrant(vmpath, s)
        with lcd(basepath):
            __provision()
    except Exception as e:
        # vagrant destroy
        print 'ERROR: %s' % e
        for s in up_servers:
            __destroy_vagrant(vmpath, s)
        shutil.rmtree(vmpath)


def __chk_uninstall():
    return []


def __make_base(vmpath):
    if path.exists(vmpath):
        raise OSError(
            'You already have development directory!(%s)' % (VM_NAME))
    os.mkdir(vmpath)


def __copy_vagrantfile(basepath, vmpath, server):
    serverpath = path.join(vmpath, server)
    os.mkdir(serverpath)
    os.chdir(serverpath)

    try:
        vagrantpath = path.join(
            basepath, 'vagrant', server, 'Vagrantfile')
        shutil.copy(vagrantpath, serverpath)
    except:
        print '[ERROR] init vagrant'
        local('vagrant destroy')
        raise


def __start_vagrant(devpath, dirname):
    serverpath = path.join(devpath, dirname)
    os.chdir(serverpath)
    local('vagrant up')


def __provision():
    local('ansible-playbook -i hosts playbook.yml')


def simple_rollback():
    basepath = path.dirname(path.abspath(__file__))
    vmpath = path.join(basepath, VM_NAME)
    for s in SERVERS:
        __destroy_vagrant(vmpath, s)
    shutil.rmtree(vmpath)


def __destroy_vagrant(vmpath, dirname):
    """destory vagrant"""
    u"""[y/N]をできれば自動で挿入したい"""
    serverpath = path.join(vmpath, dirname)
    os.chdir(serverpath)
    local('vagrant destroy')


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
