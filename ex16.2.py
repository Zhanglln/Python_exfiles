# -- coding: utf-8 --
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)." #这里无论如何都会用truncate 函数删除全部内容，要实现应该要用到 if else 循环了吧？
print "If you do want that, hit RETURN."

raw_input("?") #读取 ？ 以后输入的内容，但是没有将其赋值给别的参数？不太懂。

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."
#target.write('''
#line1
#line2
#line3
#'''  ) #将输入写入(字符串法)错误不可行

a = ("%s\n%s\n%s\n") % (line1, line2, line3) # 格式化字符串法
target.write(a)
print "And finally, we close it."
target.close()
