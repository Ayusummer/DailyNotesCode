import socket

# 木糖醇是糖么?
# nmap -p 9220-9230 214.214.214.215 是用啥扫的 UDP 么?


def scan_port(ip, port):
    """判断端口是否放通, 是则返回 True, 否则返回 False  
    尝试与 ip-port 建立 TCP 连接, 连接成功则说明端口开放  

    """
    # 创建一个 TCP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置套接字超时时间为 1s
    sock.settimeout(1)

    try:
        sock.connect((ip, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def scan_ports_on_ip(ip, ports):
    for port in ports:
        if scan_port(ip, port):
            print(f"Port {port} is open on {ip}")
        else:
            # print(f"Port {port} is closed on {ip}")
            pass


# Define the IP address
# ip = "192.168.4.210"
# ip = "192.168.1.215"
ip = "214.214.214.215"

# Define the ports
ports = list(range(9200, 9231))  # 9200 to 9230
# ports.extend([22, 80, 443])  # Add 22, 80 and 443
# ports = [9225]


# Start scanning
scan_ports_on_ip(ip, ports)
