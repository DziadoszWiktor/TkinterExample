from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Sliders")


vertical = Scale(root, from_=0, to=600)
vertical.pack()

horizontal = Scale(root, from_=0, to=600, orient=HORIZONTAL)
horizontal.pack()

#slider_label = Label(root,text=horizontal.get()).pack()

# On button click will appear a label with the slider value and we can modfiy the window values(600x500)f.e.
def slide():
    slider_label = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

btn = Button(root,text="Click me!",command=slide).pack()


root.mainloop()

#SLIDERS (trigger)