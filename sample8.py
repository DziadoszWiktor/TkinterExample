from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")

my_frame = LabelFrame(root, text="This is my farme",pady=5,padx=5)#pady,padx distance of the object and borders in the frame
my_frame.pack(padx=10,pady=10)#pady,padx distance of the object and borders out of the frame

b = Button(my_frame, text="Don't click there!")
b2 = Button(my_frame, text="Click there!")
b.grid(column=0,row=0)
b2.grid(column=1,row=1)




root.mainloop()

#FRAMES