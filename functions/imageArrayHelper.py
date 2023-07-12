from tkinter import *
from PIL import ImageTk, Image
import math

root = None
colSize = 0
rowSize = 0
imgFrame = None

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
    x = widget.winfo_x()+event.x-start[0]
    y = widget.winfo_y()+event.y-start[1] 
    widget.lift()
    widget.place(x=x,y=y)

def drag_release(event,widget,grid_info):
    widget.lower()
    x,y=root.winfo_pointerxy()
    target_widget=root.winfo_containing(x,y)
    if isinstance(target_widget,Label):
        changeOrder(target_widget,widget,grid_info)
    else:
        widget.grid(row=grid_info['row'],column=grid_info['column'])


def buildImageArray(filepaths):
    imgFrame = Frame(root)

    global colSize, rowSize
    colSize = 3
    rowSize = math.ceil(len(filepaths)/colSize)

    imgFrame.grid(column=colSize, row=rowSize, sticky=(N, W, E, S))


    imageIndex = 0
    for imagePath in filepaths:

        curRow = imageIndex // colSize
        curCol = imageIndex % colSize
        
        load = Image.open(imagePath).resize((200, 200), Image.LANCZOS)
        render = ImageTk.PhotoImage(load)
        img = Label(imgFrame, image=render)
        img.image = render
        img.grid(row=curRow,column=curCol,padx=5,pady=5,sticky=E+W+S+N)

        imageIndex += 1

def initalizeImageArrayFrame():
    global imgFrame
    imgFrame = Frame(root)
    imgFrame.grid(column=0, row=0, sticky=(N, W, E, S))