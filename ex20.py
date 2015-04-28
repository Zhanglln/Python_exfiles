# -- coding: utf-8 --
from sys import argv

script, input_file = argv

def print_all(f):     
    print f.read()
#定义一个函数名字叫 print_all  给它一个参数叫 f  接着一个冒号，冒号下面的内容都属于这个 print_all  函数，表示这个函数要干什么，这里表示  f   这个参数要执行        .read()      .
def rewind(f):
    f.seek(0) 
# seek(0) 是将指针定义到起始位置，好处是不用再打开文件。具体怎么用？  
def print_a_line(line_count, f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)
# 删除 rewind() 这行(即不执行 .seek(0) 的话会导致下面只会显示行数，但不会打印出行的内容，即 .read()执行不出来)
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) 
# 这里的 .readline()  不会识别你这里是第几行它输出，只是一行一行地输出。
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)            

