import tkinter as tk
from net_backup import back_up
import sqlite3
from tkinter import ttk, messagebox
from datetime import datetime, time
import asyncio
from time import sleep
import time
import threading

#functions

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
    my_tree.delete(d)
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM devices WHERE oid = {d}")
    conn.commit()
    conn.close()

def find_back_up_device():
    d = my_tree.selection()[0]
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    device = c.execute(f"SELECT *, oid FROM devices WHERE oid = {d}")
    return device

def update_record(bool):
    d = my_tree.selection()[0]
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()

    dt = str(datetime.now())
    print(dt)
    dt = dt.replace(" ", "")
    print(dt)
    dt = dt.replace(":", "-")
    print(dt)

    c.execute(f" UPDATE devices SET backed_up = {bool}, date1 = {dt} WHERE oid = {d}")
    conn.close()

def update_record1(date1, id):
<<<<<<< HEAD
        conn = sqlite3.connect("devices.db")
        c = conn.cursor()

        dt = str(datetime.now())
        dt = dt.replace(" ", "")
        dt = dt.replace(":", "-")
        


        c.execute(f"UPDATE devices SET date1 = {dt} WHERE oid = {id}")
        conn.commit()
        c.close()
        conn.close()
=======
    conn = sqlite3.connect("devices.db")
    c = conn.cursor()
    c.execute(f"UPDATE devices SET date1 = {date1} WHERE oid = {id}")
    conn.commit()
    c.close()
    conn.close()
>>>>>>> 894aa887b6478177edac80f13b8b7cfc488807cc

def refresh_view():
    my_tree.delete(*my_tree.get_children())
    for d in search_db():
        my_tree.insert(parent="", index="end", iid=d[9], text="", values=(d[0], d[1], d[2], d[5],d[6], d[7], f"Every {d[8]} days" ))

        
def back_up1():
        for d in find_back_up_device():

            try:
                back_up(d[1], d[2], d[3], d[4], d[5], datetime.now())
                update_record(True)
                refresh_view()
                messagebox.showinfo(title="Back Up Success", message="Back Up Success")
            except:
                update_record(False)
                refresh_view()
                messagebox.showinfo(title="Back Up Failure", message="Back Up Failure")




###this is the main tkinter gui function

def main_func():

    ## create db

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
                filepath text,
                backed_up boolean,
                date1 text,
                schedule integer
                )""")

        conn.commit()

    except:
        pass






    ### functions 

    def send_form():

        input_form = {
            "name": name_input.get(),
            "ip": ip_input.get(),
            "username": username_input.get(),
            "password": password_input.get(),
            "secret": secret_input.get(),
            "filepath": filepath_input.get(),
        }
        try:
<<<<<<< HEAD
            back_up(input_form["ip"], input_form["username"], input_form["password"], input_form["secret"], input_form["filepath"], datetime.now())
            conn = sqlite3.connect("devices.db")
            c = conn.cursor()
            c.execute("INSERT INTO devices VALUES (:name, :ip, :username, :password, :secret, :filepath, :backed_up, :date1, :schedule)",
                    
                    {
                        "name": name_input.get(),
                        "ip": ip_input.get(),
                        "username": username_input.get(),
                        "password": password_input.get(),
                        "secret": secret_input.get(),
                        "filepath": filepath_input.get(),
                        "backed_up": True,
                        "date1": datetime.now(),
                        "schedule": sch_input.get()
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
            sch_input.delete(0, tk.END)

            messagebox.showinfo(title="Back Up Success", message="Back Up Success")
        except:
    
            
=======
            back_up(d[1], d[2], d[3], d[4], d[5], datetime.now())
            update_record(True)
            refresh_view()
            messagebox.showinfo(title="Back Up Success", message="Back Up Success")
        except:
            update_record(False)
            refresh_view()
            messagebox.showinfo(title="Back Up Failure", message="Back Up Failure")
       
>>>>>>> 894aa887b6478177edac80f13b8b7cfc488807cc

            conn = sqlite3.connect("devices.db")
            c = conn.cursor()
            c.execute("INSERT INTO devices VALUES (:name, :ip, :username, :password, :secret, :filepath, :backed_up, :date1, :schedule)",
                    
                    {
                        "name": name_input.get(),
                        "ip": ip_input.get(),
                        "username": username_input.get(),
                        "password": password_input.get(),
                        "secret": secret_input.get(),
                        "filepath": filepath_input.get(),
                        "backed_up": False,
                        "date1": datetime.now(),
                        "schedule": sch_input.get()
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
            sch_input.delete(0, tk.END)

            messagebox.showinfo(title="Back Up Failed", message="Back Up Failed")
        
        #insert

        for d in search_last_record():
            my_tree.insert(parent="", index="end", iid=d[9], text="", values=(d[0], d[1], d[2], d[5], d[6], d[7], f"Every {d[8] } days" ))




    
        

    ### tkinter gui

    root = tk.Tk()



    root.geometry("1200x400")
    root.title("Network-Auto-Backup (NAB)")


    #Frame for form

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

    sch_label = tk.Label(frame1, text="Back Up Every: (days at midnight)")
    sch_label.grid(row=13, column=0)
    sch_input = tk.Entry(frame1, width=5)
    sch_input.grid(row=14, column=0)

    input_btn = tk.Button(frame1, text="Submit", command=send_form)
    input_btn.grid(row=15, column=0)

    frame1.grid(row=0, column=0)


    #frame for treeview

    frame2 = tk.Frame(root, padx=100)

    global my_tree
    
    my_tree = ttk.Treeview(frame2)

    





    #colums
    my_tree["columns"] = ("name", "ip", "username", "filepath", "backed_up", "date", "schedule")

    #format colums
    my_tree.column("#0", width=0, stretch="no")
    my_tree.column("name", anchor="w", minwidth=25,  width=120)
    my_tree.column("ip", anchor="w", minwidth=25,  width=120)
    my_tree.column("username", anchor="w", minwidth=25,  width=120 )
    my_tree.column("filepath", anchor="w", minwidth=25,  width=120 )
    my_tree.column("backed_up", anchor="w", minwidth=10,  width=70 )
    my_tree.column("date", anchor="w", minwidth=25,  width=120 )
    my_tree.column("schedule", anchor="w", minwidth=25,  width=120 )

    #headings

    my_tree.heading("#0", text="", anchor="w")
    my_tree.heading("name", text="Name", anchor="w")
    my_tree.heading("ip", text="IP", anchor="w")
    my_tree.heading("username", text="Username", anchor="w")
    my_tree.heading("filepath", text="Filepath", anchor="w")
    my_tree.heading("backed_up", text="Back Up", anchor="w")
    my_tree.heading("date", text="Last Back Up Attempt", anchor="w")
    my_tree.heading("schedule", text="Schedule", anchor="w")


    #adds data from db
    for d in search_db():
        my_tree.insert(parent="", index="end", iid=d[9], text="", values=(d[0], d[1], d[2], d[5],d[6], d[7], f"Every {d[8]} days" ))

    my_tree.grid()

    frame2.grid(row=0, column=1)


    #button frame

    frame3 = tk.Frame(root, pady=20)

    btn_backup = tk.Button(frame3, text="Back Up", command=back_up1)
    btn_backup.grid()

    btn_remove = tk.Button(frame3, text="Delete", command=delete_record)
    btn_remove.grid()

    frame3.grid(row=1, column=1)

    root.mainloop()



#automatic back ups daily at midnight
def auto_back_up():
    is_running = True
    while is_running:

        #check time
        now = datetime.now()
        now = str(now)
        now = now.rsplit(" ")
        now[1] = now[1][0:2]
        now[0] = now[0][-2:]
        t = now[1]

        #if time is 12 then back up

        if t == "13":

            #for every entry, back up
            for d in search_db():
                try:
                    back_up(d[1], d[2], d[3], d[4], d[5], datetime.now())
                    print("backed up!")
                except:
                    print("failed backed up!")
                
                update_record1(id=d[9], date1=datetime.now())
                refresh_view()
            time.sleep(3600)


x = threading.Thread(target=main_func, args=())
x1 = threading.Thread(target=auto_back_up, args=())

x.start()
x1.start()


<<<<<<< HEAD
=======
    for d in search_db():
        completed = False
        if now[1] == "05" and completed == False :
            try:
                back_up(d[1], d[2], d[3], d[4], d[5], datetime.now())
                print("backed up!")
            except:
                pass
        
        
            dt = str(datetime.now())
            dt = dt.replace(" ", "")
            dt = dt.replace(":", "-")
            
            update_record1(id=d[9], date1=dt)
        completed = True
    refresh_view()
>>>>>>> 894aa887b6478177edac80f13b8b7cfc488807cc



auto_back_up()


