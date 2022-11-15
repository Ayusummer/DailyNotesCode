# 不使用 decimal 直接 round
f = float(input('请输入华氏度: '))
c = (f - 32) / 1.8
# # 计算结果保留 2 位小数
c = round(c, 2)

print("华氏温度{0}转换为摄氏温度为:{1}".format(f,c))