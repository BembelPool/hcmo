# -*- coding:utf-8 -*-
# Ein Django-cms Projekt deployen
#

from fabric.api import *

PROJECT = 'creative-cubes'  # Name des django Projekts
TEMPFILE = '/tmp/%s.tgz' % PROJECT

env.hosts = ['django@alice']


def pack():
    local('find -iname "*pyc" -exec rm  {} \;')
    local('cd .. && tar czf %s %s' % (TEMPFILE, PROJECT))
   

def deploy():
    pack()
    put(TEMPFILE, '~/tmp')
    with cd('~/sites'):
        run('tar xzvf ~/tmp/%s.tgz' % PROJECT)
        run('touch %s/deploy/app.wsgi' % PROJECT)