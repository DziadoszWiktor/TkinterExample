from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("Window")
#ICON
root.iconbitmap('C:/Users/User/Downloads/jdm.ico')#must be .ico not .jpg or.png
root.geometry("600x600")

#BUTTON QUIT
button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack()

#IMAGES (tkinter support old photos extentions so we have to install Pillow module)
my_img = ImageTk.PhotoImage(Image.open("C:/Users/User/Pictures/Saved Pictures/jdm.jpg"))
my_label = Label(image=my_img)
my_label.pack()



root.mainloop()

#ICONS,IMAGES AND EXIT BUTTONS 