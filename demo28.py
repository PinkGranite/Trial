class student(object):
    # 带__的方法在python中被称作魔法算法，如init算法会再创建对象时自动调用
    # 同时init算法中也是定义属性变量的地方
    # str方法是用作直接输出的，可直接对print(对象),输出return后的语句
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return ("My name is %s, and my age is %d" % (self.name, self.age))
        # 这里需要用return
        
        
        
stu1 = student("YYW", 22)
print (stu1)