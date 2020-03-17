
# this one is like your scripts with argv
def print_two(*args):
    # 这里是生成了一个列表，将传入进来的参数存储在其中
    # 用*args可以接受一系列的变量，但需要一个解包的过程
    arg1, arg2 ,arg3= args
    # 将参数解包，和脚本参数解包的原理差不多
    print ("arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3))
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
# this just takes one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)
    
# this one takes no arguments
def print_none():
    print ("I got nothin.")
    
    
print_two("Zed", "Shaw", "hh")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()