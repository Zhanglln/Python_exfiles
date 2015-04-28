# -- coding: utf-8 --
from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input("> ")
    try:
        how_much = float(next) 
        if how_much < 50.0 :
            print "Nice, you're not greedy, you win!"     
            exit(0)
        else:
            dead("You greedy bastard!")         
    except ValueError:              
        dead("Man, learn to type a number.")        
#完成，当输入一个数字不论整型浮点型大于50小于50有不同输出，当输入不是一个数字的时候报错。        
def bear_room():
    print "There is a bear here."        
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
    # 当下面条件为 True 时继续执行
        next = raw_input(">")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
            #两次挑逗就会 dead 所以这里是为了阻止两次挑逗。
        elif next == "open door" and bear_moved:
        # 这里是为了先 taunt bear 之后熊动了才能打开门。
            gold_room()
        else:
            print "I got no idea what that means."
            
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "Good job!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve.") 
        
        
start()                                                                 
          
