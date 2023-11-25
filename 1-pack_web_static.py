from fabric.api import *

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    of AirBnB Clone repo, using the function do_pack."""
    from datetime import datetime
    from os.path import getsize
    from os import path
    now = datetime.now()
    file_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(file_name))
    size = getsize("versions/{}".format(file_name))
    print("web_static packed: versions/{} -> {}Bytes".format(file_name, size))
    if path.exists("versions/{}".format(file_name)):
        return "versions/{}".format(file_name)
    else:
        return None