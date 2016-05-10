import socket
import re


def main():
    try:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect(("192.168.77.77", socket.getservbyname('ssh')))
            sock_output = sock.recv(100)
        except socket.timeout:
            return False, "SSH Connection Timeout"
        except socket.error:
            return False, "SSH Connection Error"
    finally:
        sock.close()

    result = re.search('SSH-2.0-OpenSSH_5.1', sock_output)
    if not result:
        return False, "Valid SSH interface not found"
    else:
        return True, "Valid SSH interface was found"

print main()
