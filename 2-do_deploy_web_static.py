#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from os import path
from fabric.api import env, run, put, local
from datetime import datetime

env.hosts = ['54.236.45.68', '100.25.102.49']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(filename))
    if os.path.exists(filename):
        return filename
    else:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    using the function do_deploy
    Args:
        archive_path (str): The path of the archive
    """

    if path.exists(archive_path):

        archive = archive_path.split('/')[1]

        ra_path = "/tmp/{}".format(archive)
        r_folder = archive.split('.')[0]
        rd_path = "/data/web_static/releases/{}/".format(r_folder)

        put(archive_path, ra_path)

        run("mkdir -p {}".format(rd_path))
        run("tar -xzf {} -C {}".format(ra_path, rd_path))
        run("rm {}".format(ra_path))
        run("mv -f {}web_static/* {}".format(rd_path, rd_path))
        run("rm -rf {}web_static".format(rd_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(rd_path))
        return True
    return False
