import socket

def run(ip):
    target = ip
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((target, 5555))
    print('[*]开始监听---------默认监听端口是5555')
    server.listen(5)
    client_socket, addr = server.accept()
    print('[*]'+str(addr)+'连接成功------')
    print('[*]如果你想退出请输入exit:')
    client_handler(client_socket)
def client_handler(client_socket):
    while True:
        try:
            cmd_buffer = client_socket.recv(1024 * 1024).decode('gbk')
            print(cmd_buffer)
            response = input('>>')

            # 返回相应数据
            client_socket.send(response.encode('gbk'))  # python3中必须以BYTE流进行传输
            if response == 'exit':
                client_socket.close()
                return
        except Exception:
            print('[*]出现错误......')
if __name__ == '__main__':
    run('172.16.134.81')
