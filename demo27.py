from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")
    
    next = input(">")
    # 这里用try，except来进行用户输入的监测
    # 当用户输入的实时数字时，发生错误，进入except，重新进行检验
    while True:
        try:
            how_much = int(next)
            break
        except:
            next = input("Man, you're not type a number, pleace re try:")
        
    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        # exit(0)表示无错误正常退出
        exit(0)
    else:
        dead("You greedy bastard!")
        
def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you goning to move the bear?")
    bear_moved = False
    while True:
        next = input(">")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You cna go through it now.")
            bear_moved = True
            
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")
            
def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("Hi, it, Whareveer stares at you and you go insane.")
    print ("Do you flee for your life of eat your head?")
    
    next = input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
def dead(why):
    print (why, "Good, job!")
    exit(0)
    
def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")
    
    next = input (">")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the until you starve.")
        
start()