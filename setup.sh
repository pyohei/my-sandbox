#!/bin/sh

# Initial setup for linux environ.

# This script must run with root user.
# And I'm thinking wheather change user to root in this script or not.

# 2016-08-26 I'm creating simple path

# This scripts is setting up only ansible.
# And you can install other packages from ansible.

# Usage:
#   if you have wget in your terminal,
#      $ wget -O /tmp/setup.sh https://raw.githubusercontent.com/pyohei/linux-devenv/master/setup.sh
#      $ /tmp/setup.sh    

sudo apt-get -y install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get -y update
sudo apt-get -y install ansible

# I wonder if I install git in this source...
sudo apt-get -y install git
