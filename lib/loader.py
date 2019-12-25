import os
import importlib
from lib.data import logger
import threading

scan_model = {'port': 'scanner.port', 'whois': 'scanner.whois', 'c': 'scanner.C', 'os':'scanner.os','web':'scanner.web',
              'all': ['scanner.port', 'scanner.whois', 'scanner.C', 'scanner.os','scanner.web']}
mutex = threading.Lock()
#线程列表
threads = []
def isDir(plugin_path):
    if not os.path.isdir(plugin_path):
        logger.warning("%s is not a directory! " % plugin_path)
        raise EnvironmentError
    logger.info("Plugin path: %s " % plugin_path)
def jiazai(url, items, pay, dirname):
    if pay:
        logger.info('Loading scanner with "%s" key words.' % pay)
        for item in items:
            if item.endswith(".py") and not item.startswith('__'):
                plugin_name = item[:-3]
                if pay in plugin_name:
                    logger.info("Loading plugin: %s" % plugin_name)
                    module = importlib.import_module(dirname + '.' + plugin_name)
                    try:
                        result = module.run(url)
                        if result:
                            logger.success(result)
                        else:
                            logger.error("Not Vulnerable %s " % plugin_name)
                    except:
                        logger.warning("ConnectionError ")
                else:
                    continue
    else:
        pay = ''
        for item in items:
            thread = threading.Thread(target=load, args=(url, item, pay, dirname))
            threads.append(thread)
            thread.start()
    return
def load(url, item, pay, dirname):
    if item.endswith(".py") and not item.startswith('__'):
        plugin_name = item[:-3]
        if pay in plugin_name:
            mutex.acquire()
            logger.info("Loading plugin: %s" % plugin_name)
            module = importlib.import_module(dirname + '.' + plugin_name)
            try:
                result = module.run(url)
                if result:
                    logger.success(result)
                else:
                    logger.error("Not Vulnerable %s " % plugin_name)
            except:
                logger.warning("%s" % plugin_name + " ConnectionError ")
            mutex.release()
        else:
            mutex.release()
            pass
def load_exp_or_plugin(url,poc = None, exp = None):
    dirname = ''
    if exp:
        plugin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "exp")
        dirname = plugin_path[plugin_path.rfind('\\') + 1:]
        pay = exp
    elif poc:
        plugin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "plugins")
        pay = poc
        dirname = plugin_path[plugin_path.rfind('\\') + 1:]
    else:
        plugin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "plugins")
        dirname = plugin_path[plugin_path.rfind('\\') + 1:]
        pay = ''
    #判断加载的是否是一个目录
    isDir(plugin_path)
    items = os.listdir(plugin_path)
    jiazai(url, items, pay, dirname)
    return
def loadPlugin(url, poc=None, sca=None, ex=None):
    if "://" not in url:
        url = "http://" + url
    url = url.strip("/")
    logger.info("Target url: %s" % url)
    if sca:
        if sca == 'all':
            for i in scan_model['all']:
                moudel = importlib.import_module(i)
                moudel.run(url)
                logger.info("Finished")

        else:
            for i in scan_model.keys():
                if sca == i:
                    moudel = importlib.import_module(scan_model[sca])
                    moudel.run(url)
                    logger.info("Finished")
                    break
        return

    load_exp_or_plugin(url, poc, ex)
    ''''''
    for t in threads:
        t.join()
    logger.info("Finished")