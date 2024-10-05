import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

frame2 = tk.Frame(root)

my_tree = ttk.Treeview(frame2)




#colums
my_tree["columns"] = ("name", "ip", "username")

#format colums
my_tree.column("#0", width=0, stretch="no")
my_tree.column("name", anchor="w", minwidth=25,  width=120)
my_tree.column("ip", anchor="w", minwidth=25,  width=120)
my_tree.column("username", anchor="w", minwidth=25,  width=120 )


#headings

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("name", text="Name", anchor="w")
my_tree.heading("ip", text="IP", anchor="w")
my_tree.heading("username", text="Username", anchor="w")

#add data

my_tree.insert(parent="", index="end", iid=0, text="", values=("switch1", "192.168.1.2", "cisco"))
my_tree.insert(parent="", index="end", iid=1, text="", values=("switch2", "192.168.1.3", "cisco"))
my_tree.insert(parent="", index="end", iid=2, text="", values=("switch3", "192.168.1.4", "cisco"))
my_tree.insert(parent="", index="end", iid=3, text="", values=("switch4", "192.168.1.5", "cisco"))

my_tree.pack()

frame2.pack()

root.mainloop()