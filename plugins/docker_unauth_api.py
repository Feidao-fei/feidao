import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    """Docker Remote API unauth"""
    url = url + ":2375/info"
    req = requests.get(url, timeout=3)
    if "Containers" in req.text:
        print(req.text)
        return "Docker Remote API unauth Vulnerable"
    else:
        return False