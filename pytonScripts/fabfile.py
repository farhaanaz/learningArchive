from fabric.api import *

def greetings(msg):
    print("Hello, good {}".format(msg))

def sysinfo():
    print("Disk space.")
    local("df -h")
    
    print("Memory info.")
    local("free -m")

    print("System uptime.")
    local("uptime")

def remoteExec():
    run("hostname")
    run("uptime")
    run("free -m")
    run("df -h")

    sudo("yum install unzip zip wget -y")

def webSetup(WEBURL, DIRNAME):
    print("#########################################")
    print("INSTALLING DEPENDENCIES")
    print("#########################################")
    sudo("yum install httpd wget unzip -y")

    print("#########################################")
    print("Start & enable service.")
    print("#########################################")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("#########################################")
    local("apt install zip unzip -y")

    print("#########################################")
    print("Downloading and pushing website to webservers")
    print("#########################################")
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip -i website.zip")
 
    print("#########################################")
    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)

    with cd("/var/www/html"):
        sudo ("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

    print("WEBSITE SETUP IS DONE")

