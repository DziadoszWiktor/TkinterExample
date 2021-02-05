from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("600x600")

conn = sqlite3.connect('address_book.db')#create a database
#create cursor
c = conn.cursor()
#create a table in the database
c.execute("""CREATE TABLE adresses (
        first_name text,
        last_name text,
        adress text,
        city text,
        stat text,
        zipcode integer
        )""")
#commit changes in the database
conn.commit()
#close connection
conn.close()


root.mainloop()


#DATABASES