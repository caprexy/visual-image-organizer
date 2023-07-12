from tkinter import *


root = None

def setActivityRoot(rootIn):
    global root 
    root = rootIn



def initalizeActivityFrame():
    global imgFrame
    imgFrame = Frame(root, bg="black")
    # imgFrame.grid(column=0, row=1, sticky=(N, W, E, S))
    return imgFrame