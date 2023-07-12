from tkinter import *
from PIL import ImageTk, Image
from functions.imageArrayHelper import *
from functions.activityFrameHelper import *
from functions.topMenuHelper import buildMenubar, setTopMenuRoot



# setup god window
root = Tk()
setTopMenuRoot(root)

# setting up root geometry
root.geometry("1000x900")

# adds an onclick for image array watching
root.bind("<Button-1>",on_click_img_arr)

# add other binds
root.bind("<Configure>", resizeImageArray)

root.config(menu=buildMenubar())




# build main window which will be a panedwindow
mainWindow = PanedWindow(root, orient=HORIZONTAL)
mainWindow.pack(fill=BOTH, expand=TRUE)

# set the roots or parents of the img and the activity frame
setImgArrRoot(mainWindow)
setActivityRoot(mainWindow)
# add said frames
mainWindow.add(initalizeActivityFrame(), stretch="always")
mainWindow.add(initalizeImageArrayFrame(), stretch="always")

# extra configs to dynamically recalculate image array sizes
mainWindow.bind("<Configure>", resizeImageArray)



root.mainloop()