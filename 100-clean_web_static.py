#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy.
"""
from datetime import datetime
from fabric.api import env, put, run, local
from os.path import exists
env.hosts = ['100.25.20.254', '54.144.154.99']


def do_clean(number=0):
    """Cleans up old versions of web_static"""
    number = int(number)
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1
    local("ls -t versions | tail -n +{} | xargs rm -rf".format(number))
    run("ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf".format(
        number))
