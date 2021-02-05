from tkinter import *

root = Tk()

label1 = Label(root, text="Hello Wik! ", background="white", font=(["Helvetica"],20))
label2 = Label(root, text="How are you? ", background="white", font=(["Helvetica"],20))
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.geometry("600x600")
root.mainloop()

#GRID