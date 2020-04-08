from tkinter import *
import pickle
import os
import tkinter.messagebox
import main_login

d = {}


class User_Form:
    def __init__(self, window):
        self.wn = window
        self.wn.geometry('500x500+500+200')
        self.wn.configure(background='#d9d9d9')

        # string var

        self.ent_fname_value = StringVar()
        self.ent_lname_value = StringVar()
        self.ent_pass_value = StringVar()
        self.ent_add_value = StringVar()
        self.ent_email_value = StringVar()
        self.ent_age_value = StringVar()
        self.ent_user_value = StringVar()

        self.lb_heading = Label(self.wn, text='Registration', font=('arial', 20, 'bold'), bg='#d9d9d9',
                                fg='black')
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn, bg='#d9d9d9')
        self.frame1.place(x=80, y=40)

        self.lb_fname = Label(self.frame1, text='First name:', font=('arial', 18,), fg='blue', bg='#d9d9d9')
        self.lb_fname.grid(row=0, column=0)

        self.lb_lname = Label(self.frame1, text='Last name:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_lname.grid(row=1, column=0)

        self.lb_gender = Label(self.frame1, text='Gender:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_gender.grid(row=2, column=0)

        """Combobox for gender"""

        gen = ['Male', 'Female', 'Other']
        s = StringVar()
        menu = OptionMenu(self.wn, s, *gen)
        menu.config(width=27, font=('arial', 10, 'italic'))
        menu.place(x=210, y=108)

        self.lb_age = Label(self.frame1, text='Age:', font=('arial', 18,), fg='blue', bg='#d9d9d9')
        self.lb_age.grid(row=3, column=0)

        self.lb_add = Label(self.frame1, text='Address:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_add.grid(row=4, column=0)

        self.lb_user = Label(self.frame1, text='User Name:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_user.grid(row=5, column=0)

        self.lb_email = Label(self.frame1, text='Email:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_email.grid(row=6, column=0)

        self.lb_pass = Label(self.frame1, text='Password:', font=('arial', 18), fg='blue', bg='#d9d9d9')
        self.lb_pass.grid(row=7, column=0)

        """The entry box"""
        self.ent_fname = Entry(self.frame1, textvariable=self.ent_fname_value)
        self.ent_fname.grid(row=0, column=1)
        self.ent_fname.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_lname = Entry(self.frame1, textvariable=self.ent_lname_value)
        self.ent_lname.grid(row=1, column=1)
        self.ent_lname.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_age = Entry(self.frame1, textvariable=self.ent_age_value)
        self.ent_age.grid(row=3, column=1)
        self.ent_age.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_add = Entry(self.frame1, textvariable=self.ent_add_value)
        self.ent_add.grid(row=4, column=1)
        self.ent_add.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_user = Entry(self.frame1, textvariable=self.ent_user_value)
        self.ent_user.grid(row=5, column=1)
        self.ent_user.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_email = Entry(self.frame1, textvariable=self.ent_email_value)
        self.ent_email.grid(row=6, column=1)
        self.ent_email.configure(width='25', font=('arial', 13, 'italic'))

        self.ent_pass = Entry(self.frame1, show='*', textvariable=self.ent_pass_value)
        self.ent_pass.grid(row=7, column=1)
        self.ent_pass.configure(width='25', font=('arial', 13,))

        # submit

        self.btn_submit = Button(self.wn, text='Submit',font=('arial', 25, 'bold'), bg='skyblue', fg='white',
                                 command=self.btn_submit_click)
        self.btn_submit.place(x=250, y=370)

        """Reseting"""
        def res():
            self.ent_fname.delete(0, END)
            self.ent_lname.delete(0, END)
            self.ent_age.delete(0, END)
            self.ent_add.delete(0, END)
            self.ent_email.delete(0, END)
            self.ent_pass.delete(0, END)
            self.ent_user.delete(0, END)

        self.btn_reset = Button(self.wn, text='Reset', bg='skyblue', font=('arial', 25, 'bold'), fg='white',
                                command=res)
        self.btn_reset.place(x=80, y=370)

    def btn_submit_click(self):
        self.insert()
        newwindow = Toplevel(self.wn)
        self.wn.withdraw()
        main_login.Login(newwindow)

    def insert(self):
        if self.ent_fname_value.get() != '' and self.ent_lname_value.get() != '' and self.ent_email_value.get()\
                != '' and \
                self.ent_user_value.get() != '' and self.ent_age_value.get() != '' and self.ent_add_value.get()\
                != '' and self.ent_pass_value.get() != '':
            global d
            le = os.path.getsize('C:\\Users\\Dell\\PycharmProjects\\number 8\\ss.txt')
            fname = self.ent_fname_value.get()
            lname = self.ent_lname_value.get()
            email = self.ent_email_value.get()
            user = self.ent_user_value.get()
            age = self.ent_age_value.get()
            add = self.ent_add_value.get()
            passm = self.ent_pass_value.get()

            ls = [fname, lname, age, add, email, passm]
            di = {user: ls}
            print(di)
            if le > 0:
                f = open('ss.txt', 'rb+')
                d = pickle.load(f)
                d.update(di)
                f.seek(0)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo('yes!', 'Data saved ')
                f.close()
            else:
                f = open('ss.txt', 'wb')
                d.update(di)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo('yes!', 'Data saved ')
                f.close()

        else:
            tkinter.messagebox.showerror('Error', 'please fill out the all empty boxes.')


def main():
    wn = Tk()
    User_Form(wn)
    wn.mainloop()


if __name__ == '__main__':
    main()
