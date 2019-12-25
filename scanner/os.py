from nmap import PortScanner
import socket
def run(target):

    print('[*]使用系统识别扫描模块.................')
    print('[*]温馨提示如果对方挂了CDN就很难识别真正的服务器的操作系统.......')
    if "http://" in target or "https://" in target:
        ip = target[target.find('://') + 3:]
        print("[*]正在分析网站服务器IP")
    try:
        server_ip = socket.gethostbyname(str(ip))
        print("[*]服务器IP为%s" % server_ip)
        ip = server_ip
    except Exception as e:
        print("[!]服务器IP获取失败")
        pass

    print('')
    nm = PortScanner()
    nm.scan(ip, arguments="-sS -O -vv -n -T4 -p 80,22,443")
    if "osmatch" in nm[ip]:
        for osmatch in nm[ip]['osmatch']:
            print('[*]操作系统: {0}'.format(osmatch['name']))
            print('[*]识别准确度: {0}'.format(osmatch['accuracy']))
            print('')
            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    print('[*]osClass.type: {0}'.format(osclass['type']))
                    print('[*]osClass.vendor: {0}'.format(osclass['vendor']))
                    print('[*]osClass.osfamily: {0}'.format(osclass['osfamily']))
                    print('[*]osClass.osgen: {0}'.format(osclass['osfamily']))
                    print('[*]osClass.accuracy: {0}'.format(osclass['accuracy']))
                    print('')
    return
if __name__ == '__main__':
    run('https://www.qq.com')