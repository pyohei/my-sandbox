#!/bin/sh
#
# Initial setup for linux(ubuntu mate) environ.
# You can initial set up from this script.
# This scripts is setting up only ansible and git.
# You can use from `Usage`, and you enter your sudo password.
# After you setup your command, you can install from `ansible` command.
# Please detail from README.
#
# Usage:
#   if you have wget in your terminal,
#      $ wget -O /tmp/setup.sh https://raw.githubusercontent.com/pyohei/linux-devenv/master/setup.sh
#      $ /tmp/setup.sh    
#   After you finish install, you can use `git` command, and you command below command.
#      $ git clone https://github.com/pyohei/linux-devenv.git
#   And you can set up your linux(ubunt mate) environment from README.md
#
# Note:
#   2016-08-26 I'm creating simple path

sudo apt-get -y install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get -y update
sudo apt-get -y install ansible

# I wonder if I install git in this source...
sudo apt-get -y install git
