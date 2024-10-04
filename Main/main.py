import tkinter as tk
from net_backup import back_up
import sqlite3


### functions 

def send_form():

    input_form = {
        "name": name_input.get(),
        "ip": ip_input.get(),
        "username": username_input.get(),
        "password": password_input.get(),
        "secret": secret_input.get(),
        "filepath": filepath_input.get()
    }
    try:
        back_up(input_form["ip"], input_form["username"], input_form["password"], input_form["secret"], input_form["filepath"])
    except:
        pass
    conn = sqlite3.connect("devices.db")
    c= conn.cursor()
    c.execute("INSERT INTO devices VALUES (:name, :ip, :username, :password, :secret, :filepath)",
              
              {
                "name": name_input.get(),
                "ip": ip_input.get(),
                "username": username_input.get(),
                "password": password_input.get(),
                "secret": secret_input.get(),
                "filepath": filepath_input.get()  
              }
              )
    conn.commit()
    conn.close()

    name_input.delete(0, tk.END)
    ip_input.delete(0, tk.END)
    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    secret_input.delete(0, tk.END)
    filepath_input.delete(0, tk.END)
 




def search_db():
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    devices = c.execute("SELECT * FROM devices")
    conn.close
    return devices


### tkinter gui

root = tk.Tk()


root.geometry("1000x600")
root.title("Network-Auto-Backup (NAB)")


add_new_device_label = tk.Label(root, text="Add New Device")
add_new_device_label.grid(row=0, column=0)

name_label = tk.Label(root, text="Device Name")
name_label.grid(row=1, column=0)
name_input = tk.Entry(root, width=20)
name_input.grid(row=2, column=0)

ip_label = tk.Label(root, text="IP Adress")
ip_label.grid(row=3, column=0)
ip_input = tk.Entry(root, width=20)
ip_input.grid(row=4, column=0)


username_label = tk.Label(root, text="username")
username_label.grid(row=5, column=0)
username_input = tk.Entry(root, width=20)
username_input.grid(row=6, column=0)

password_label = tk.Label(root, text="password")
password_label.grid(row=7, column=0)
password_input = tk.Entry(root, width=20)
password_input.grid(row=8, column=0)

secret_label = tk.Label(root, text="secret")
secret_label.grid(row=9, column=0)
secret_input = tk.Entry(root, width=20)
secret_input.grid(row=10, column=0)

filepath_label = tk.Label(root, text="filepath")
filepath_label.grid(row=11, column=0)
filepath_input = tk.Entry(root, width=60)
filepath_input.grid(row=12, column=0)

input_btn = tk.Button(root, text="Submit", command=send_form)
input_btn.grid(row=13, column=0)


#y = 0
#for o in search_db():
 #   y = y + 1
#
 #   frame1 = tk.Frame(root)
#
 #   label1 = tk.Label(frame1, text="DEVICE", font="Helvetica 18 bold")
  #  label1.grid(row=y, column=1)
#
 #   label3 = tk.Label(frame1, text=o)
  #  label3.grid(row=y+1, column=1)




    #back_up_button = tk.Button(frame1, text="Back up")
   # back_up_button.grid(row=y+1, column=2)
    #delete_button = tk.Button(frame1, text="Delete")
    #delete_button.grid(row=y+1, column=3)

    #frame1.grid(row=y, column=2)

try:

    ### create or connect to db

    conn = sqlite3.connect("devices.db")

    ### create curser
    c = conn.cursor()

    ## create table

    c.execute("""CREATE TABLE devices (
            name text,
            ip text,
            username text,
            password text,
            secret text,
            filepath text
            )""")

    conn.commit()

except:
    pass

root.mainloop()

