

import paramiko

ssh = paramiko.SSHClient() # 22
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('xxx.xx.xx.xx', 54321, 'Alex', 'xxxxx!')

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read().decode("utf-8"))
ssh.close();

