from tkinter import *
from PIL import ImageTk, Image
from functions.imageArrayHelper import *
from functions.topMenuHelper import buildMenubar, setTopMenuRoot

root = Tk()
setImgArrRoot(root)
setTopMenuRoot(root)


#  build img array frame
initalizeImageArrayFrame()

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

root.geometry("500x200")
# load = Image.open("a.jpg").resize((200, 200), Image.LANCZOS)
# render = ImageTk.PhotoImage(load)
# imgA = Label(imgFrame, image=render)
# imgA.image = render
# imgA.grid(row=0,column=0,padx=5,pady=5,sticky=E+W+S+N)

# load = Image.open("b.png").resize((200, 200), Image.LANCZOS)
# render = ImageTk.PhotoImage(load)
# imgB = Label(imgFrame, image=render)
# imgB.image = render
# imgB.grid(row=0,column=1,padx=5,pady=5,sticky=E+W+S+N)

# load = Image.open("c.jpg").resize((200, 200), Image.LANCZOS)
# render = ImageTk.PhotoImage(load)
# imgC = Label(imgFrame, image=render)
# imgC.image = render
# imgC.grid(row=1,column=0,padx=5,pady=5,sticky=E+W+S+N)

root.bind("<Button-1>",on_click)

root.config(menu=buildMenubar())

root.mainloop()