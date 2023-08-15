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
emptyImgArrIndex = -1

def setImgArrRoot(rootIn):
    global root 
    root = rootIn

def moveToEmpty(widget1):
    global emptyImgArrIndex
    target=imgLabels[emptyImgArrIndex].grid_info()
    if target == {}: return
    imgLabels.pop(emptyImgArrIndex).destroy()
    imgLabels.insert(emptyImgArrIndex, widget1)
    emptyImgArrIndex = -1
    widget1.grid(row=target['row'],column=target['column'])

def on_click_img_arr(event):
    widget=event.widget
    if isinstance(widget,Label):
        start=(event.x,event.y)
        
        originIndex = imgLabels.index(widget)
        imgLabels.pop(imgLabels.index(widget))
        reprintImgArr()

        widget.bind("<B1-Motion>",lambda event:drag_motion(event,widget,start))
        widget.bind("<ButtonRelease-1>",lambda event:drag_release(event,widget,originIndex))
    else:
        root.unbind("<ButtonRelease-1>")

def drag_motion(event,widget,start):
    global dragging, imgLabels
    dragging = True
    x = widget.winfo_x()+event.x-start[0]
    y = widget.winfo_y()+event.y-start[1] 
    widget.lift()
    widget.place(x=x,y=y)

    # find next two closest widgets
    # get X midpoint of image and find the closests two widgets
    mouseX,mouseY=root.winfo_pointerxy()
    maxX = root.winfo_width() #minX obviously 0

    # find widgets to the left and right and make an empty space
    target_widget_right = None
    for newX in range(widget.winfo_rootx()+widget.winfo_width()+1, maxX, widget.winfo_width()):
        potential_right_widget = root.winfo_containing(newX,mouseY)
        if isinstance(potential_right_widget,Label):
            target_widget_right = potential_right_widget
            break

    target_widget_left = None
    for newX in range(widget.winfo_rootx()-1, 0, -widget.winfo_width()):
        potential_left_widget = root.winfo_containing(newX,mouseY)
        if isinstance(potential_left_widget,Label):
            target_widget_left = potential_left_widget
            break
        


    if(target_widget_left != None and target_widget_right != None):
        insertEmptyImgArr(imgLabels.index(target_widget_left))
    elif(target_widget_left != None):
        insertEmptyImgArr(imgLabels.index(target_widget_left))
    elif(target_widget_right != None):
        if(imgLabels.index(target_widget_right)-1 != -1):
            insertEmptyImgArr(imgLabels.index(target_widget_right)-1)
        else:
            insertEmptyImgArr(0)
    else:
        lowest = imgLabels[0].winfo_rooty()
        highest = imgLabels[-1].winfo_rooty()
        if(mouseY < lowest):
            insertEmptyImgArr(0)
        elif(mouseY > highest):
            insertEmptyImgArr(len(imgLabels)-1)


def drag_release(event,widget,originIndex):
    global dragging
    
    widget.lower()
    if emptyImgArrIndex != -1:
        moveToEmpty(widget)
    else:
        imgLabels.insert(originIndex, widget)
    dragging = False
    reprintImgArr()


# inserts an empty img at the index of label and moves everything to the right
# if -1 then remove emptyImgArr
def insertEmptyImgArr(index):
    global emptyImgArrIndex, imgLabels
    if(index != -1 and emptyImgArrIndex == -1):
        emptyImgArrIndex = index
        imgLabels.insert(emptyImgArrIndex, Label(imgFrame))
        print("creating a empty at ", index)
    elif(index != -1 and emptyImgArrIndex != -1 and index != emptyImgArrIndex):
        imgLabels.pop(emptyImgArrIndex).destroy()
        emptyImgArrIndex = index
        imgLabels.insert(emptyImgArrIndex, Label(imgFrame))
        print("replacing our empty and moving it to ", index)
    elif(emptyImgArrIndex != -1 and index == -1):
        imgLabels.pop(emptyImgArrIndex).destroy()
        emptyImgArrIndex = index
        print("removing empty")
    else:
        return
    reprintImgArr()

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
        img.filepath = imagePath
        img.grid(row=curRow,column=curCol,padx=imageHeightPadding,pady=imageWidthPadding,sticky=E+W+S+N)
        imgLabels.append(img)

        imageIndex += 1

def reprintImgArr():

    colSize = int(imgFrame.winfo_width()/(imageWidth+imageWidthPadding))
    for i, label in enumerate(imgLabels):

        curRow = 0 if colSize==0 else i // colSize
        curCol = 0 if colSize==0 else i % colSize

        label.grid(row=curRow,column=curCol,padx=imageHeightPadding,pady=imageWidthPadding,sticky=E+W+S+N)



# based on our images/labels recalculate num of image sin rows/cols
def resizeImgArrEvent(event):
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