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
    archive_count = local("ls -t versions | wc -l", capture=True)
    if number == 0 or number == 1:
        number = 1
    unneccessary_archives = int(archive_count) - number
    if unneccessary_archives > 0:
        local("ls -t versions | tail -n +{} | xargs rm -rf".format(
            unneccessary_archives))
    releases_count = run("ls -t /data/web_static/releases | wc -l")
    unneccessary_releases = int(releases_count) - number
    if unneccessary_releases > 0:
        run("ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf"
            .format(unneccessary_releases))
