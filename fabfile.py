# -*- coding:utf-8 -*-
# Ein Django-cms Projekt deployen
#

from fabric.api import *

PROJECT = 'hcmo'  # Name des django Projekts
TEMPFILE = '/tmp/%s.zip' % PROJECT

env.hosts = ['django@alice']

def pack():
    local('find -iname "*pyc" -exec rm  {} \;')
    local('git archive --format=zip -9 --prefix=%s/ -o %s HEAD' % (PROJECT, TEMPFILE))
   
 
def deploy():
    pack()
    put(TEMPFILE, '~/tmp/')
    with cd('~/sites'):
        run('rm -rf %s/' %  PROJECT)
        run('unzip ../tmp/%s.zip ' %  PROJECT)
        run('touch %s/deploy/hcmo.wsgi' % PROJECT)
    

def restart_wsgi():
    run('touch %s/deploy/hcmo.wsgi' % PROJECT)