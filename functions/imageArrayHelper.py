from tkinter import *
from PIL import ImageTk, Image
import math

root = None
colSize = 0
rowSize = 0
imgFrame = None

imageWidth = 200
imageHeight = 300
imageWidthPadding = 5
imageHeightPadding = 5

imgLabels = []

dragging = False

def setImgArrRoot(rootIn):
    global root 
    root = rootIn

def changeOrder(widget1,widget2,initial):
    target=widget1.grid_info()
    widget1.grid(row=initial['row'],column=initial['column'])
    widget2.grid(row=target['row'],column=target['column'])

def on_click(event):
    widget=event.widget
    print(widget) 
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


def buildImageArray(filepaths):
    clearImgFrame()
    global imgLabels
    imgLabels = []
    global colSize, rowSize
    colSize = int(imgFrame.winfo_width()/(imageWidth+imageWidthPadding))
    rowSize = math.ceil(len(filepaths)/colSize)

    #imgFrame.grid(column=colSize, row=rowSize, sticky=(N, W, E, S))


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

def resizeImageArray(event):
    global dragging
    if dragging: return
    print("s")
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
    # imgFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    return imgFrame