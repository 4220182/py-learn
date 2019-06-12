"""
基于paramiko模块，不但实现ssh远程执行命令，并且可以实现文件的上传和下载；

安装：
pip3 install paramiko


参考：
https://www.cnblogs.com/python-nameless/p/6855804.html
"""

import paramiko

ssh = paramiko.SSHClient()  #创建SSH对象

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='127.0.0.1', port=22, username='test', password='test')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('touch /tmp/test.log')

# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()
print(result)

#  实现文件的上传和下载
transport = paramiko.Transport(('127.0.0.1',22))
transport.connect(username='test',password='test')
sftp = paramiko.SFTPClient.from_transport(transport)

# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/test.log', '/tmp/test.txt')

# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')
