from tkinter import *

from tkinter.filedialog import askopenfilenames

from functions.imageArrayHelper import buildImageArray


root = None

def setTopMenuRoot(rootIn):
    global root 
    root = rootIn

def buildMenubar():
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Load images", command=loadImages)
    menubar.add_cascade(label="File", menu=filemenu)

    # filemenu = Menu(menubar, tearoff=0)
    # filemenu.add_command(label="New")
    # filemenu.add_command(label="Open")
    # filemenu.add_command(label="Save")
    # filemenu.add_separator()
    # filemenu.add_command(label="Exit", command=root.quit)
    # menubar.add_cascade(label="File", menu=filemenu)

    # helpmenu = Menu(menubar, tearoff=0)
    # helpmenu.add_command(label="Help Index")
    # helpmenu.add_command(label="About...")
    # menubar.add_cascade(label="Help", menu=helpmenu)

    return menubar

def loadImages():
    files = askopenfilenames( title  = "Select images to sort", 
                filetypes =  [('image files', '.png'),
                              ('image files', '.jpg'),])
    buildImageArray(files)