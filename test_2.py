# Operators
from tkinter import *
import mysql.connector
from tkinter import messagebox
import sys
import os

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',database='lifechoicesonline')
my_cursor = mydb.cursor()
my_cursor.execute("create database if not exists lifechoicesonline")
mydb.commit()
my_cursor.execute("use lifechoicesonline")
mydb.commit()
my_cursor.execute("create table if not exists users (id int(11) NOT NULL auto_increment , username varchar(50) default null, password varchar(20) default null, fullname varchar(60) default null, logintime timestamp , logouttime timestamp, primary key(id))")
my_cursor.execute("create table if not exists admin (id int(11) NOT NULL auto_increment, username varchar(60) default null, password varchar(20) default null,  logintime timestamp , logouttime timestamp , fullname varchar(60) default null, primary key(id))")
mydb.commit()

#Home page
choices = Tk()
choices.title("Lifechoices Online")
choices.geometry("500x210")
choices.config(bg="yellow")



signup = Label(choices, text='Please sign in below')
signup.place(x=30, y=0)

Username = Label(choices, text='Username:')
Username.place(x=30, y=30)
Username_entry = Entry(choices, width=20)
Username_entry.place(x=300, y=30)

Password = Label(choices, text='Password:')
Password.place(x=30, y=60)
Password_entry = Entry(choices, width=20)
Password_entry.place(x=300, y=60)

# Login section
def login():
    user = Username_entry.get()
    password = Password_entry.get()
    sql = 'Select * from users where Username=%s and Password=%s'
    my_cursor.execute(sql, [(user), (password)])
    results = my_cursor.fetchall()

    if results:
        for i in results:

            messagebox.showinfo("Login Successful", "Enjoy your day")
            choices.withdraw()
            logout = Tk()

            def log_out():
                messagebox.showinfo("Attention", "LoggedOut")
                logout.destroy()
                import main


            log_btn=Button(logout,text="Logout", command=log_out)
            log_btn.pack()
            logout.mainloop()

    else:
        messagebox.showinfo("Incorrect Username or password", "Login Unsuccessful. Please try again")



B1 = Button(choices, text='Login', command=login)
B1.place(x=30, y=90)

Register = Label(choices, text='Not yet a member? Register here or sign in as a visitor')
Register.place(x=30, y=135)


# register Option
def register():
    choices.destroy()
    reg = Tk()
    reg.title('Register today!')
    reg.geometry("500x210")
    reg.config(bg='yellow')

    name_reg = Label(reg, text='Please enter your name')
    name_reg.place(x=30, y=30)
    name_ent = Entry(reg, width=20)
    name_ent.place(x=300, y=30)

    password_reg = Label(reg, text="Please set a password")
    password_reg.place(x=30, y=60)
    password_ent = Entry(reg, width=20)
    password_ent.place(x=300, y=60)

    user_reg = Label(reg, text='Please enter a username')
    user_reg.place(x=30, y=90)
    user_ent = Entry(reg, width=20)
    user_ent.place(x=300, y=90)



    def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)


    backbtn = Button(reg, text="back", command=restart)
    backbtn.pack()
    backbtn.place(x=30, y=170)


    def regis():
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
            host='localhost', database='lifechoicesonline')

        mycursor = mydb.cursor()

        x = name_ent.get()
        y = user_ent.get()
        z = password_ent.get()

        if x == '' or y == '' or z == '':
            messagebox.showerror("TRY AGAIN", "Please do not leave the fields empty")
            reg.destroy()
            register()

        else:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
            host='localhost', database='lifechoicesonline')

        try:
            mycursor = mydb.cursor()
            sql = "INSERT INTO users(fullname, username, password) VALUES(%s, %s, %s)"
            mycursor.execute(sql, [(x), (y), (z)])
            messagebox.showinfo("Register Successfull","SUCCESS, " + x + " has been added to the server")
            mydb.commit()
            reg.destroy()
        except:
            messagebox.showerror("OOPS", "Error connecting to databases")
            reg.destroy()
            register()

    registration = Button(reg, text='Register!', command=regis)
    registration.place(x=30, y=130)


Register_b = Button(choices, text='Register Here', command=register)
Register_b.place(x=30, y=170)


# sign in as a visitor
def visitor():
    choices.destroy()
    visitor = Tk()
    visitor.title('Sign in as a visitor!')
    visitor.geometry("500x210")
    visitor.config(bg='yellow')

    visit_reg = Label(visitor, text='Please enter your name')
    visit_reg.place(x=30, y=30)
    visit_ent = Entry(visitor, width=20)
    visit_ent.place(x=300, y=30)

    number_reg = Label(visitor, text="Please set a password")
    number_reg.place(x=30, y=60)
    number_ent = Entry(visitor, width=20)
    number_ent.place(x=300, y=60)

    def visiting():
        messagebox.showinfo('Signed in', 'You have been signed in')

    def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)


    backbtn = Button(visitor, text="back", command=restart)
    backbtn.pack()
    backbtn.place(x=30, y=150)
    visitorsign = Button(visitor, text='Sign in', command=visiting)
    visitorsign.place(x=30, y=90)


visitors = Button(choices, text='Visitors sign in', command=visitor)
visitors.place(x=300, y=170)

# A key assigned to admin section
def manage():
    import file

A_key = ""
def key():

    def admin_log():
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
        database='lifechoicesonline')
        my_cursor = mydb.cursor()
        username = admin_ent.get()
        password = adminp_ent.get()
        sql = 'Select * from admin where username = %s and password = %s'
        my_cursor.execute(sql, [username, password])
        results = my_cursor.fetchall()

        if results:
            sql = 'insert into admin where logintime = NOW() WHERE username = %s'
            my_cursor.execute(sql, [(username)])
            mydb.commit()
            admin.destroy()
            import file

        else:
            messagebox.showerror("error","incorrect details")




    global A_key
    choices.destroy()
    admin = Tk()
    admin.title('Admin Authorization')
    admin.geometry("500x210")
    admin.config(bg='yellow')

    admin_l = Label(admin, text='Admin User')
    admin_l.place(x=30, y=30)
    admin_ent = Entry(admin, width=20)
    admin_ent.place(x=300, y=30)

    adminp_reg = Label(admin, text="Password")
    adminp_reg.place(x=30, y=60)
    adminp_ent = Entry(admin, width=20)
    adminp_ent.place(x=300, y=60)

    adminb = Button(admin, text='Authorize', command=admin_log)
    adminb.place(x=30, y=100)

    lbl = Label(choices)
    lbl.place(x=0, y=1000)

choices.bind("<Control-a>", lambda x: key())

choices.mainloop()
