from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

#showinfo ("ok") , showarning ("ok") , showerror ("ok") , askquestion , askokcancel ("yes" or "cancel") , askyesno (1 or 0)
def popup():
    response = messagebox.askyesno("This is my PopUp","Hello World!")
    if response == 1:
        Label(root,text="You clicked yes! ").pack()
    else:
        Label(root,text="You clicked no! ").pack()

Button(root, text="Popup",command=popup).pack()


root.mainloop()


#MESSAGES BOXES