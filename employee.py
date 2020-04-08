"""Employee Management Form"""
import os
import pickle
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import main_login

d = {}


class welcome:
    def __init__(self, window, username):
        self.wn = window
        self.wn.geometry('1300x700+80+20')
        self.wn.configure(background='#d9d9d9')
        self.wn.title('Employee Form')

        self.user = username
        self.lb_heading = Label(self.wn, text='Welcome  ' + self.user, bg='#d9d9d9', fg='BLUe',
                                font=('arial', 20, 'bold'))
        self.lb_heading.pack()


        self.Detail_Frame = Frame(self.wn, bd=4, relief=RIDGE, bg="#d9d9d9")
        self.Detail_Frame.place(x=500, y=60, width=750, height=640)

        """In string"""

        self.ent_id_value = StringVar()
        self.ent_name_value = StringVar()
        self.ent_age_value = StringVar()
        self.ent_add_value = StringVar()
        self.ent_contact_value = StringVar()
        self.ent_department_value = StringVar()

        self.lb_id = Label(self.wn, text='Id:  ', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_id.place(x=10, y=70)

        self.lb_name = Label(self.wn, text='Name:', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_name.place(x=10, y=140)

        self.lb_age = Label(self.wn, text='Age:', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_age.place(x=10, y=210)

        self.lb_add = Label(self.wn, text='Address:', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_add.place(x=10, y=280)

        self.lb_contact = Label(self.wn, text='Contact:', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_contact.place(x=10, y=350)

        self.lb_department = Label(self.wn, text='Department:', font=('arial', 20, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_department.place(x=10, y=420)

        """Entering """
        self.ent_id = Entry(self.wn, textvariable=self.ent_id_value)
        self.ent_id.place(x=190, y=70, width=200, height='29')

        self.ent_name = Entry(self.wn, textvariable=self.ent_name_value)
        self.ent_name.place(x=190, y=140, width=200, height='29')

        self.ent_age = Entry(self.wn, textvariable=self.ent_age_value)
        self.ent_age.place(x=190, y=210, width=200, height='29')

        self.ent_add = Entry(self.wn, textvariable=self.ent_add_value)
        self.ent_add.place(x=190, y=280, width=200, height='29')

        self.ent_contact = Entry(self.wn, textvariable=self.ent_contact_value)
        self.ent_contact.place(x=190, y=350, width=200, height='29')

        self.ent_department = Entry(self.wn, textvariable=self.ent_department_value)
        self.ent_department.place(x=190, y=420, width=200, height='29')

        self.btn_add = Button(self.wn, text='Add', width='6',
                              font=('arial', 18, 'bold'), bg='skyblue', fg='white', command=self.btn_submit_click)
        self.btn_add.place(x=130, y=520)

        """Search"""

        self.table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="skyblue")
        self.table_Frame.place(x=10, y=70, width=720, height=540)

        """Tree view"""
        self.scroll_y = Scrollbar(self.table_Frame, orient=VERTICAL)
        self.employee_tbl = ttk.Treeview(self.table_Frame,
                                         columns=("id", "name", "age", "address", "contact","department"),
                                         xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.employee_tbl.yview, bg='white')
        self.employee_tbl.heading("id", text="ID")
        self.employee_tbl.heading("name", text="Name")
        self.employee_tbl.heading("age", text="Age")
        self.employee_tbl.heading("address", text="Address")
        self.employee_tbl.heading("department", text="Department")
        self.employee_tbl.heading("contact", text="Contact")
        self.employee_tbl['show'] = 'headings'
        self.employee_tbl.column("id", width=40)
        self.employee_tbl.column("name", width=150)
        self.employee_tbl.column("age", width=40)
        self.employee_tbl.column("address", width=100)
        self.employee_tbl.column("department", width=150)
        self.employee_tbl.column("contact", width=150)
        self.employee_tbl.pack(fill=BOTH, expand='1')

        self.btn_show = Button(self.Detail_Frame, text='View Information', bg='skyblue', fg='white'
                               , width='16', height='2', font=('Calibri', 11, 'bold'), command=self.show_all)
        self.btn_show.grid(row=0, column=4, pady=10, padx=10)

        # reset
        def res():
            self.ent_id.delete(0, END)
            self.ent_name.delete(0, END)
            self.ent_add.delete(0, END)
            self.ent_age.delete(0, END)
            self.ent_contact.delete(0, END)
            self.ent_department.delete(0, END)

        self.btn_reset = Button(self.wn, width='6', text='Reset', bg='skyblue', font=('arial', 18, 'bold'), fg='white',
                                command=res)
        self.btn_reset.place(x=10, y=520)

        exit = Button(self.wn, width='6', text='Exit', font=('arial', 18, 'bold'), bg='skyblue', fg='white',
                      command=self.wn.quit)
        exit.place(x=370, y=520)

        logout = Button(self.wn, width='6', text='Logout', font=('arial', 18, 'bold'), bg='skyblue', fg='white',
                        command=self.logout_handler)
        logout.place(x=250, y=520)

    def show_all(self):
        objs = []
        with open('sss.txt', 'rb') as f:
            while 1:
                try:
                    objs.append(pickle.load(f))
                except EOFError:
                    break
        for i in self.employee_tbl.get_children():
            self.employee_tbl.delete(i)

        for i in objs:
            for j in i:
                self.employee_tbl.insert('', END, values=(
                    j, i[j][0], i[j][1], i[j][2], i[j][3],i[j][-1]))

    def btn_submit_click(self):
        self.insert()

    def logout_handler(self):
        newwindow = Toplevel(self.wn)
        self.wn.withdraw()
        main_login.Login(newwindow)

    def insert(self):
        if self.ent_department_value.get() != '' and self.ent_id_value.get() != '' and self.ent_age_value.get() != '' \
                and self.ent_contact_value.get() != '' and self.ent_contact_value.get() != '':
            global d
            la = os.path.getsize('C:\\Users\\Dell\\PycharmProjects\\number 8\\sss.txt')
            id = self.ent_id_value.get()
            name = self.ent_name_value.get()
            contact = self.ent_contact_value.get()
            age = self.ent_age_value.get()
            address = self.ent_add_value.get()
            department = self.ent_department_value.get()

            lf = [name, age, address,contact, department]
            di = {id: lf}

            if la > 0:
                f = open('sss.txt', 'rb+')
                d = pickle.load(f)
                d.update(di)
                f.seek(0)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo('Well done', 'Data saved ')
                f.close()
            else:
                f = open('sss.txt', 'wb')
                d.update(di)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo('Well Done', 'Data saved ')
                f.close()
        else:
            tkinter.messagebox.showerror('Error', 'please fill out the all empty boxes.')


def main():
    wn = Tk()
    welcome(wn, "User")
    wn.mainloop()


if __name__ == '__main__':
    main()
