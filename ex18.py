# -- coding: utf-8 --
#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)    
    
#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
    print "I got nothin'."
    
    
print_two("Zhang", "yuting")
print_two_again("Zhang", "yuting") 
print_one("Frist")           
print_none()
#为自己写一个函数注意事项以供后续参考。你可以写在一个索引卡片上随时阅读，直到你记住所有的要点为止。注意事项如下：

#函数定义是以 def 开始的吗？
#函数名称是以字符和下划线 _ 组成的吗？
#函数名称是不是紧跟着括号 ( ？
#括号里是否包含参数？多个参数是否以逗号隔开？
#参数名称是否有重复？（不能使用重复的参数名）
#紧跟着参数的是不是括号和冒号 ): ？
#紧跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？
#函数结束的位置是否取消了缩进 (“dedent”)？
#当你运行（或者说“使用 use”或者“调用 call”）一个函数时，记得检查下面的要点：

#调运函数时是否使用了函数的名称？
#函数名称是否紧跟着 ( ？
#括号后有无参数？多个参数是否以逗号隔开？
#函数是否以 ) 结尾？
#按照这两份检查表里的内容检查你的练习，直到你不需要检查表为止。


