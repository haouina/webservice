#!/usr/bin/python2.7

from fabric.api import cd, env, prefix, run, task, prompt, local, get
import platform


env.hosts = ['prod', 'agent']
env.user = "root"
env.roledefs = {
    'Ubuntu': ['prod'],
    'CentOS': ['agent']
    }


@task
def memory_usage():
    run('free -m')


@task
def pull(branch='master', remote='https://github.com/haouina/app.git'):
    with cd('/var/www/html/'):
        run("git pull %s %s" % (remote, branch))


@task
def install(pkg=None):
    if pkg is not None:
        env["pkg"] = pkg
    elif pkg is None and env.get("pkg") is None:
        env["pkg"] = prompt("Which package? ")
    run('apt-get install -y %s' % env["pkg"])


@task
def check():
    run("uptime")
    run("hostname")
    result = run("ls -l /var/www")
    result.failed


@task
def local_tar():
    local("tar -xzvf /root/web.py-0.37.tar.gz -C /root")


@task
def file_get(remote_path, local_path):
    get(remote_path, local_path)


@task
def update_upgrade():
    opsys = run("cat /etc/issue | cut -f1 -d ' ' | head -1")
    if opsys == "Ubuntu":
        run("apt-get update")
        run("apt-get -y upgrade")
    elif opsys == "CentOS":
        run("yum update -y")
    else:
        print "Erreur d'OS"


@task
def install_memcached():
    opsys = run("cat /etc/issue | cut -f1 -d ' ' | head -1")
    if opsys == "Ubuntu":
        run("apt-get install -y memcached")
    elif opsys == "CentOS":
        run("yum install -y memcached")
    else:
        print "Erreur d'OS"


@task
def install_apache_git():
    opsys = run("cat /etc/issue | cut -f1 -d ' ' | head -1")
    if opsys == "Ubuntu":
        run("apt-get install -y apache2 git")
    elif opsys == "CentOS":
        run("yum install -y httpd git")
        with cd("/var/www/html"):
            run("git init")
    else:
        print "Erreur d'OS"


@task
def deploy():
    print 'Starting deployment'
    memory_usage()
    install_apache_git()
    pull()
    local_tar()
    install_memcached()
    check()
    print 'deploy complete!'
