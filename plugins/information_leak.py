import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    result = ""
    result += git(url) or ""
    result += svn(url) or ""
    if result:
        return result
    else:
        return False

def git(url):
   req = requests.get(url + "/.git", timeout=3, allow_redirects=False)
   if req.status_code == 302:
       return False
   if req.status_code == 200:
        return ".git found in %s" % url
   else:
        return False

def svn(url):
    req = requests.get(url + "/.svn", allow_redirects=False)
    if req.status_code == 302:
        return False
    if req.status_code == 200:
        return ".svn found in %s" % url
    else:
        return False

if __name__ == "__main__":
    print(run("https://www.sise.com.cn"))
