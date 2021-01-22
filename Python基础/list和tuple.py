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
