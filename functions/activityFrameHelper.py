from tkinter import *


root = None

def setActivityRoot(rootIn):
    global root 
    root = rootIn



def initalizeActivityFrame():
    global imgFrame
    imgFrame = Frame(root, bg="black")
    return imgFrame