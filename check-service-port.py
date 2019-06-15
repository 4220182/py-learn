"""
tcp端口状态检查

参考：
https://www.jb51.net/article/144318.htm
"""

import socket


def check_server(address, port):
    s = socket.socket()
    s.settimeout(5)
    print('Attempting to connect to %s on port %s' % (address, port))
    try:
        s.connect((address, port))
        print('Connected to %s on port %s' % (address, port))
        return True
    except socket.error as e:
        print('Connection to %s on port %s failed: %s' % (address, port, e))
        return False
    finally:
        s.close()


if __name__ == '__main__':
    check_server("127.0.0.1", 22)
    check_server("127.0.0.1", 23)

