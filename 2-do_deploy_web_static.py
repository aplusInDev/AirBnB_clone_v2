#!/usr/bin/python3

"""Fabric script that distributes an archive to your web servers,
using the function do_deploy."""

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'
env.hosts = ['ubuntu@54.146.86.128',
             'ubuntu@100.26.152.40']

def do_deploy(archive_path):
    """distributes an archive to your web servers,
    using the function do_deploy."""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/" + file_name_no_ext
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_no_ext))
        run("rm -r /tmp/{}".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(path_no_ext))
        return True
    except:
        return False