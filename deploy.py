from fabric.api import cd, env, prefix, run, task, prompt

env.hosts = ['prod']


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
