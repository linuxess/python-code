#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:Branches and Functions 
# ScriptName: less35.py
#***************************************************************#

from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take?"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man, learn to type a number.")

    if how_much < 50:
        print "nice, you're not greedy, you win."
        exit(0)
    else:
        dead("you greedy bastard")
#dead函数在下面定义。

def bear_room():
    print "there is a bear here"
    bear_moved = False
    while True:
        next == raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "take bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "good job"
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
         dead("You stumble around the room until you starve.")

start()
