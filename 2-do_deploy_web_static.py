#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy.
"""
from fabric.api import env, put, run
from os.path import exists
env.hosts = ['100.25.20.254', '54.144.154.99']
# env.user = 'ubuntu'
# env.key_filename = '~/.ssh/holberton'
# env.warn_only = True


def do_deploy(archive_path):
    """Function to deploy"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        folder_path = "/data/web_static/releases/" + archive_path[9:-4]
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(
            archive_path[9:-4], folder_path))
        run("rm /tmp/{}".format(archive_path[9:]))
        run("mv {}/web_static/* {}/".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        return True
    except:
        return False
