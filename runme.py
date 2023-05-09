__author__ = "Sehran"
__version__ = "1.0"

import os
import subprocess
import platform

root_dir = os.getcwd()
warehouse_frontend = "warehouse_frontend"
warehouse_backend = "warehouse_backend"

git_clone_cmd = "git clone "

java_backend = "https://github.com/SehDev96/warehouse-backend.git"
react_frontend = "https://github.com/SehDev96/warehouse-frontend.git"


def is_docker_daemon_running():
    command = "docker ps -q"
    if platform.system() == 'Darwin':
        output = subprocess.getoutput(command)
        if not output:
            return True
        else:
            return False
    elif platform.system() == 'Linux':
        output = subprocess.getoutput("systemctl is-active docker")
        if output == 'active':
            return True
        else:
            return False
    return False


def code_exists(folder):
    return os.path.exists(root_dir + '/' + folder)


def get_source_code():
    if not code_exists(warehouse_backend):
         os.system(git_clone_cmd + java_backend)
    else:
        print("Java directory already exist!")
        os.chdir(root_dir + '/' + warehouse_backend)
        print("Pulling the latest code")
        os.system("git pull")
        os.chdir(root_dir)

    if not code_exists(warehouse_frontend):
        print("Code does not exists")
        os.system(git_clone_cmd + react_frontend)
    else:
        print("React directory already exists")
        os.chdir(root_dir + '/' + warehouse_frontend)
        print("Pulling the latest code")
        os.system("git pull")
        os.chdir(root_dir)


def run_docker_compose():
    os.system("docker-compose up -d")


def main():
    get_source_code()
    if is_docker_daemon_running():
        run_docker_compose()
        print("Docker containers up and running")
    else:
        print('Docker daemon is not running. Please start docker daemon')


if __name__ == "__main__":
    main()