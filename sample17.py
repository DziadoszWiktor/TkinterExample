from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Database App")
root.geometry("600x600")

#Text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)

address= Entry(root,width=30)
address.grid(row=2,column=1)
 
city = Entry(root,width=30)
city.grid(row=3,column=1)

stat = Entry(root,width=30)
stat.grid(row=4,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

#Text box labels

f_name_label = Label(root,text="First name")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root,text="Last name")
l_name_label.grid(row=0,column=0)

address_label = Label(root,text="Address")
address_label.grid(row=0,column=0)

city_label = Label(root,text="City")
city_label.grid(row=0,column=0)

stat_label = Label(root,text="State")
stat_label.grid(row=0,column=0)

zipcode_label = Label(root,text="Zip Code")
zipcode_label.grid(row=0,column=0)

root.mainloop()


#DATABASE APP