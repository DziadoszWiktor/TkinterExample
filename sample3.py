from tkinter import *

root = Tk()

def myclick():
    label1 = Label(root, text="The button was clicked! ")
    label1.pack() 

button1 = Button(root, text="Click me! ", command=myclick, padx=50, pady=50, fg="red", bg="black")#padx and pady , height and width
button1.pack()#.grid(row=0,column=0)


root.geometry("600x600")
root.mainloop()

#BUTTONS