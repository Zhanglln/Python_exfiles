# -- coding: utf-8 --
print '''
"I am 6'2\" tall."
'I am 6\'2" tall.'
'''
print "I am 6'2\" tall.",    #此处加上逗号 ,  就会打印在一行，不带逗号就分成两行打印。
print 'I am 6\'2" tall.'
print "First\nSecond"
print r'\"First\nSecond"'   # r'       ' 表示引号内的内容默认不转义。同理可以用在多行换行输出的 '''          '''   

tabby_cat = "\t@$\a\b*I'm tabbed\n i\000n."  #\t 横向制表符，\a响铃（未显示），       \b退格，\000空
print "\ffirst,second" #\f 换页 （未显示）？？？

fat_cat = '''
I'll do a list:
\v* Cat food
\v* Fishies
\v* Catnip\n\v* Grass
'''
#纵向制表符
print tabby_cat
print fat_cat

#将转义序列和格式化字符串放到一起，创建一种更复杂的格式，只需要在           formatter = "%r\n %r\n %r\n %r" 中的 %r 或 %s 的后面像打印字符串一样正常的使用转义符即可。
color = "\n\t%s\t\n%s\n\t%r\n\t%r\n"  #\t 相当于缩进，所以每一段都要用。而且一定要注意！！！！ 先\n\t 这样才表示先换行再横向制表（即缩进，相当于多了几个空格），  如果先 \t\n 就会先缩进有几个空格然后在换行，所以顶在一行的前面！最后一个%r 后面如果再没有 \n 的话再输入就会和它一行。
print "I like the clothes with",color  %(
    "Blue",
    "White",
    "Red",
    "Purple."
 )  + "\tcolors"  #这里其实也可以把color 加在格式化字符串里。这样更好。
 #要先确定想要的是什么样的结果，然后从后往前推设计什么样的代码才能实现，不要没有头绪，目标要清晰。如果不想出现  '       '分号的话应该用到数组了吧？逗比把 %r 改成%s 就行了。
