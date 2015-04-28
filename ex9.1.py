# -- coding: -utf-8 --
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nAug"

print "Here are the %s:\n " % days  # 格式化打印也可以，但是一定注意 % 前面绝不能有逗号！！！！！！
print "Here are the months: ", months  #只是简单的打印，前面有双引号就打印引号内的内容， 而 months 在前面有过定义，所以当成字符串来打。 但是一定注意要有逗号！！！

print '''    #这里无法加注释，与上面一行代码之间的空行就是这一行与第7行无关
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or5, or6.
'''
#8行是多行换行打印的符号,要么上下都是三个 ''' 单引号，要么上下都是三个 """  双引号
