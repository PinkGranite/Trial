def whi (top, plus, numbers):
    i = 0
    while i < top:
        print ("At the top i is %d" % i)
        numbers.append(i)
        
        i += plus
        print ("Numbers now:", numbers)
        print ("At the bottom i is %d" % i)
        
my_numbers = []
whi(50, 5, my_numbers)