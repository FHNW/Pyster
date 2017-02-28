from fabric.api import run
from fabric.api import sudo
from fabric.api import cd
from fabric.context_managers import settings

def install_pyster():
    # don't fail, if ius-release is already installed
    with settings(warn_only=True):
        sudo("yum -y install https://centos7.iuscommunity.org/ius-release.rpm")
    sudo("yum -y update")
    sudo("yum -y install python36u git nginx vim-enhanced gcc python36u-devel")
    run("git clone https://github.com/FHNW/Pyster.git")
    # allow proxy connections
    sudo(" /usr/sbin/setsebool -P httpd_can_network_connect 1")
    with cd('Pyster'):
        run('python3.6 -m venv .')
        run('bin/pip install -r requirements.txt')

