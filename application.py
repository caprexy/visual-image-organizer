from tkinter import *
from PIL import ImageTk, Image
from functions.imageArrayHelper import *
from functions.activityFrameHelper import *
from functions.topMenuHelper import buildMenubar, setTopMenuRoot

root = Tk()
setTopMenuRoot(root)


#  build img array frame


# setting up root geometry
root.geometry("1000x900")

mainWindow = PanedWindow(root, orient=HORIZONTAL)
mainWindow.pack(fill=BOTH, expand=TRUE)

setImgArrRoot(mainWindow)
setActivityRoot(mainWindow)
mainWindow.add(initalizeActivityFrame(), stretch="always")
mainWindow.add(initalizeImageArrayFrame(), stretch="always")

mainWindow.bind("<Configure>", resizeImageArray)


root.bind("<Button-1>",on_click)

root.bind("<Configure>", resizeImageArray)

root.config(menu=buildMenubar())

root.mainloop()