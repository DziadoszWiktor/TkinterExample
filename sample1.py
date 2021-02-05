from tkinter import *

root = Tk()

# Looped windows opening
# for x in range(40):
#     root = Tk()
#     root.geometry("600x600")

label = Label(root, text="Hello Wik! ", background="white", font=(["Helvetica"],20))

label.pack()# .pack() and .grid() 

root.geometry("600x600")
root.mainloop()

#INTRO