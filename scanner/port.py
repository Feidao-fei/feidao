#!/usr/local/python3.6.3/bin/python3.6
# coding = utf-8

import socket
import datetime
import re
from concurrent.futures import ThreadPoolExecutor, wait
import sys
import os

DEBUG = False

# 判断ip地址输入是否符合规范
def check_ip(ipAddr):
    compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False
# 扫描端口程序
def portscan(ip, port, dir):
    try:
        s = socket.socket()
        s.settimeout(0.2)
        s.connect((ip, port))
        with open(dir+'/'+"--端口.txt", 'a') as f:
            f.write(str(ip)+":"+str(port)+'\n')
        openstr = f'[+] {ip} port:{port} open'
        sys.stdout.write(openstr + '\n')
    except Exception as e:
        if DEBUG is True:
            print(ip + str(port) + str(e))
        else:
            return sys.stdout.write(openstr + '\n')
    finally:
        s.close
#主程序,利用ThreadPoolExecutor创建800个线程同时扫描端口
def run(ip):
    print('[*]使用扫描端口模块.................')
    if "http://" in ip or "https://" in ip:
        ip = ip[ip.find('://') + 3:]
        print("[*]正在分析网站服务器IP")
    try:
        domain_name = ip
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data\\" + domain_name)
        if os.path.isdir(dir):
            pass
        else:
            os.mkdir(dir)
        server_ip = socket.gethostbyname(str(ip))
        print("[*]服务器IP为%s" % server_ip)
        ip = server_ip
    except Exception as e:
        print("[!]服务器IP获取失败")
        pass
    if check_ip(ip):
        start_time = datetime.datetime.now()
        if os.path.isfile(dir+'/'+"--端口.txt"):
            os.remove(dir+'/'+"--端口.txt")
        executor = ThreadPoolExecutor(max_workers=600)
        t = [executor.submit(portscan, ip, n, dir) for n in range(1, 65536)]
        if wait(t, return_when='ALL_COMPLETED'):
            end_time = datetime.datetime.now()
            print("[*]扫描完成,用时:", str((end_time - start_time).seconds)+'s')
if __name__ == '__main__':
    run('https://www.sise.com.cn')
