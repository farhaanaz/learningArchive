#!/usr/bin/python3
import os

userlist = ["alpha", "beta", "gamma"]

print("adding users to system")
print("##############################")

#loop to add users from userlist
for user in userlist:
    exitcode = os.system("id {}".format(user) )
    if exitcode !=0:
        print("User {} does not exists. Adding it.".format(user))
        print("##############################")
        print()
        os.system("useradd {}".format(user))
    else:
        print("user already exists") 
        print("##############################")
        print()

# condition to check if group exists or not. add if not exists.
exitcode = os.system("grep science /etc/group")
if exitcode!=0:
    print("Group science does not exist. Adding it")
    print("##################################")
    print()
    os.system("groupadd science")
else:
    print("Group already exists. Skipping it")
    print("##################################")
    print()

for user in userlist:
    print("adding user {} in science group".format(user))
    print("##################################")
    print()
    os.system("usermod -G science {}".format(user))

print("Adding directory")
print("##################################")
print()

if os.path.isdir("/opt/science_dir"):
    print("Directory already exists. Skipping it")
else:
    os.mkdir("/opt/science_dir")

print("Assigning permissions and ownership to the directory.")
print("##################################")
print()
os.system("chown :science /opt/science_dir")

os.system("chmod 770 /opt/science_dir")
