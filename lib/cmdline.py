import sys
import argparse


def cmdLineParser():
    #创建一个解析对象,description -help时显示的开始文字
    parser = argparse.ArgumentParser(description='feidao.version1.0',
                                     usage='python feidao.py')
    target = parser.add_argument_group("Target")
    target.add_argument("-u", metavar="URL", dest="target", type=str, default='',
                        help="target url. such as: python feidao.py -u https://www.baidu.com")

    module = parser.add_argument_group("Module")
    module.add_argument("-m", metavar="Module", dest="module", type=str, default='',
                        help="poc to be loaded. defaul is all. also you can scanner one. such as python -u https://www.sise.com.cn -m thinkphp")
    scanner = parser.add_argument_group("Scanner")
    scanner.add_argument("-s", metavar="Scanner", dest='scanner', type=str, default='',
                         help='''
                              scanner and acquisition of information.-s c , -s port, -s whois, -s os, -s web, -s all(scan c,whois,port,os)
                                  example:python -u https://www.sise.com.cn -s c
                              ''')
    exp = parser.add_argument_group("Exp")
    exp.add_argument('-e', metavar="Exp", dest='exp', type=str, default='',
                     help="use exp to exploit.example:python -u https://www.sise.com.cn -e thinkphp")
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    args = parser.parse_args()
    return args