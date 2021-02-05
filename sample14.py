from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("CheckBoxes")
root.geometry("600x600")

var = IntVar()
#var = StringVar()


c = Checkbutton(root, text="Check this box!", variable=var)# onvalue="on",offvalue="off"
c.deselect()#this fix the string ERROR
c.pack()


# on button click we see 1 if checked and 0 if not, We can do it too with strings too but we can find some ERRORS
def show():
    lbl = Label(root,text=var.get()).pack()

btn = Button(root, text="Check",command=show).pack()


root.mainloop()


#CHECKBOXES