class TheThing(object):
    
    def __init__(self):
        self.number = 0
        
    def some_function(self):
        print ('I got called.')
        
    def add_me_up(self, more):
        self.number += more
        return self.number
        
# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print (a.number)
print (b.number)

print (a.add_me_up(22))
print (a.add_me_up(33))

print (a.number)
print (b.number)

# Study this. This is how you pass a variable
# from one class to another. You will need this
class TheMultiplier(object):
    
    def __init__(self, base):
        self.base = base
        
    def do_it(self, m):
        return m * self.base
        
X = TheMultiplier(a.number)
print (X.do_it(b.number))