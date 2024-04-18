# 计算各种 hash
import hashlib, binascii, base64
from gmssl import sm3, func
from pathlib import Path

"""
各种哈希算法(基于字符串)
"""


def pwdbase64(password: str, encode="utf-8"):
    b64_byt = base64.b64encode(password.encode(encoding=encode))
    b64_str = b64_byt.decode(encoding=encode)
    return b64_str


def pwdmd5(password: str, encode="utf-8"):
    m = hashlib.md5()
    m.update(password.encode(encoding=encode))
    return m.hexdigest()


def pwdsha1(password: str, encode="utf-8"):
    s1 = hashlib.sha1()
    s1.update(password.encode(encoding=encode))
    return s1.hexdigest()


def pwdsha256(password: str, encode="utf-8"):
    s1 = hashlib.sha256()
    s1.update(password.encode(encoding=encode))
    return s1.hexdigest()


def pwdntlm(password: str, encode="utf-8"):
    # n = hashlib.new('md4', text.encode('utf-16le'))
    n = hashlib.new("md4")
    n.update(password.encode("utf-16le"))
    return binascii.hexlify(n.digest()).decode()


def pwdmysql(password: str, encode="utf-8"):
    nr = 1345345333
    add = 7
    nr2 = 0x12345671

    for c in (ord(x) for x in password if x not in (" ", "\t")):
        nr ^= (((nr & 63) + add) * c) + (nr << 8) & 0xFFFFFFFF
        nr2 = (nr2 + ((nr2 << 8) ^ nr)) & 0xFFFFFFFF
        add = (add + c) & 0xFFFFFFFF

    return "%08x%08x" % (nr & 0x7FFFFFFF, nr2 & 0x7FFFFFFF)


def pwdmysql5(password: str, encode="utf-8"):
    """
    用SHA1散列字符串两次并返回大写十六进制摘要
    """
    pass1 = hashlib.sha1(password.encode(encoding=encode)).digest()
    pass2 = hashlib.sha1(pass1).hexdigest()
    return pass2


def pwdmd5_middle(password: str, encode="utf-8"):
    m = hashlib.md5()
    m.update(password.encode(encoding=encode))
    m = m.hexdigest()
    m16 = m[8:]
    m16 = m16[:-8]
    return m16


def pwdsm3(password: str, encode="utf-8"):
    # 数据和加密后数据为bytes类型
    m = sm3.sm3_hash(func.bytes_to_list(password.encode(encoding=encode)))
    return m


def generateHashBase(password: str) -> dict:
    """根据明文密码生成各种哈希"""
    PWD_ENCODE = "utf-8"
    hash_dict = {}
    hash_dict["md5"] = pwdmd5(password, PWD_ENCODE)
    hash_dict["md5x2"] = pwdmd5(hash_dict["md5"], PWD_ENCODE)
    hash_dict["md5x3"] = pwdmd5(pwdmd5(hash_dict["md5x2"], PWD_ENCODE))
    hash_dict["sha1"] = pwdsha1(password, PWD_ENCODE)
    hash_dict["ntlm"] = pwdntlm(password, PWD_ENCODE)
    hash_dict["mysql"] = pwdmysql(password, PWD_ENCODE)
    hash_dict["mysql5"] = pwdmysql5(password, PWD_ENCODE)
    hash_dict["md5_sha1"] = pwdmd5(pwdsha1(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["sha1_sha1"] = pwdsha1(pwdsha1(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["sha1_md5"] = pwdsha1(pwdmd5(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["md5_base64"] = pwdmd5(pwdbase64(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["md5_middle"] = pwdmd5_middle(password, PWD_ENCODE)
    hash_dict["base64_md5"] = pwdbase64(pwdmd5(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["md5_sha256"] = pwdmd5(pwdsha256(password, PWD_ENCODE), PWD_ENCODE)
    hash_dict["sha256"] = pwdsha256(password, PWD_ENCODE)
    hash_dict["sm3"] = pwdsm3(password, PWD_ENCODE)
    return hash_dict


"""
各种哈希算法(基于文件)
"""


# 计算文件的 md5
def filemd5(file_path: Path):
    m = hashlib.md5()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest().upper()
