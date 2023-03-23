# 测试 chatdbg  - https://github.com/plasma-umass/ChatDBG
# 失败, 报错, 用不成功
def tryme(x):
    count = 0
    for i in range(100):
        if x / i > 2:
            count += 1
    return count

if __name__ == '__main__':
    print(tryme(100))
