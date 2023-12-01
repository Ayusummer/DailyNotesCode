# 向 https://attack.mitre.org/matrices/enterprise/ 发送一个 get 请求
import httpx

url = "https://attack.mitre.org/matrices/enterprise/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# 使用本地 7890 端口作为代理
proxies = {"http": "http://127.0.0.1:7890"}

# 发送请求(忽略证书验证)
r = httpx.get(url, headers=headers, verify=False, proxies="http://127.0.0.1:7890")
print(r.text)
