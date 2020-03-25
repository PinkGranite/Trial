## Animal is a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
# （创建一个 狗 类）（动物的子类）
class Dog(Animal):
    
    def __init__(self, name):
        #?
        self.name = name
        
# 创建一个 猫 类（动物的子类）
class Cat(Animal):
    
    def __init__(self, name):
        ## ?
        self.name = name
        
# 创建一个 人 类
class Person(Animal):
    
    def __init__(self, name):
        self.name = name
        
        ## Person has a pet of some kind
        self.pet = None
        
## 创建一个工人类（人的子类）
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? hmm what is this stange magic
        ## super（）是调用父类的一个方法，在python3中，可以直接用python（）代替python（class，self）
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
        
## 创建一个 鱼 对象
class Fish(object):
    pss
    
class Salmon(Fish):
    pass
    
class Halibut(Fish):
    pass
    
## rover is a dog
rover = Dog('Rover')

satan = Cat("Satan")

mary = Person("Mary")