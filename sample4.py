from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="white", borderwidth=5, )
e.pack()
#e.insert(0, "Enter your name: ") default words in the input field
#e.get() get the text from input to use it in the label(click function) replacing the text string "You clicked the button! "

def Clickme():
    label = Label(root, text="Hello "+e.get()+" !")
    label.pack()

button1 = Button(root, text="Done", command=Clickme)
button1.pack()

root.geometry("600x600")
root.mainloop()


#INPUT FIEDLS