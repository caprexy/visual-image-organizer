from tkinter import *
from PIL import ImageTk, Image
import math

# image property values
imageWidth = 200
imageHeight = 300
imageWidthPadding = 5
imageHeightPadding = 5

# frame information
root = None
colSize = 0
rowSize = 0
imgFrame = None
dragging = False

# images infomation
imgLabels = []


def setImgArrRoot(rootIn):
    global root 
    root = rootIn

def changeOrder(widget1,widget2,initial):
    target=widget1.grid_info()
    widget1.grid(row=initial['row'],column=initial['column'])
    widget2.grid(row=target['row'],column=target['column'])

    # needs to change the imgLabels so when recalculating the array size and reprinting    
    index1 = imgLabels.index(widget1)
    index2 = imgLabels.index(widget2)
    imgLabels[index1], imgLabels[index2] = imgLabels[index2], imgLabels[index1]

def on_click_img_arr(event):
    widget=event.widget
    if isinstance(widget,Label):
        start=(event.x,event.y)
        grid_info=widget.grid_info()
        widget.bind("<B1-Motion>",lambda event:drag_motion(event,widget,start))
        widget.bind("<ButtonRelease-1>",lambda event:drag_release(event,widget,grid_info))
    else:
        root.unbind("<ButtonRelease-1>")

def drag_motion(event,widget,start):
    global dragging
    
    dragging = True
    x = widget.winfo_x()+event.x-start[0]
    y = widget.winfo_y()+event.y-start[1] 
    widget.lift()
    widget.place(x=x,y=y)

def drag_release(event,widget,grid_info):
    global dragging
    
    widget.lower()
    x,y=root.winfo_pointerxy()
    target_widget=root.winfo_containing(x,y)
    if isinstance(target_widget,Label):
        changeOrder(target_widget,widget,grid_info)
    else:
        widget.grid(row=grid_info['row'],column=grid_info['column'])
    dragging = False


# when user selects their images
def buildImageArray(filepaths):
    global imgLabels,  colSize, rowSize

    # clean up things to reprint
    clearImgFrame()
    imgLabels = []
    

    colSize = int(imgFrame.winfo_width()/(imageWidth+imageWidthPadding))
    rowSize = math.ceil(len(filepaths)/colSize)


    imageIndex = 0
    for imagePath in filepaths:

        curRow = 0 if colSize==0 else imageIndex // colSize
        curCol = 0 if colSize==0 else imageIndex % colSize

        load = Image.open(imagePath).resize((imageWidth, imageHeight), Image.LANCZOS)
        render = ImageTk.PhotoImage(load)
        img = Label(imgFrame, image=render)
        img.image = render
        img.grid(row=curRow,column=curCol,padx=imageHeightPadding,pady=imageWidthPadding,sticky=E+W+S+N)
        imgLabels.append(img)

        imageIndex += 1

# based on our images/labels recalculate sizes
def resizeImageArray(event):
    global dragging
    if dragging: return
    newWidth = event.width
    colSize = int(newWidth/(imageWidth+imageWidthPadding))

    for i, label in enumerate(imgLabels):

        curRow = 0 if colSize==0 else i // colSize
        curCol = 0 if colSize==0 else i % colSize

        label.grid(row=curRow,column=curCol,padx=imageHeightPadding,pady=imageWidthPadding,sticky=E+W+S+N)


def clearImgFrame():
    for widget in imgFrame.winfo_children():
        widget.destroy()

def initalizeImageArrayFrame():
    global imgFrame
    imgFrame = Frame(root, bg="red")
    return imgFrame