from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import time

# intro slider
import random


def main():
    global count, text
    colors = ['red', 'green', 'blue', 'yellow', 'red2', 'gold2']

    def IntroLabelColorTick():
        fg = random.choice(colors)
        sliderlabel.config(fg=fg)
        sliderlabel.after(2, IntroLabelColorTick)

    def IntroLabelTick():
        global count, text
        if count >= len(tt):
            count = 0
            text = ''
            sliderlabel.config(text=text)

        else:
            text = text + tt[count]
            sliderlabel.config(text=text)
            count += 1
        sliderlabel.after(200, IntroLabelTick)

    def tick():
        time_string = time.strftime("%H:%M")
        date_string = time.strftime("%d/%m:/%Y")
        clock.config(text='date :' + date_string + "\n" + "Time : " + time_string)
        clock.after(200, tick)

    root = Tk()
    root.title("Student Management system")
    root.config(bg='pink')
    root.geometry('1060x785+200+0')
    root.resizable(0, 0)

    tt = 'Welcome to student management system'
    count = 0
    text = ''
    # slider label
    sliderlabel = Label(root, text='tt', relief=RIDGE, borderwidth=4, font=('chiller', 30, 'italic bold'), width=35,
                        bg='powderblue')
    sliderlabel.place(x=300, y=0)
    IntroLabelTick()
    IntroLabelColorTick()

    # clock
    clock = Label(root, relief=RIDGE, borderwidth=4, font=('times', 14, 'bold'), bg='#8bd3dd')
    clock.place(x=0, y=0)
    tick()

    # frames
    frame = Frame(root, bg='#8bd3dd', relief=GROOVE, borderwidth=5)
    frame.place(x=10, y=80, width=1040, height=420)
    Buttondataframe1 = Frame(root, bg='#ffd803', relief=GROOVE, borderwidth=5)
    Buttondataframe1.place(x=20, y=100, width=180, height=370)
    Dataentryframe = Frame(root, bg='#ffd803', relief=GROOVE, borderwidth=5)
    Dataentryframe.place(x=210, y=100, width=830, height=370)
    Buttondataframe2 = Frame(root, bg='#8bd3dd', relief=GROOVE, borderwidth=5)
    Buttondataframe2.place(x=10, y=505, width=1040, height=50)
    showentryframe = Frame(root, bg='#8bd3dd', relief=GROOVE, borderwidth=5)
    showentryframe.place(x=10, y=560, width=1040, height=220)
    showentryframe2 = Frame(root, bg='#ffd803', relief=GROOVE, borderwidth=5)
    showentryframe2.place(x=20, y=570, width=1020, height=195)

    # show dataframe
    style = ttk.Style()
    style.configure('Treeview.Heading', font=('Times', 12, 'italic '), foreground='black')
    style.configure('Treeview', font=('Times', 10, 'italic '), fg='black', bg='cyan')
    scroll_x = Scrollbar(showentryframe2, orient=HORIZONTAL)
    scroll_y = Scrollbar(showentryframe2, orient=VERTICAL)
    student_table = Treeview(showentryframe2, columns=(
    'No', 'First Name', 'Last Name', 'Father Name', 'Mother Name', 'Permanent Address', 'Gender',
    'Temporary Address', 'D.O.B', 'Email Address', 'Contact Number', 'ID Number', 'Branch'),
                             yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    student_table.heading('No', text='No')
    student_table.heading('First Name', text='First Name')
    student_table.heading('Last Name', text='Last Name')
    student_table.heading('Father Name', text='Father Name')
    student_table.heading('Mother Name', text='Mother Name')
    student_table.heading('Permanent Address', text='Permanent Address')
    student_table.heading('Gender', text='Gender')
    student_table.heading('Temporary Address', text='Temporary Address')
    student_table.heading('D.O.B', text='D.O.B')
    student_table.heading('Email Address', text='Email Address')
    student_table.heading('Contact Number', text='Contact Number')
    student_table.heading('ID Number', text='ID Number')
    student_table.heading('Branch', text='Branch')
    student_table['show'] = 'headings'

    student_table.column('No', width=50)

    student_table.pack(fill=BOTH, expand=1)

    # label
    first_name_label = Label(Dataentryframe, text='First Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    first_name_label.place(x=15, y=45)
    last_name_label = Label(Dataentryframe, text='Last Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    last_name_label.place(x=465, y=45)
    father_name_label = Label(Dataentryframe, text='Father Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    father_name_label.place(x=15, y=95)
    mother_name_label = Label(Dataentryframe, text='Mother Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    mother_name_label.place(x=465, y=95)
    address1_label = Label(Dataentryframe, text='Permanent Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    address1_label.place(x=15, y=145)
    gender_label = Label(Dataentryframe, text='Gender :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    gender_label.place(x=465, y=145)
    address2_label = Label(Dataentryframe, text='Temporary Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    address2_label.place(x=15, y=195)
    date_of_birth_label = Label(Dataentryframe, text='D.O.B :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    date_of_birth_label.place(x=465, y=195)
    email_label = Label(Dataentryframe, text='Email Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    email_label.place(x=15, y=245)
    contact_label = Label(Dataentryframe, text='Contact Number :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    contact_label.place(x=465, y=245)
    Id_number_label = Label(Dataentryframe, text='ID Number :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    Id_number_label.place(x=15, y=295)
    branch_label = Label(Dataentryframe, text='Branch :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    branch_label.place(x=465, y=295)

    # for searching
    search_label = Label(Buttondataframe2, text='Search By', bg='#8bd3dd', font=('Times', 17, 'italic bold'))
    search_label.place(x=100, y=3)
    # option= Entry(Buttondataframe2, font = ('Times', 14 ,'italic ' ), width = 10, borderwidth =3)
    # option.place(x =160 , y = 3)
    search = Entry(Buttondataframe2, font=('Times', 14, 'italic '), width=15, borderwidth=3)
    search.place(x=410, y=3)
    search_btn = Button(Buttondataframe2, font=('calibri', 14, 'bold'), width=10, text="SEARCH", bg='#FF1493',
                        fg='white')
    search_btn.place(x=620, y=2, heigh=30)
    show_btn = Button(Buttondataframe2, font=('calibri', 14, 'bold'), width=10, text="SHOW ALL", bg='#FF1493',
                      fg='white')
    show_btn.place(x=750, y=2, heigh=30)

    # drop down menu for serching option
    option = ["Name", "Id Number", "Contact Number"]
    option_dropdown = StringVar()
    option_dropdown.set("select option")
    drop2 = OptionMenu(Buttondataframe2, option_dropdown, *option)
    drop2.config(font=('calibri', 14, 'bold'))
    drop2.place(x=260, y=3, width=140)

    # entry
    first_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    first_name.place(x=250, y=45)
    last_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    last_name.place(x=650, y=45)
    father_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    father_name.place(x=250, y=95)
    mother_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    mother_name.place(x=650, y=95)
    address1 = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    address1.place(x=250, y=145)
    # gender = Entry( Dataentryframe, font = ('Times', 14 ,'italic ' ), width = 15, borderwidth = 5)
    # gender.place(x =650 , y = 145)
    address2 = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    address2.place(x=250, y=195)
    date_of_birth = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    date_of_birth.place(x=650, y=195)
    email = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    email.place(x=250, y=245)
    contact = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    contact.place(x=650, y=245)
    Id_number = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    Id_number.place(x=250, y=295)
    Branch = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    Branch.place(x=650, y=295)

    # dropdown
    # drop down menu for gender
    gender = ["Male", "Female", "Other", "Prefer not to say"]
    gender_dropdown = StringVar()
    gender_dropdown.set("select gender")
    drop1 = OptionMenu(Dataentryframe, gender_dropdown, *gender)
    drop1.place(x=650, y=145, width=160)

    # Buttonfor student details
    submit_btn = Button(Buttondataframe1, font=('calibri', 16, 'bold'), width=10, text="SAVE", bg='#FF1493', fg='white')
    submit_btn.place(x=20, y=30)
    query_btn = Button(Buttondataframe1, font=('calibri', 16, 'bold',), width=10, text="DISPLAY", bg='#FF1493',
                       fg='white')
    query_btn.place(x=20, y=90)
    edit_btn = Button(Buttondataframe1, font=('calibri', 16, 'bold'), width=10, text="UPDATE", bg='#FF1493', fg='white')
    edit_btn.place(x=20, y=150)
    delete_box = Button(Buttondataframe1, font=('calibri', 16, 'bold'), width=10, text="DELETE", bg='#FF1493',
                        fg='white')
    delete_box.place(x=20, y=210)
    logout_button = Button(Buttondataframe1, font=('calibri', 16, 'bold'), width=10, text="LOGOUT", bg='#FF1493',
                           fg='white')
    logout_button.place(x=20, y=270)

    root.mainloop()


