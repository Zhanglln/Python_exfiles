# -- coding: utf-8 --
# 设计程序的时候别乱，构思要清晰。先在纸上写流程从后往前推导。

def loop(n):
    # 这里的 i , elements 参数赋值要在 def 定义的函数下，否则报错/
    i = 0
    elements = []
    while i < n:
        print "At the top i is :%d" % i
        elements.append(i)
        
        i += k
        print "Numbers now :", elements
        print "At the bottom i is : %d" % i
    for t in elements:       
    # 这里的 for 要与上面的 while 缩进对齐，这样就能打印在循环外面。
        print t
n = 10
k = 0.5
print "The loop is:"
loop(n)        

