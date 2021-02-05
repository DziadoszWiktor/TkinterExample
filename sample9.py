from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio Buttons")

r = IntVar()
r.set("2")#setting a choice

def clicked(value):
    lab = Label(root, text=value).pack()


Radiobutton(root, text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 3",variable=r,value=3,command=lambda:clicked(r.get())).pack()
my_button = Button(root, text="Click Me",command=lambda:clicked(r.get())).pack()

lab = Label(root, text=r.get()).pack()


root.mainloop()


#RADIO BUTTONS