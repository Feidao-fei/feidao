#首先我们要导入requests模块和bs4模块里的BeautifulSoup和time模块
import requests
import time
import os
import re
from lxml import html
etree = html.etree


#设置好开始时间点
strat=time.time()

class G:
    rb1=None
    rb2=None
    rb3=None
def chax(lid):
    #设置浏览器头过反爬
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    #设置好url

    urldomain = "http://site.ip138.com/{}/domain.htm".format(lid)
    url2 = "http://site.ip138.com/{}/beian.htm".format(lid)
    url3 = "http://site.ip138.com/{}/whois.htm".format(lid)
    #打开网页
    G.rb1 = requests.get(urldomain, headers=head)
    G.rb2 = requests.get(url2, headers=head)
    G.rb3 = requests.get(url3, headers=head)

def run(ip):
    result = re.match(r'https://www|http://www', ip)
    if result == None:
        print("[*]请输入以\'https://www\'或者\'http://www\'开头的格式")
        return
    name = ip
    name = name[name.find('://') + 3:]
    dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data\\" + name)
    try:
        if os.path.isdir(dir):
            pass
        else:
            os.mkdir(dir)
    except Exception as e:
        pass
    print('[*]使用扫描whois模块.................')
    if "http://" in ip or "https://" in ip:
        ip = ip[ip.find('://') + 7:]
        chax(ip)
    gf2 = etree.HTML(G.rb2.content.decode())
    gf2_result = gf2.xpath("//div[@class='panels']//p/text()")[0].strip()
    print('[*]备案信息结果:'+gf2_result)

    gf3 = etree.HTML(G.rb3.content.decode())
    gf3_reuslt = gf3.xpath("//div[@class='whois']//p/text()")
    print('[*]whois查询结果:')
    for i in gf3_reuslt:
        print(i)

    gf1 = etree.HTML(G.rb1.content.decode())
    gf1_result = gf1.xpath("//div[@class='panel']//p/a/text()")

    if os.path.isfile(dir + '/' + "--子域名.txt"):
        os.remove(dir + '/' + "--子域名.txt")
    print('[*]子域名查询结果:')
    for i in gf1_result:
        with open(dir + '/' + "--子域名.txt", 'a') as f:
            f.write(i + '\n')
        print(i)
    end=time.time()
    print('[*]查询耗时:', end-strat)
if __name__ == '__main__':
    run('https://www.sise.com.cn')
