from tkinter import *
from PIL import ImageTk, Image

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





root = Tk()

#  build img array frame
imgFrame = Frame(root)
imgFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


load = Image.open("a.jpg").resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
imgA = Label(imgFrame, image=render)
imgA.image = render
imgA.grid(row=0,column=0,padx=5,pady=5,sticky=E+W+S+N)

load = Image.open("b.png").resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
imgB = Label(imgFrame, image=render)
imgB.image = render
imgB.grid(row=0,column=1,padx=5,pady=5,sticky=E+W+S+N)

load = Image.open("c.jpg").resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
imgC = Label(imgFrame, image=render)
imgC.image = render
imgC.grid(row=1,column=0,padx=5,pady=5,sticky=E+W+S+N)

# https://stackoverflow.com/questions/66582100/how-to-swap-widget-placement-in-a-tkinter-grid-using-drag-and-drop
# myTextLabel1 = Label(root,text="Label 1",bg='yellow')
# # imgA.grid(row=0,column=0,padx=5,pady=5,sticky=E+W+S+N)

# myTextLabel2 = Label(root,text="Label 2",bg='lawngreen')
# # imgB.grid(row=1,column=0,padx=5,pady=5,sticky=E+W+S+N)

root.bind("<Button-1>",on_click)


root.mainloop()