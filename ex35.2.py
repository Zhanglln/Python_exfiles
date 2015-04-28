# -- coding: utf-8 --

s = raw_input(">")              
try:
    t = float(s)
    if t < 50:
        print "good"
    else:
        print "You're greedy!"        
except ValueError:
        print "fuck"




