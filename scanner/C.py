import socket
import datetime
import sys
from concurrent.futures import ThreadPoolExecutor, wait
import re
import os
import os.path

DEBUG = False
def check_ip(ipAddr):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1   -9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False

def cDuan(ip, i, dir):
    ip += '{}'.format(i)
    try:
        s = socket.socket()
        s.settimeout(0.2)
        s.connect((ip, 80))
        with open(dir+'/'+"--c段.txt", 'a') as f:
            f.write(ip+'\n')
        openstr = '[+] {} open'.format(ip)
        sys.stdout.write(openstr+'\n')
    except Exception as e:
        if DEBUG is True:
            print(ip + str(e))
        else:
            return sys.stdout.write(openstr+'\n')
    finally:
        s.close
def run(ip):
    new_ip = ''
    print('[*]使用扫描c段模块.................')
    if "http://" in ip or "https://" in ip:
        ip = ip[ip.find('://') + 3:]
        print(ip)
        print("[*]正在分析网站服务器IP")
    try:
        domain_name = ip
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data\\"+domain_name)
        if os.path.isdir(dir):
            pass
        else:
            os.mkdir(dir)
        server_ip = socket.gethostbyname(str(ip))
        print("[*]服务器IP为%s" % server_ip)
        ip = str(server_ip)
        list = ip.split('.')
        for i in list[0:3]:
            new_ip += i + '.'
    except Exception as e:
        print('[!]服务器IP获取失败')
        pass
    if check_ip(new_ip):
        start_time = datetime.datetime.now()
        if os.path.isfile(dir+'/'+"--c段.txt"):
            os.remove(dir+'/'+"--c段.txt")
        executor = ThreadPoolExecutor(max_workers=60)
        t = [executor.submit(cDuan, new_ip, i, dir) for i in range(1, 254)]
        if wait(t, return_when='ALL_COMPLETED'):
            end_time = datetime.datetime.now()
            print('\n')
            print("[*]扫描完成,用时:", str((end_time - start_time).seconds)+'s')
if __name__ == '__main__':
    run('172.16.2.81')