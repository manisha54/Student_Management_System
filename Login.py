from tkinter import *
from tkinter import messagebox
import os


def login_success():
    messagebox.showinfo(screen, "Login Success")
    screen2.destroy()
    import registration2
    registration2.main()


def password_not_recognised():
    messagebox.showwarning('ALERT', 'Invalid Password')


def user_not_found():
    messagebox.showwarning('ALERT', 'User not found')


def register_user():
    a = ''
    if username_entry.get() == a and password_entry.get() == a and password_entry2.get() == a:
        messagebox.showwarning('ALERT', 'All fields are required')
    elif username_entry.get() == a:
        messagebox.showwarning('ALERT', 'All fields are required')
    elif password_entry.get() == a:
        messagebox.showwarning('ALERT', 'Enter the password')
    elif password_entry2.get() == a:
        messagebox.showwarning('ALERT', 'Enter your password again')
    elif password_entry.get() != password_entry2.get():
        messagebox.showwarning('ALERT', "Sorry! Password donot match")

    else:
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "a+")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        screen1.destroy()
        screen.destroy()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    # os returns the list containing name of entries in the directory in the path
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x550")

    global bg2
    bg2 = PhotoImage(file="image1.png")
    label2 = Label(screen1, image=bg2)
    label2.place(x=0, y=0)

    frame3 = Frame(screen1, bd=3, width=0, bg='#33272a', padx=20, relief=RIDGE)
    frame3.place(x=50, y=30, width=300, height=450)

    global username
    global password
    global username_entry
    global password_entry
    global password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    Label(frame3, text="REGISTER HERE", fg="red", bg='#33272a', font=("francisco", 23)).place(x=0, y=20)
    Label(frame3, text="").pack()
    Label(frame3, text="Username  ", fg="red", bg='#33272a', font=("francisco", 18)).place(x=65, y=90)
    username_entry = Entry(frame3, width=30, textvariable=username)
    username_entry.place(x=30, y=130, height=30, width=200)
    Label(frame3, text="Password  ", fg="red", bg='#33272a', font=("francisco", 18)).place(x=65, y=170)
    password_entry = Entry(frame3, width=30, textvariable=password)
    password_entry.place(x=30, y=210, height=30, width=200)
    Label(frame3, text="Confirm Password  ", fg="red", bg='#33272a', font=("francisco", 18)).place(x=35, y=250)
    password_entry2 = Entry(frame3, width=30, textvariable=confirmpassword)
    password_entry2.place(x=30, y=290, height=30, width=200)
    Label(frame3, text="").pack()
    Button(frame3, text="Register", width=10, height=1, fg="blue", font=("francisco", 19),
           command=register_user).place(x=45, y=370, height=40)


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x550")

    # image
    global bg3
    bg3 = PhotoImage(file="image1.png")
    label3 = Label(screen2, image=bg3)
    label3.place(x=0, y=0)
    frame2 = Frame(screen2, bd=3, width=0, bg='#33272a', padx=20, relief=RIDGE)
    frame2.place(x=50, y=30, width=300, height=450)

    # global bg4
    # bg4 = PhotoImage(file="images.png")
    # label4 = Label(screen2, image=bg4)
    # label4.place(x=0, y=0)

    Label(frame2, text="HELLO AGAIN!", bg='#33272a', fg="red", font=("francisco", 20, "bold")).place(x=40, y=30)
    Label(frame2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(frame2, text="Username  ", bg='#33272a', fg="red", font=("francisco", 18)).place(x=80, y=100)
    username_entry1 = Entry(frame2, width=30, textvariable=username_verify)
    username_entry1.place(x=40, y=135, height=30)
    Label(frame2, text="").pack()
    Label(frame2, text="Password  ", bg='#33272a', fg="red", font=("francisco", 18)).place(x=80, y=185)
    password_entry1 = Entry(frame2, show="*", width=30, textvariable=password_verify)
    password_entry1.place(x=40, y=220, height=30)

    Label(frame2, text="").pack()
    Button(frame2, text="Login", width=10, fg="blue", font=("francisco", 19), command=login_verify).place(x=50, y=310)


def main_screen():
    global screen
    screen = Tk()
    screen.geometry('1200x750+200+0')
    screen.resizable(False, False)
    screen.title('Student Management System')

    # image
    global bg1
    bg1 = PhotoImage(file="image1.png")
    label1 = Label(screen, image=bg1)
    label1.place(x=0, y=0)

    frame1 = Frame(screen, padx=20, bg='#33272a', relief=RIDGE)
    frame1.place(x=400, y=110, width=450, height=550)

    # Title and subtitle
    title = Label(frame1, text='Create Admin', font=("Impact", 35, "bold"), fg='red', bg="#33272a")
    title.place(x=70, y=30)
    subtitle = Label(frame1, text='Welcome to Student Management System', font=("Gudy old style", 14, "bold"), fg='red',
                     bg="#33272a")
    subtitle.place(x=10, y=100)

    # textboxes
    Label(text=" ", bg='white').pack()
    Label(text="", bg='white').pack()
    Label(text="", bg='white').pack()
    Label(text="", bg='white').pack()
    Button(frame1, text="Login", height="3", width="30", font=("CALBRIA", 14, "bold"), bg="#8bd3dd", fg="black",
           command=login).place(x=20, y=200)
    Label(text="", bg='white').pack()
    Button(frame1, text="Register", height="3", width="30", font=("CALBRIA", 14, "bold"), bg="#8bd3dd", fg="black",
           command=register).place(x=20, y=350)

    screen.mainloop()


main_screen()
