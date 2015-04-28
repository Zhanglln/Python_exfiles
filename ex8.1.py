# -- coding: -utf-8 --
formatter = "%r\n %r\n %r\n %r"
#有时候自己想到的问题也许就在后面出现了，怎么在格式化字符串中换行输出（或者是使用其他类的转义符）？出现在 ex10 的加分习题中  ^_^

print formatter % (
       " I had this thing.", 
       #在这行的引号后面或者前面加 \n 都无法转义换行
       "That you could type up right.",
      "But it didn't sing.",
      "So I said goodnight."
      )
      #  not all arguments converted during string formatting

