#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy.
"""
from datetime import datetime
from fabric.api import env, put, run, local
from os.path import exists
env.hosts = ['100.25.20.254', '54.144.154.99']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    of AirBnB Clone repo, using the function do_pack."""

    now = datetime.now()
    file_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    if not exists("versions"):
        local("mkdir -p versions")

    local("tar -cvzf versions/{} web_static".format(file_name))
    if exists("versions/{}".format(file_name)):
        return "versions/{}".format(file_name)
    else:
        return None


def do_deploy(archive_path):
    """Function to deploy"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        folder_path = "/data/web_static/releases/" + archive_path[9:-4]
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}/".format(
            archive_path[9:], folder_path))
        run("rm /tmp/{}".format(archive_path[9:]))
        run("mv {}/web_static/* {}/".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        return True
    except Exception:
        return False


file = do_pack()


def deploy():
    """Function to deploy"""
    if file is None:
        return False
    return do_deploy(file)
