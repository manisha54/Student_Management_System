from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox
import time
import sqlite3

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
    root.iconbitmap("student.ico")

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

    # connect to database
    conn = sqlite3.connect('Studentmanagement.db')
    # create a cursor
    c = conn.cursor()

    """
    c.execute('''CREATE TABLE addresses(
           first_name text ,
           last_name text ,
           father_name text,
           mother_name text,
           address1 text,
           gender text,
           address2 text,
           date_of_birth integer,
           email text,
           contact integer,
           Id_number integer,
           Branch text
    )''')
    
    """

    # Create submit button for databases
    def submit():
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()
        # insert in to table
        c.execute(
            "INSERT INTO addresses VALUES (:first_name, :last_name, :father_name, :mother_name, :address1, :gender, :address2, :date_of_birth, :email, :contact,:Id_number, :Branch)",
            {
                'first_name': first_name.get(),
                'last_name': last_name.get(),
                'father_name': father_name.get(),
                'mother_name': mother_name.get(),
                'address1': address1.get(),
                'gender': gender_dropdown.get(),
                'address2': address2.get(),
                'date_of_birth': date_of_birth.get(),
                'email': email.get(),
                'contact': contact.get(),
                'Id_number': Id_number.get(),
                'Branch': Branch.get()
            })
        # showinfo messagebox
        messagebox.showinfo("Adresses", "Stored Successfully")

        conn.commit()
        conn.close()

    def clear():
        # clear the text boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        father_name.delete(0, END)
        mother_name.delete(0, END)
        address1.delete(0, END)
        address2.delete(0, END)
        date_of_birth.delete(0, END)
        email.delete(0, END)
        contact.delete(0, END)
        Id_number.delete(0, END)
        Branch.delete(0, END)

    def query():
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
        # print(records)

        # Loop through the results
        if (len(records) != 0):
            student_table.delete(*student_table.get_children())
            for row in records:
                student_table.insert('', END, values=row)

        conn.commit()
        conn.close()

    def get_cursor(ev):
        clear()
        cursor_row = student_table.focus()
        content = student_table.item(cursor_row)
        row = content['values']

        first_name.insert(0, row[0])
        last_name.insert(0, row[1])
        father_name.insert(0, row[2])
        mother_name.insert(0, row[3])
        address1.insert(0, row[4])
        address2.insert(0, row[6])
        date_of_birth.insert(0, row[7])
        email.insert(0, row[8])
        contact.insert(0, row[9])
        Id_number.insert(0, row[10])
        Branch.insert(0, row[11])

    def delete():
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()

        # delete a record
        c.execute("DELETE from addresses WHERE oid = " + delete_box_entry.get())
        messagebox.showinfo('DELETE DATA',
                            'You have successfully deleted the data of ID number ')

        # query of the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        # print(records)
        # Loop through the results
        print_record = ''
        for record in records:
            # str(record[12]) added for displaying the id
            print_record += str(record[12]) + ' ' + str(record[0]) + ' ' + str(record[1]) + ' ' + str(
                record[2]) + ' ' + str(record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(
                record[6]) + ' ' + str(record[7]) + ' ' + str(record[8]) + ' ' + str(record[9]) + ' ' + str(
                record[10]) + ' ' + str(record[11]) + '\t' + "\n"

        conn.commit()
        conn.close()
        clear()

    def update():
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()
        # update of the database
        record_id = delete_box_entry.get()
        c.execute("SELECT *FROM addresses WHERE oid=" + record_id)
        record = c.fetchall()

        for records in record:
            first_name.insert(0, records[0])
            last_name.insert(0, records[1])
            father_name.insert(0, records[2])
            mother_name.insert(0, records[3])
            address1.insert(0, records[4])
            address2.insert(0, records[6])
            date_of_birth.insert(0, records[7])
            email.insert(0, records[8])
            contact.insert(0, records[9])
            Id_number.insert(0, records[10])
            Branch.insert(0, records[11])

    def editor():
        """this function will update the datas saved in the database."""
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()
        record_id = delete_box_entry.get()
        c.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                father_name = :father,
                mother_name = :mother,
                address1 = :permanent_address,
                address2 = :temporary_address,
                date_of_birth= :dob,
                email = :email_address,
                contact = :contact_number,
                Id_number = :ID_number,
                Branch = :Branch
                
                WHERE oid = :oid""",
                  {'first': first_name.get(),
                   'last': last_name.get(),
                   'father': father_name.get(),
                   'mother': mother_name.get(),
                   'permanent_address': address1.get(),
                   'temporary_address': address2.get(),
                   'dob': date_of_birth.get(),
                   'email_address': email.get(),
                   'contact_number': contact.get(),
                   'ID_number': Id_number.get(),
                   'Branch': Branch.get(),
                   'oid': record_id
                   })
        conn.commit()
        conn.close()

    def search_data():
        conn = sqlite3.connect('Studentmanagement.db')

        c = conn.cursor()
        # search data of the database
        record_id = search.get()
        c.execute("SELECT *, oid FROM addresses where oid=" + record_id)

        records = c.fetchall()
        # print(records)

        # Loop through the results
        if (len(records) != 0):
            student_table.delete(*student_table.get_children())
            for row in records:
                student_table.insert('', END, values=row)

        conn.commit()
        conn.close()




    def logout():
        response = messagebox.askyesno("Logout Application", "Are you sure want to close this application",
                                       icon="warning")
        if response > 0:
            root.destroy()
            return

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
    style.configure('Treeview.Heading', font=('Times', 12, 'italic '), foreground='blue')
    style.configure('Treeview', font=('Times', 10, 'italic '), fg='black', bg='cyan')
    scroll_x = Scrollbar(showentryframe2, orient=HORIZONTAL)
    scroll_y = Scrollbar(showentryframe2, orient=VERTICAL)
    student_table = Treeview(showentryframe2, columns=(
        'First Name', 'Last Name', 'Father Name', 'Mother Name', 'Permanent Address', 'Gender',
        'Temporary Address', 'D.O.B', 'Email Address', 'Contact Number', 'ID Number', 'Branch', 'Delete/Update ID'),
                             yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    # student_table.heading('No', text='No')
    student_table.heading('First Name', text='First Name', anchor=W)
    student_table.heading('Last Name', text='Last Name', anchor=W)
    student_table.heading('Father Name', text='Father Name', anchor=W)
    student_table.heading('Mother Name', text='Mother Name', anchor=W)
    student_table.heading('Permanent Address', text='Permanent Address', anchor=W)
    student_table.heading('Gender', text='Gender', anchor=W)
    student_table.heading('Temporary Address', text='Temporary Address', anchor=W)
    student_table.heading('D.O.B', text='D.O.B', anchor=W)
    student_table.heading('Email Address', text='Email Address', anchor=W)
    student_table.heading('Contact Number', text='Contact Number', anchor=W)
    student_table.heading('ID Number', text='ID Number', anchor=W)
    student_table.heading('Branch', text='Branch', anchor=W)
    student_table.heading('Delete/Update ID', text='Delete/Update ID', anchor=W)
    student_table['show'] = 'headings'

    # student_table.column('No', width=50)
    student_table.column('#0', stretch=NO, minwidth=0, width=0)
    student_table.column('#1', stretch=NO, minwidth=0, width=100)
    student_table.column('#2', stretch=NO, minwidth=0, width=150)
    student_table.column('#3', stretch=NO, minwidth=0, width=150)
    student_table.column('#4', stretch=NO, minwidth=0, width=150)
    student_table.column('#5', stretch=NO, minwidth=0, width=180)
    student_table.column('#6', stretch=NO, minwidth=0, width=150)
    student_table.column('#7', stretch=NO, minwidth=0, width=200)
    student_table.column('#8', stretch=NO, minwidth=0, width=150)
    student_table.column('#9', stretch=NO, minwidth=0, width=150)
    student_table.column('#10', stretch=NO, minwidth=0, width=150)
    student_table.column('#11', stretch=NO, minwidth=0, width=150)
    student_table.column('#12', stretch=NO, minwidth=0, width=150)

    student_table.pack(fill=BOTH, expand=1)
    student_table.bind("<ButtonRelease-1>", get_cursor)

    # label
    first_name_label = Label(Dataentryframe, text='First Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    first_name_label.place(x=15, y=25)
    last_name_label = Label(Dataentryframe, text='Last Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    last_name_label.place(x=465, y=25)
    father_name_label = Label(Dataentryframe, text='Father Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    father_name_label.place(x=15, y=75)
    mother_name_label = Label(Dataentryframe, text='Mother Name :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    mother_name_label.place(x=465, y=75)
    address1_label = Label(Dataentryframe, text='Permanent Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    address1_label.place(x=15, y=125)
    gender_label = Label(Dataentryframe, text='Gender :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    gender_label.place(x=465, y=125)
    address2_label = Label(Dataentryframe, text='Temporary Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    address2_label.place(x=15, y=175)
    date_of_birth_label = Label(Dataentryframe, text='D.O.B :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    date_of_birth_label.place(x=465, y=175)
    email_label = Label(Dataentryframe, text='Email Address :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    email_label.place(x=15, y=225)
    contact_label = Label(Dataentryframe, text='Contact Number :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    contact_label.place(x=465, y=225)
    Id_number_label = Label(Dataentryframe, text='ID Number :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    Id_number_label.place(x=15, y=275)
    branch_label = Label(Dataentryframe, text='Branch :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    branch_label.place(x=465, y=275)
    delete_box = Label(Dataentryframe, text='Delete/Update ID :', bg='#ffd803', font=('Times', 15, 'italic bold'))
    delete_box.place(x=15, y=325)

    # for searching
    search_label = Label(Buttondataframe2, text='Search By', bg='#8bd3dd', font=('Times', 17, 'italic bold'))
    search_label.place(x=100, y=3)
    # option= Entry(Buttondataframe2, font = ('Times', 14 ,'italic ' ), width = 10, borderwidth =3)
    # option.place(x =160 , y = 3)
    search = Entry(Buttondataframe2, font=('Times', 14, 'italic '), width=15, borderwidth=3)
    search.place(x=410, y=3)
    search_btn = Button(Buttondataframe2, font=('calibri', 14, 'bold'), width=10, text="SEARCH", bg='#FF1493',
                        fg='white', command=search_data)
    search_btn.place(x=620, y=2, heigh=30)
    show_btn = Button(Buttondataframe2, font=('calibri', 14, 'bold'), width=10, text="SHOW ALL", bg='#FF1493',
                      fg='white', command=query)
    show_btn.place(x=750, y=2, heigh=30)

    # drop down menu for searching option
    option = ["Name", "Id Number", "Contact Number"]
    option_dropdown = StringVar()
    option_dropdown.set("Id Number")
    drop2 = OptionMenu(Buttondataframe2, option_dropdown, *option)
    drop2.config(font=('Times', 14, 'italic '))
    drop2.place(x=260, y=3, width=140)

    # entry
    first_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    first_name.place(x=250, y=25)
    last_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    last_name.place(x=650, y=25)
    father_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    father_name.place(x=250, y=75)
    mother_name = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    mother_name.place(x=650, y=75)
    address1 = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    address1.place(x=250, y=125)
    # gender = Entry( Dataentryframe, font = ('Times', 14 ,'italic ' ), width = 15, borderwidth = 5)
    # gender.place(x =650 , y = 145)
    address2 = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    address2.place(x=250, y=175)
    date_of_birth = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    date_of_birth.place(x=650, y=175)
    email = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    email.place(x=250, y=225)
    contact = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    contact.place(x=650, y=225)
    Id_number = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    Id_number.place(x=250, y=275)
    Branch = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=15, borderwidth=5)
    Branch.place(x=650, y=275)
    delete_box_entry = Entry(Dataentryframe, font=('Times', 14, 'italic '), width=5, borderwidth=5)
    delete_box_entry.place(x=250, y=325)

    # dropdown
    # drop down menu for gender
    gender = ["Male", "Female", "Other", "Prefer not to say"]
    gender_dropdown = StringVar()
    gender_dropdown.set("select gender")
    drop1 = OptionMenu(Dataentryframe, gender_dropdown, *gender)
    drop1.config(font=('Times', 14, 'italic '))
    drop1.place(x=650, y=125, width=160)

    # Buttonfor student details
    submit_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), relief=RIDGE, width=13, text="SUBMIT",
                        bg='#FF1493', fg='white', command=submit)
    submit_btn.place(x=5, y=15, height=40)

    query_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), width=13, text="CLEAR", bg='#FF1493',
                       fg='white', command=clear)
    query_btn.place(x=5, y=75, height=40)

    edit_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), width=13, text="UPDATE", bg='#FF1493', fg='white',
                      command=update)

    edit_btn.place(x=5, y=135, height=40)

    save_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), width=13, text="SAVE", bg='#FF1493',
                      fg='white', command=editor)
    save_btn.place(x=5, y=195, height=40)

    delete_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), width=13, text="DELETE", bg='#FF1493',
                        fg='white', command=delete)
    delete_btn.place(x=5, y=255, height=40)

    logout_btn = Button(Buttondataframe1, font=('chiller', 20, 'bold'), width=13, text="LOGOUT", bg='#FF1493',
                        fg='white', command=logout)
    logout_btn.place(x=5, y=315, height=40)

    root.mainloop()


main()
