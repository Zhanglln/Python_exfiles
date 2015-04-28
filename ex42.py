# -- coding: utf-8 --
class TheThing(object):

    def __init__(self):
        self.number = 0
#接下来，看到 __init__ 函数了吗？这就是你为 Python class 设置内部变量的方式。你可以使用 . 将它们设置到 self 上面。        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        self.number += more
        return self.number
        
#two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number                        
