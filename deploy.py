from fabric.api import cd, env, prefix, run, task, prompt, local, get

env.hosts = ['prod']
env.user   = "root"


@task
def memory_usage():
    run('free -m')


@task
def deploy():
    with cd('/var/www/html/'):
            run('git pull https://github.com/haouina/app.git')


@task
def install(pkg=None):
    if pkg is not None:
        env["pkg"] = pkg
    elif pkg is None and env.get("pkg") is None:
        env["pkg"] = prompt("Which package? ")
    run('apt-get install -y %s' % env["pkg"])


@task
def check():
    run("mkdir /tmp/trunk/")
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
    run("aptitude    update")
    run("aptitude -y upgrade")

@task
def install_memcached():
    run("aptitude install -y memcached")


@task
def update_install():
    update_upgrade()
    install_memcached()
