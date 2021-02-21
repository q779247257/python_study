#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
#  Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素
# 比如，列出班立所有同学的名字，就可以用一个list表示
names = ['小明' , '小红' , '小蓝' ]
print(len(names))# 用 len（） 函数可以获得list元素的个数
print(names)

# 用索引来访问list钟的每一个位置的元素（会报数据下标越界）
print(names[0])
# python 中可以使用负数的索引来获取倒数的元素 如下(倒数第一个元素 ； 最后一个):
print(names[-1])
# 以此类推 可以获取倒数第2，3
print(names[-2])
print(names[-3])

# list 是一个可变的有序表，所以，可以往list中追加元素到末尾
names.append("小粉")
print(names)
# 也可以把元素插入到指定的位置
names.insert(1 , '小紫')
print(names)
# 要删除list末尾的元素 用 pop（） 方法
names.pop()
print(names)
# 要删除指定位置的元素 使用 pop（index）方法
names.pop(-1)
print(names)
# 要替换某个元素直接赋值对应的索引
names[2] = '小蓝'
print(names)

# list里面的元素的数据类型也可以不同，比如：
L = ['轩轩',123,True]

# list元素也可以是另一个list，比如：
Ls = ['python','java','php',L]
print(len(Ls))


# tuple
# 另一种有序列表叫做元组,tuple和list非常类似,但是tuple一旦初始化就不饿能修改,比如列出同学的名字
classmates = ("小明","小红","小丽")
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
# 但不能赋值成另外的元素。



# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])
