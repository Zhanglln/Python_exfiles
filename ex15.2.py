# -- coding: utf-8 --
from sys import argv  #调用 sys 模块的 argv 函数 

script, filename = argv # 把两个值赋给 argv 运行的时候要把变量给 argv可以是文件


txt_file = open(filename)
print "Here's your file %r." % filename
print txt_file.read()
filename_again = raw_input ("Please type:\n")
the_file = open(filename_again) #打印txt 文件
a = the_file.read()
print a 
the_file.close()

