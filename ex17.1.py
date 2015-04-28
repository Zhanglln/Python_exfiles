# -- coding: utf-8 --
from sys import argv
from os.path import exists

script, from_file, to_file = argv


open(to_file, 'w').write(open(from_file).read())

# 一行实现将文件复制到另一个文件


