# 使用 decimal
from decimal import Decimal

# 输入华氏度
f = Decimal(input('请输入华氏度: '))
c = Decimal(f - 32) / Decimal(18/10)
# # 计算结果保留 2 位小数
c = round(c, 2)

print("华氏温度{0}转换为摄氏温度为:{1}".format(f,c))