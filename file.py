import mysql.connector
from tkinter import *
from tkinter import messagebox as mb
from tkinter import *
import datetime
import os


db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

def disp():
    selction = var.get()
    if selction == 1:
        cursor.execute("SELECT id FROM admin")

        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)

            liName.insert(END, str(cursor.rowcount) + " rows")


        cursor.execute("SELECT fullname FROM admin")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

            liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM admin")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)
            liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM admin")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logintime FROM admin")

        tUn = cursor.fetchall()
        for x in tUn:
            LiTi.insert(END, x)
            LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logouttime FROM admin")

        d = cursor.fetchall()
        for x in d:
            LiT0.insert(END, x)
            LiT0.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT id FROM users")

        timeIn = cursor.fetchall()
        for x in timeIn:
            liName.insert(END, x)
            liName.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT fullname FROM users")

        timeout = cursor.fetchall()
        for x in timeout:
            liD.insert(END, x)
            liD.insert(END, str(cursor.rowcount) + " rows")

    elif selction == 2:
        cursor.execute("SELECT id FROM users")
        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)


        cursor.execute("SELECT fullname FROM users")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        cursor.execute("SELECT username FROM users")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)


        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)


        cursor.execute("SELECT logintime FROM users")

        tUn = cursor.fetchall()
        for x in tUn:
            LiTi.insert(END, x)

        cursor.execute("SELECT logouttime FROM users")

        d = cursor.fetchall()
        for x in d:
            LiT0.insert(END, x)


        cursor.execute("SELECT id FROM users")

        timeIn = cursor.fetchall()
        for x in timeIn:
            liName.insert(END, x)


        cursor.execute("SELECT fullname FROM users")

        timeout = cursor.fetchall()
        for x in timeout:
            liD.insert(END, x)


def add():
    selction = var.get()
    if selction == 1:
        comm3 = "INSERT INTO admin (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "Admin created successfully")

    elif selction == 2:
        comm3 = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "User created successfully")


def delete():
    selction = var.get()
    if selction == 1:
        fullname=usrName.get()
        Delete="delete from admin where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information","Record Deleted")

    elif selction == 2:
        fullname = usrName.get()
        Delete = "delete from users where full_name='%s'" % (fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information", "Record Deleted")

def clear():
    liName.delete(0,END)
    liD.delete(0,END)
    liT.delete(0,END)
    liP.delete(0,END)
    Lid.delete(0,END)
    LiTi.delete(0, END)
    LiT0.delete(0,END)



def grant():
    selection = var.get()
    if selection == 1:
        u = usrName.get()
        priv_com = "GRANT ALL PRIVILEGES ON books.authors  TO '%s'@'localhost'" % (u)
        cursor.execute(priv_com)
        mb.showinfo("Message", "Privileges Granted")
    elif selection >=2:
        mb.showerror("Attention", "Admin users online")

def count():

    selection = var.get()
    if selection == 1:
        cursor = db.cursor()
        query = "SELECT count(*) FROM admin"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of admin users logged in\n',(myresult[-1][-1]))
        mb.showinfo("Attention", total)
    elif selection == 2:
        cursor = db.cursor()
        query = "SELECT count(*) FROM users"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of users logged in\n', (myresult[-1][-1]))
        mb.showinfo("Attention", total)

def dump():
    pass


admin = Tk()
admin.resizable(False, False)
admin.title("Admin Page")


panel = Label(admin, width=800, bg="black")
panel.place(x=20, y=0)





liLb = Label(admin, text="ID:", fg="black", bg="yellow")
liName = Listbox(admin, width=20)
li2Lb = Label(admin, text="Fullname:", fg="black", bg="yellow")
liD = Listbox(admin, width=20)
liTL = Label(admin, text="Username", fg="black", bg="yellow")
liT = Listbox(admin, width=20)
liLp = Label(admin, text="Password:",fg="black", bg="yellow")
liP = Listbox(admin, width=20)


#######################################
#lbU = Label(admin, text="Username:",fg="black", bg="yellow")
#Liu = Listbox(admin, width=20)
Lid = Listbox(admin, width=20)
LiTiL = Label(admin, text="Login Time:", fg="black", bg="yellow")
LiTi = Listbox(admin, width=20)
LiOl = Label(admin, text="Logout Time:", fg="black", bg="yellow")
LiT0 = Listbox(admin, width=20)


#Entries
nameRegLb = Label(admin, text="Full Name:",fg="black", bg="yellow")
nameReg = Entry(admin)
usrNamelb = Label(admin, text="Username:",fg="black", bg="yellow")
psswrdlb = Label(admin, text="Password:",fg="black", bg="yellow")

usrName = Entry(admin)
psswrd = Entry(admin, show='*')



liLb.place(x=20, y=100)
liName.place(x=20, y=130)
li2Lb.place(x=200, y=100)
liD.place(x=200, y=130)
liTL.place(x=380, y=100)
liT.place(x=380, y=130)
liLp.place(x=20, y=320)
liP.place(x=20, y=350)
#lbU.place(x=560, y=320)
#lbD.place(x=20, y=320)
#Lid.place(x=20, y=350)
LiTiL.place(x=200, y=320)
LiTi.place(x=200, y=350)
LiOl.place(x=380, y=320)
LiT0.place(x=380, y=350)

nameRegLb.place(x=20, y=50)
nameReg.place(x=100, y=50)
usrNamelb.place(x=275, y=50)
usrName.place(x=355, y=50)
psswrdlb.place(x=530, y=50)
psswrd.place(x=610, y=50)


#Buttons

showbtn = Button(admin, text="Display",width=5, command=disp, bd=2)
addbtn = Button(admin, text="Add", width=5, bd=2, command=add)
removebtn = Button(admin, text="Delete", width=5, bd=2, command=delete)
updatebtn = Button(admin, text="Clear", width=5, bd=2, command=clear)
grantbtn = Button(admin, text="Grant", width=5, bd=2, command=grant)
quitbtn = Button(admin, text="Count", width=5, bd=2, command=count)
backup = Button(admin, text="Back-up", width=22, fg="black", command=dump)
showbtn.place(x=560, y=130)
addbtn.place(x=560, y=180)
removebtn.place(x=560, y=230)
updatebtn.place(x=560, y=280)
grantbtn.place(x=560, y=330)
quitbtn.place(x=560, y=380)
backup.place(x=560, y=420)


var = IntVar()
admin_radio = Radiobutton(admin, text="admin", variable=var, value=1, fg="white", bg="red")
admin_radio.place(x=20, y=10)


user_radio = Radiobutton(admin, text="Users", variable=var, value=2, fg="white", bg="red")
user_radio.place(x=130, y=10)



#Center gui on screen

window_height = 600
window_width = 800

screen_width = admin.winfo_screenwidth()
screen_height = admin.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

admin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
admin.geometry("800x600")
admin.configure(bg="yellow")
admin.mainloop()
