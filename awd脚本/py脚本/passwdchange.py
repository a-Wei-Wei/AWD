import paramiko
import socket
import pandas as pd
import sys
import threading


def userssh_changepwd(hostname,username,old_password,new_password,port=22):
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    try:
        client.connect(hostname=hostname, port=port, username=username, password=old_password)
        # 打开一个Channel并执行命令
        # stdin, stdout, stderr = client.exec_command('touch ./Desktop/1.txt')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
        stdin, stdout, stderr = client.exec_command('passwd') 
        stdin.write(old_password+'\n'+new_password+'\n'+new_password+'\n')
        outinfo, errroinfo = stdout.read(), stderr.read()
        # print(outinfo) #输出信息
        # print(errinfo) #错误信息
        successful = 'updated successfully'
        if successful in str(outinfo):
            print("{}密码修改成功".format(hostname))
        else:
            print("{}密码修改失败".format(hostname))
        # 关闭连接
        client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("{}账号或密码错误".format(hostname))
    except TimeoutError as e:
        print("{}连接超时".format(hostname))
if __name__ == '__main__':
    iplist = []
    username = sys.argv[1]
    old_password = sys.argv[2]
    new_password = sys.argv[3]
    with open("iplist.txt","r") as f:
        lines = f.readlines()
    for line in lines:
        # #print(line.replace("\n",""))
        # iplist.append(line.replace("\n",""))
        hostname = line.replace("\n","")
        t = threading.Thread(target=userssh_changepwd,args=(hostname,username,old_password,new_password))
        # userssh_changepwd(hostname,username,old_password,new_password)
        t.start()
        print("正在修改{}的密码".format(hostname))