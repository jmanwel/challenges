import datetime
import paramiko
import sys


print("The backup will be performed each " + sys.argv[0] + " days")

t = datetime.datetime.now()

with open('/path/to/file/inventory.csv') as inventory:
    for line in inventory.readlines()[1:]:
        host = line.split(",")[0]
        ip = line.split(",")[1]
        u = line.split(",")[2]
        p = line.split(",")[-1]
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip, 22, u, p)
        stdin, stdout, stderr = ssh_client.exec_command('show configuration')
        with open(f"backups/backup_{host}_{t}.config", "w") as f:
            f.write(stdout.read().decode("UTF-8"))
        ssh_client.close()