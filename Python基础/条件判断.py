#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断
# 比如输入用户的年龄 根据用户的年龄来判断是否为未成年

age = 18
if age >= 18:
    print('yes! 你成年了!', age)
else:
    print("not 你未成年 ", age)

# 也可以加多个 elseIf python中 是 elif
#  python中没有 && 、 ||  运算符 用and 和 or 替代

height = 169

if height >= 180:
    print("你的身高还不错")
elif 170 <= height < 180:
    print("其实你的身高还可以")
else:
    print("你的身高在170以下 需要加油哦！")

# 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

birthStr = input('请输入你的出生年份：')
birthInt = int(birthStr)

if birthInt < 2000:
    print("你是00前！！")
else:
    print("你是00后")

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5

bmi = weight / (height * height)
print("bmi 指数为：", bmi)

if bmi < 18.5:
    print("您有点轻了！！")
elif 25 > bmi >= 18.5:
    print("恭喜您，您的bmi指数正常")
elif 25 <= bmi < 28:
    print("有点过重哦")
elif 28 <= bmi < 32:
    print("有点肥胖哦")
elif bmi >= 32:
    print("严重肥胖")
