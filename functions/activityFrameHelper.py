from tkinter import *
from tkinter import ttk
import functions.imageArrayHelper 
from functions.operationHelper import sortByModifiedDate, rebuildNames
from functions.imageArrayHelper import buildImageArray
from tkinter.filedialog import askopenfilenames


root = None
activityFrame = None

ascending = None
dropVal = None

# operation options
options = [
    "Date modified",
    "Name"
]

def setActivityRoot(rootIn):
    global root 
    root = rootIn

def buildFrame():
    global ascending, dropVal

    activityFrame.grid_columnconfigure(0, weight=1, uniform="equal")
    activityFrame.grid_columnconfigure(1, weight=1, uniform="equal")
    activityFrame.grid_columnconfigure(2, weight=1, uniform="equal")

    loadButton = Button(activityFrame, text = "Load images", command = loadImages)
    loadButton.grid( row=0, column=0, pady= 10, sticky= W + E)
    loadButton.configure(width=10, height=2)

    reorgButton = Button(activityFrame, text = "Reorganize", command = operationCallback)
    reorgButton.grid( row=0, column=2, pady= 10, sticky= W + E)
    reorgButton.configure(width=10, height=2)

    seperator = ttk.Separator(activityFrame, orient=HORIZONTAL)
    seperator.grid(row = 2, column=0, columnspan=3, sticky="ew", pady=10)

    operationLabel = Label(activityFrame, text="Reorganize according to: ")
    operationLabel.grid(row=3, column=0)
    dropVal = StringVar(root)
    dropVal.set(options[0])
    drop = OptionMenu( activityFrame , dropVal , *options )
    drop.grid( row=3, column=1, pady= 10, sticky= W + E)
    drop.configure(width=10, height=2)
    ascendingCheckbutton = Checkbutton(activityFrame, text="Ascending: (First is smallest)", variable=ascending)
    ascendingCheckbutton.grid(row=3, column=2)

    

def initalizeActivityFrame():
    global activityFrame, ascending

    ascending = BooleanVar()
    ascending.set(True)

    activityFrame = Frame(root)
    activityFrame.grid_propagate(False)
    buildFrame()
    return activityFrame

def operationCallback():
    imgLabels = functions.imageArrayHelper.imgLabels
    if(imgLabels == []): return 

    paths = [photoImage.filepath for photoImage in imgLabels]
    userChoice = dropVal.get()

    if(userChoice == options[0]):
        sortByModifiedDate(paths, ascending)
    elif(userChoice == options[1]):
        rebuildNames(paths, ascending)

def loadImages():
    files = askopenfilenames( title  = "Select images to sort", 
                filetypes =  [('image files', '.png'),
                              ('image files', '.jpg'),])
    buildImageArray(files)