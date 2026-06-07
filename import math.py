import math

# 控制台字符爱心
for y in range(15, -15, -1):
    line = ""
    for x in range(-30, 30):
        # 心形公式: (x^2 + (9/4)y^2 + |x|*y - 1) ... 简化版用圆形组合
        # 使用更经典的心形方程
        if ((x*0.8)**2 + (y*1.2)**2 - 1)**3 - (x*0.8)**2 * (y*1.2)**3 <= 0:
            line += "*"
        else:
            line += " "
    print(line)