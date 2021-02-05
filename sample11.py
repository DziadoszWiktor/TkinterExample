from tkinter import *
from PIL import ImageTk, Image

#main window
root = Tk()
root.title("First window")

#new window on button click
#(PH) in case f.e. an image we have to call a global variable first, cause pyhton cant't see a global variable in a function like the image path
def open():
    #(PH) global my_img
    top = Toplevel()
    top.title("Second window")
    top.geometry("600x600")
    #(PH) my_img = ImageTk.Photoimage(Image.open(*PHOTO PATH*))
    lambel1 = Label(top, text="Hello world!").pack()
    exit_btn = Button(top, text="Quit",command=top.destroy).pack()

btn = Button(root, text="Open new window",command=open).pack()

#new window
# top = Toplevel()
# top.title("Second window")
# lambel1 = Label(top, text="Hello world!").pack()


root.mainloop()

#NEW WINDOWS