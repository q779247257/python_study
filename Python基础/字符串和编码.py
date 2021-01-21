# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对于单个字符的编码。Python提供了 ord（） 函数获取字符的整数 表示，chr()函数把编码转换为对应的字符


print(ord('A'))
print(chr(66))

# 由于Python的字符串类型是 str ，在内存钟以 Unicode 表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把 str 变为以字节为单位的 bytes

# Python 对 bytes 类型的数据用带 b 铅锤的单引号或双引号表示
x = b'ABC'
print(x)

# 已 Unicode 表示的 字符串 通过 encode（）方法可以编码为指定的 bytes，如下
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 注意 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


# 你可能猜到了，%运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
#
# 常见的占位符有：
#
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
formatString = 'Hello, %s' % 'world'
print(formatString)
print('你好， %s , 我今年 %d 岁了' % ("邢轩轩" , 18))

#  其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果你不太确定用什么， %S 永远起作用，它会把任何数据类型转换为字符串
print('我今年 %s 岁了 ， 替换一个 bool 类型 %s ' % ( 18 , True ))


# format()
# 另一种格式化字符串的方法是使用字符串的 format() 方法，它会用传入的参数一次替换字符串的占位符 {0} {1}......
# 不过这种方式写起来比 % 要麻烦的多
print("你好，我是 {0} 我今年 {1} 岁了".format("邢轩轩" , 18))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

qunian = 72
jinnian = 85

r = (jinnian - qunian ) / qunian
print('小明的成绩提升了 %.1f' % r )
print('中文'.encode('utf-8'))




