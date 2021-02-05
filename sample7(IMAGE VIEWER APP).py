from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer App")
root.iconbitmap("AppViewerIcon.ico")

image1 = ImageTk.PhotoImage(Image.open("imgs/supra1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("imgs/supra2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("imgs/supra3.jpg"))

img_list = [image1,image2,image3]

#status bar
status_label = Label(root,text="Image 1 of "+str(len(img_list)), bd=1, relief=SUNKEN,anchor=E)#anchor E put the label in the low right angle

my_label = Label(image=image1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(n):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()#first image desappear
    my_label = Label(image=img_list[n-1])
    button_forward = Button(root,text=" >> ",command=lambda:forward(n+1))
    button_back = Button(root,text=" << ",command=lambda:back(n-1))

    if n == len(img_list):
        button_forward = Button(root,text=" >> ",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #Uptading status bar
    status_label = Label(root,text="Image "+str(n)+" of "+str(len(img_list)), bd=1, relief=SUNKEN,anchor=E)
    status_label.grid(row=2,column=0,columnspan=3, sticky=W+E)

def back(n):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[n-1])
    button_forward = Button(root,text=" >> ",command=lambda:forward(n+1))
    button_back = Button(root,text=" << ",command=lambda:back(n-1))

    if n == 1:
        button_back = Button(root,text=" << ",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #Uptading status bar
    status_label = Label(root,text="Image "+str(n)+" of "+str(len(img_list)), bd=1, relief=SUNKEN,anchor=E)
    status_label.grid(row=2,column=0,columnspan=3, sticky=W+E)

button_back = Button(root,text=" << ",command=back,state=DISABLED)
button_forward = Button(root,text=" >> ",command=lambda:forward(2))
button_exit = Button(root,text=" Quit ", command=root.quit)

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_exit.grid(row=1,column=1)

status_label.grid(row=2,column=0,columnspan=3, sticky=W+E)

root.mainloop()