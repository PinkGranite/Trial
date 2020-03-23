print ("This is a magic world, and wellcome you here my brave!")
print ("Please chooce your peofession. Do you want to be a  1#soilder, 2#enchanter, 3#assassinator")
my_profession = input(">")
if my_profession == '1':
    print("OK, you are a brave soilder, and you are good at fight against the enemy right in front them. You have high HP but low MP")
elif my_profession == '2':
    print ("OK, you are a enchanter, and you are good at fight against the enemy in a long distance. You have high MP bot low HP.")
elif my_profession == '3':
    print ("OK, you are a skilled assassinator, and you are good at kill your enemy in the near shadow. You have high MP and low HP.")
print ("The adventure begin…………")
print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input(">")

if door == '1':
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream the bear.")
    
    bear = input(">")
    
    if bear == '1':
        print ("The bear eats your face off. Good job!")
    elif bear == '2':
        print ("The bear eats your legs off. Good job!")
    else:
        print ("Well, doing %s is probabaly better. Bear runs away." % bear)
        
elif door == '2':
    print ("You stare into rhe endless abyss at Cthulhu's retina.")
    print ("1. Blueberies.")
    print ("2. Yellow jacket clothespins.")
    print ("Understanding revolvers yelling molodies.")
    
    insanity = input(">")
    
    if insanity == '1' or insanity == '2':
        print ("Your body survives powered by a mind of jello. Good job!")
    else:
        print ("The insanity rots your eyes into a pool if muck. Good job!")
        
else:
    print ("You stumble around and fall on a knife and die. Good job!")