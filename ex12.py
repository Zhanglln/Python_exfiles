# -- coding: utf-8 --
age = raw_input ("How old are you?\n")
height = raw_input ("How tall are you?\n ") #这个 \n "之间的空格会导致换行打入输入的时候前面有个空格。而第2行没有这个空格所以就顶格写。
weight = raw_input ("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy" %(age, height, weight)
