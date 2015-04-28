# -- coding: utf-8 --
from sys import argv  #调用 sys 模块的 argv 函数 

script, filename = argv # 把两个值赋给 argv 运行的时候要把变量给 argv可以是文件

txt = open(filename)  #打开这个文件给 txt

print "Here's your file %r." % filename
print txt.read()  #打印txt 文件

print "Type the filename again:"
file_again = raw_input(">")   #这里如果输入其他文件名会报错因为找不到

txt_again = open(file_again)  #再打开

print txt_again.read()  #再打印

txt_again.close()
