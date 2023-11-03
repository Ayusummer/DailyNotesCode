import socket

# 定义域名和IP地址的映射
dns_records = {
    "example.com": {
        "A": "192.168.1.100",
        "AAAA": "2401:da00::6666",
    },
    "google.com": {
        "A": "172.217.10.110",
        "AAAA": "2404:6800:4004:80a::200e",
    },
    "yahoo.com": {
        "A": "98.137.246.7",
        "AAAA": "2001:4998:58:1836::10",
    },
}


def query_dns(data):
    print(f"数据: {data}")
    return b"\xcb_\xcf\x12~\x81\x80\x00\x01\x00\x06\x00\x00\x00\x00\x05yahoo\x03com\x00\x00\x1c\x00\x01\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x00$\x12\r\x00\x00\x00\x00\x00\x01\x00\x00\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x01$\x15\x07\x00\x00\x00\x00\x00\x00\xf0\x00\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x00D5\x07\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x00D5\x07\x00\x00\x00\x00\x00\x00\x80\x01\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x00$\x12\r\x00\x00\x00\x00\x00\x01\x00\x01\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00<\x00\x10 \x01I\x98\x01$\x15\x07\x00\x00\x00\x00\x00\x00\xf0\x01"
    if domain in dns_records:
        ip_address = dns_records[domain]
        return f"{domain} A {ip_address}"
    else:
        return f"{domain} - Not Found"


def main():
    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("0.0.0.0", 53)  # 监听所有接口的53端口

    server_socket.bind(server_address)

    print("DNS服务器正在监听...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        response = query_dns(data)
        server_socket.sendto(response, client_address)
        # print(f"客户端地址: {client_address}, 数据: {data}")
        # data = b'M\xa4\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05yahoo\x03com\x00\x00\x01\x00\x01'

        # # data 为16进制数据, 1,2位为标识符，3,4位为标志位，5,6位为问题数，7,8位为回答数，9,10位为授权数，11,12位为附加数
        # identification = data[0:2]
        # flags = data[2:4]
        # questions = data[4:6]
        # answers = data[6:8]
        # authority = data[8:10]
        # additional = data[10:12]
        # # 问题部分
        # # 问题部分的第一个字节为问题长度，后面为问题内容，以\x00结尾
        # quert_name_1_length = data[12]
        # query_name_1 = data[13 : 13 + quert_name_1_length]
        # query_name_2_length = data[13 + quert_name_1_length]
        # query_name_2 = data[
        #     14 + quert_name_1_length : 14 + quert_name_1_length + query_name_2_length
        # ]
        # query_name = (query_name_1 + b"." + query_name_2).decode("utf-8")
        # # 问题部分的最后两个字节为问题类型，最后两个字节为问题类
        # query_type = data[-4:-2]
        # query_class = data[-2:]
        # # print(query_name, query_type, query_class)
        # print(
        #     f"标志位: {flags}, 问题数: {questions}, 回答数: {answers}, 授权数: {authority}, 附加数: {additional}, 问题: {query_name}, 类型: {query_type}, 类: {query_class}"
        # )


if __name__ == "__main__":
    main()
