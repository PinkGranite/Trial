# -*- encode: utf-8 -*-
tabby_cat = "\t I'm tabbed in."
perisian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

# 使用连续"""或者'''都可以是的一下多段文本皆为字符
fat_cat = ''' 
I' ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print (tabby_cat)
print (perisian_cat)
print (backslash_cat)
print (fat_cat)

print ("\x45")# 输出16进制下45对应的ASCALL符号
print ("\145")# 输出8进制下145对应的ASCALL符号
print ("a\v ")# 垂直制表
print ("a?????\r?????b\r123456")# 回车符
print ("a \bb")# 退格符
print ("a  \f  b")
print ("\a")# 响铃符