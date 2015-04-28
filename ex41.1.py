# -- coding: utf-8 --
def compare(a, b):
    """比较两个数的大小,输出较大的那个"""
    print (compare.__doc__)  # 这里是两个下划线 __
    if x > y :
        print "The big one is %r" % x
    else:
       print "The big one is %r" % y    
print "Please type two numbers:"
x= raw_input()
y = raw_input()
compare(x, y)    
   
