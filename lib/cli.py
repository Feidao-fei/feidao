from lib.cmdline import cmdLineParser
from lib.loader import loadPlugin
from colorama import Fore
def main():
    banner = '''
                  _____         .__     .___                
        _/ ____\  ____  |__|  __| _/_____     ____  
        \   __\ _/ __ \ |  | / __ | \__  \   /  _ \ 
         |  |   \  ___/ |  |/ /_/ |  / __ \_(  <_> )
         |__|    \___  >|__|\____ | (____  / \____/ 
                     \/          \/      \/         
                     Author:{}
    '''.format(Fore.LIGHTGREEN_EX+"feidao")
    print(Fore.LIGHTCYAN_EX+banner)

    args = cmdLineParser()
    if args.target:
        url = args.target
    if args.module:
        plugin = args.module
    else:
        plugin = None
    if args.scanner:
        scan = args.scanner
    else:
        scan = None
    if args.exp:
        exp = args.exp
    else:
        exp = None
    loadPlugin(url=url, poc=plugin, sca=scan, ex=exp)