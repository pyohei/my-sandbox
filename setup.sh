#!/bin/sh

# Initial setup for linux environ.

# This script must run with root user.
# And I'm thinking wheather change user to root in this script or not.

# 2016-08-26 I'm creating simple path

# This scripts is setting up only ansible.
# And you can install other packages from ansible.

# Usage:
#   if you have wget in your terminal,
#      $ wget -O /tmp/setup.sh https://github.com/pyohe/linux-devenv/setup.sh
#      $ /tmp/setup.sh    

sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
