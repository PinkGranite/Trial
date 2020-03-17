print ("How old are you?"),
# 这里的这个逗号可以使在读完这一行语句后不切换到下一行
age = raw_input()
# 在python2中raw_input会将用户输入的所用信息都当做字符创处理，而input则必须输入规范的数据类型，如要输入字符串时，必须带“”
# 在python3中已经将以上两个函数进行了整合，input（）功能就可以实现原理raw——input的功能
# 事实上在python2中，input（）函数会将用户输入的信息当做python的代码来处理
print ("How tall are you?"),
height = input()
print ("How muth do you weight?"),
weight = raw_input()

print ("So, you're %s old, %s tall and %s heavy" % (age, height, weight))