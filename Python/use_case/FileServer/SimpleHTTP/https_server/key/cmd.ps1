# 生成 rsa 私钥
openssl genrsa -des3 -out ca.key 2048
# 用私钥生成公钥证书
openssl req -x509 -key ca.key -out ca.crt -days 365
# 可以读一下证书的内容看看
openssl x509 -in ca.crt -text -noout

# 生成 rsa 私钥
openssl genrsa -out summer-py-server.key 2048
# 用私钥生成证书签名请求
openssl req -new -key summer-py-server.key -out summer-py-server.csr
# 用 CA 根证书签名
openssl x509 -req -in summer-py-server.csr -CA ../ca/ca.crt -CAkey ../ca/ca.key  -extfile ext.ext -set_serial 01 -out summer-py-server.crt -days 365

# 在证书管理器中查看证书
certlm.msc
