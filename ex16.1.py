# -- coding: utf-8 --
#写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。
from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your txt_file:", filename
print txt.read()
txt.close()
