#web信息收集模块只针对外网，调用的是whatweb API接口
import requests
import zlib
import json
from colorama import Fore
requests.packages.urllib3.disable_warnings()

def whatweb(url):
    response = requests.get(url, verify=False)
    #上面的代码可以随意发挥,只要获取到response即可
    #下面的代码您无需改变，直接使用即可
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

def run(url):
    print('[*]加载web信息识别模块...........')
    request = whatweb(url)
    num = request.headers["X-RateLimit-Remaining"]
    request = request.json()
    print(Fore.CYAN+"[*]'"+url+"'结果:..........")
    for i, j in request.items():
        print('[*]' + i, j)

if __name__ == '__main__':
    run("https://aliyun.bugscaner.com")