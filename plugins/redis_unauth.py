import socket

def run(url):
    ip = url if not "://" in url else url.strip("http://")
    port = int(ip.split(':')[-1]) if ':' in ip else 6379
    payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
    s = socket.socket()
    socket.setdefaulttimeout(3)
    s.connect((ip, port))
    s.send(payload.encode())
    recvdata = s.recv(1024)
    s.close()
    if recvdata and 'redis_version' in recvdata.decode():
        return "Redis unauth Vulnerable."
    else:
        return False

if __name__ == '__main__':
    print(run("192.168.27.128"))
