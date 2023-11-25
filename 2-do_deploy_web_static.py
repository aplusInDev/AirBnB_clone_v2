#!/usr/bin/python3

"""Fabric script that distributes an archive to your web servers,
using the function do_deploy."""

from fabric.api import *
from os import path


env.hosts = ['ubntu@54.146.86.128',
             'ubntu@100.26.152.40']

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
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}/web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_ext))
        return True
    except:
        return False