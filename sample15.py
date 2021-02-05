from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Dropdown Menu")
root.geometry("600x600")

def show():
    lbl = Label(root, text=clicked.get()).pack()

options = [
    "File",
    "Save",
    "Save As",
    "Help"
    ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text="Show selection",command=show).pack()

root.mainloop()


#DROP DOWN MENU