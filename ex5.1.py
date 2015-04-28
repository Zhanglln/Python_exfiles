# -- coding: utf-8 --
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74  # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name   #Let's talk about 'Zed A. Shaw'.
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy." 
print "He's got %r eyes and %s hair." % (eyes, hair)   #He's got 'Blue' eyes and Brown hair.注意前后一个是 %r，一个是 %s.
print "His teeth are usually %r depending on the coffee." %teeth

#this lines is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# %d 整数  %f 浮点数  %s 字符串 %x 十六进制整数 %r 不管什么都打印出来
#当不确定用什么的时候就用 %s.
