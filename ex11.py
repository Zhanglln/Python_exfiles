# -- coding: utf-8 --
print "How old are you?"    #这里不加逗号 ,  会换到下一行输入自己的年龄。
age = raw_input()
print "How tall are you?",   #这里加逗号 ,  输入的体重和问题在一行。
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %r tall and %r heavy."%(age, height, weight)

name = raw_input ("What's your name :")
print "Hello", name
