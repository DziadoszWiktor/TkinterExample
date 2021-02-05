from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.title("Open Files Dialog Box")

#this variable return a location
#root.filename = filedialog.askopenfilename(initialdir="imgs",title="File",filetypes=(("text files","*.txt"),("all files","*.*")))
#this label return an image of imgs dir
#my_label = Label(root,text=root.filename).pack()
#my_img = ImageTk.PhotoImage(Image.open(root.filename))
#my_label_img = Label(root,image=my_img).pack()

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="imgs",title="File",filetypes=(("text files","*.txt"),("all files","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label_img = Label(root,image=my_img).pack()

file_btn = Button(root,text="File",command=open).pack()

root.mainloop()

#OPEN FILES DIALOG BOX - searching a file trought the pc files