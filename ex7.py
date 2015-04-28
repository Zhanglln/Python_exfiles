# --coding: utf-8 --
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?
print " 亭哥哥 \n" * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, 
print end7 + end8 + end9 + end10 + end11 + end12  #22.23行运行后出现在一行
print " '%r' " % (end1 + end2 + end3 + end4 + end5 + end6,)   #  ''Cheese'' 
print " %r " % (end1 + end2 + end3 + end4 + end5 + end6,) 
print " '%r' " % end1 + end2 + end3 + end4 + end5 + end6,     #  ''C'' heese
print " %r " % end1 + end2 + end3 + end4 + end5 + end6, "\n"      #  'C' heese   会换行，但是和下一行中间会空一行？
print " %s " % (end1 + end2 + end3 + end4 + end5 + end6,) 
