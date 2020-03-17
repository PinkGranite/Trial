# -*- coding: utf-8 -*-
x = "There are %d types of people ." % 10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x) #%r 表示将任何类型的数据打印出来,会自动输出一对单引号，%r 会重现对象类型，比如加了引号说明是字符型等
print ("I also said: '%s'" % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)