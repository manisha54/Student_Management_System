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
    screen1.iconbitmap("student.ico")
    screen1.geometry("730x500")
    screen1.resizable(False, False)

    global bg2
    bg2 = PhotoImage(file="image1.png")
    label2 = Label(screen1, image=bg2)
    label2.place(x=-5, y=0)

    global username
    global password
    global username_entry
    global password_entry
    global password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    Label(screen1, text="REGISTER HERE!!", fg="#800080", bg='white', font=("francisco", 23)).place(x=350, y=150)
    Label(screen1, text="").pack()
    Label(screen1, text="Username  ", fg="#800080", bg='white', font=("francisco", 18)).place(x=270, y=220)
    username_entry = Entry(screen1, width=25, borderwidth='5', textvariable=username)
    username_entry.place(x=480, y=220, height=30, width=200)
    Label(screen1, text="Password  ", fg="#800080", bg='white', font=("francisco", 18)).place(x=270, y=260)
    password_entry = Entry(screen1, width=25, borderwidth='5', textvariable=password)
    password_entry.place(x=480, y=260, height=30, width=200)
    Label(screen1, text="Confirm Password  ", fg="#800080", bg='white', font=("francisco", 18)).place(x=270, y=310)
    password_entry2 = Entry(screen1, width=25, borderwidth='5', textvariable=confirmpassword)
    password_entry2.place(x=480, y=310, height=30, width=200)
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, fg="#800080", font=("francisco", 19),
           command=register_user).place(x=350, y=370, height=40)


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.iconbitmap("student.ico")
    screen2.geometry("730x500")
    screen2.resizable(False, False)

    # image
    global bg3
    bg3 = PhotoImage(file="image5.png")
    label3 = Label(screen2, image=bg3)
    label3.place(x=-5, y=0)

    Label(screen2, text="HELLO AGAIN!", bg='white', fg="#0000FF", font=("francisco", 20, "bold")).place(x=470, y=150)
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username  ", bg='white', fg="#0000FF", font=("francisco", 18)).place(x=390, y=230)
    username_entry1 = Entry(screen2, width=25, borderwidth='5', textvariable=username_verify)
    username_entry1.place(x=530, y=230, height=30)
    Label(screen2, text="").pack()
    Label(screen2, text="Password  ", bg='white', fg="#0000FF", font=("francisco", 18)).place(x=390, y=280)
    password_entry1 = Entry(screen2, show="*", width=25, borderwidth='5', textvariable=password_verify)
    password_entry1.place(x=530, y=280, height=30)

    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, fg="#0000FF", font=("francisco", 19), command=login_verify).place(x=480,
                                                                                                              y=350,
                                                                                                              height=40)


def main_screen():
    global screen
    screen = Tk()
    screen.geometry('1200x750+200+0')
    screen.resizable(False, False)
    screen.title('Student Management System')
    screen.iconbitmap("image2.ico")

    frame = Frame(screen, padx=20, bg='#8bd3dd', borderwidth=0, relief=RIDGE)
    frame.place(x=620, y=0, width=620, height=800)

    frame1 = Frame(screen, padx=20, bg='#f9bc60', relief=RIDGE)
    frame1.place(x=700, y=110, width=450, height=550)

    frame2 = Frame(screen, padx=20, bg='#33272a', borderwidth=0, relief=RIDGE)
    frame2.place(x=0, y=0, width=620, height=800)

    global bg4
    bg4 = PhotoImage(file="image3.png")
    label1 = Label(frame2, image=bg4)
    label1.place(x=-50, y=0, height=850)

    # Title and subtitle
    title = Label(frame1, text='Create Admin', font=("Impact", 35, "bold"), fg='#800080', bg="#f9bc60")
    title.place(x=70, y=30)
    subtitle = Label(frame1, text='LOGIN AND REGISTER HERE', font=("Gudy old style", 14, "bold"), fg='#800080',
                     bg="#f9bc60")
    subtitle.place(x=70, y=100)

    subtitle1 = Label(frame2, text='WELCOME TO STUDENT MANAGEMENT SYSTEM', font=('chiller', 27, 'italic bold'),
                      fg='#800080',
                      bg="#f9bc60", width=60, height=3)
    subtitle1.place(x=-130, y=0)

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
