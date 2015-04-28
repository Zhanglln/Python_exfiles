# --coding: utf-8 --
formatter = "%r %r %r%r "

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
       " I had this thing." ,
       "That you could type up right.",
      "But it didn't sing.", #字符串里有单引号  '   输出两端就是双引号，否则输出就是单引号
      "So I said goodnight."
      )
      
# 怎么让后4行输出换行？？？格式化输出怎么换行使用转意字符 "\n" ？已解决ex8.1.py
