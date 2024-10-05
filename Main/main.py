import tkinter as tk
from net_backup import back_up
import sqlite3
from tkinter import ttk


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
    
    #insert

    for d in search_last_record():
        my_tree.insert(parent="", index="end", iid=d[6], text="", values=(d[0], d[1], d[2], d[5]))




def search_last_record():
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    device = c.execute("SELECT *, oid FROM devices ORDER BY oid DESC LIMIT 1")
    return device

def search_db():
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    devices = c.execute("SELECT *, oid FROM devices")
    return devices


def delete_record():
    d = my_tree.selection()[0]
    print(d)
    my_tree.delete(d)
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM devices WHERE oid = {d}")
    conn.commit()
    conn.close()



### tkinter gui

root = tk.Tk()


root.geometry("1000x600")
root.title("Network-Auto-Backup (NAB)")

frame1 = tk.Frame(root)

add_new_device_label = tk.Label(frame1, text="Add New Device")
add_new_device_label.grid(row=0, column=0)

name_label = tk.Label(frame1, text="Device Name")
name_label.grid(row=1, column=0)
name_input = tk.Entry(frame1, width=20)
name_input.grid(row=2, column=0)

ip_label = tk.Label(frame1, text="IP Adress")
ip_label.grid(row=3, column=0)
ip_input = tk.Entry(frame1, width=20)
ip_input.grid(row=4, column=0)


username_label = tk.Label(frame1, text="username")
username_label.grid(row=5, column=0)
username_input = tk.Entry(frame1, width=20)
username_input.grid(row=6, column=0)

password_label = tk.Label(frame1, text="password")
password_label.grid(row=7, column=0)
password_input = tk.Entry(frame1, width=20)
password_input.grid(row=8, column=0)

secret_label = tk.Label(frame1, text="secret")
secret_label.grid(row=9, column=0)
secret_input = tk.Entry(frame1, width=20)
secret_input.grid(row=10, column=0)

filepath_label = tk.Label(frame1, text="filepath")
filepath_label.grid(row=11, column=0)
filepath_input = tk.Entry(frame1, width=40)
filepath_input.grid(row=12, column=0)

input_btn = tk.Button(frame1, text="Submit", command=send_form)
input_btn.grid(row=13, column=0)

frame1.grid(row=0, column=0)



frame2 = tk.Frame(root, padx=100)

my_tree = ttk.Treeview(frame2)




#colums
my_tree["columns"] = ("name", "ip", "username", "filepath")

#format colums
my_tree.column("#0", width=0, stretch="no")
my_tree.column("name", anchor="w", minwidth=25,  width=120)
my_tree.column("ip", anchor="w", minwidth=25,  width=120)
my_tree.column("username", anchor="w", minwidth=25,  width=120 )
my_tree.column("filepath", anchor="w", minwidth=25,  width=120 )


#headings

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("name", text="Name", anchor="w")
my_tree.heading("ip", text="IP", anchor="w")
my_tree.heading("username", text="Username", anchor="w")
my_tree.heading("filepath", text="Filepath", anchor="w")

#add data
for d in search_db():
    my_tree.insert(parent="", index="end", iid=d[6], text="", values=(d[0], d[1], d[2], d[5]))

my_tree.grid()

frame2.grid(row=0, column=1)


frame3 = tk.Frame(root, pady=20)

btn_backup = tk.Button(frame3, text="Back Up")
btn_backup.grid()

btn_remove = tk.Button(frame3, text="Delete", command=delete_record)
btn_remove.grid()

frame3.grid(row=1, column=1)






















#elist = []
#for e in search_db():
#    mydict = {"id": e[6], "name": e[0], "ip": e[1], "username": e[2], "password": e[3], "secret": e[4], "filepath": e[5]}
#    elist.append(mydict)

   



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

