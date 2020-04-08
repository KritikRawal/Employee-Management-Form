import tkinter
from tkinter import *
from tkinter import messagebox
import registration
import os
import pickle
import employee


class Login:

    """This is a class for is employee managenent form.
            Attributers
            Multiple"""


    def __init__(self, window):

        """Constructs all the attributes dor login objects"""

        self.wn = window
        self.wn.title('Login Form')
        self.wn.geometry('400x300+500+200')
        self.wn.configure(background='#d9d9d9')

        """For creating label"""

        self.lb_head = Label(self.wn, text='Please Login to Continue', fg='#1ab2ff', font=('Calibri', 20, 'bold'),
                             bg='#d9d9d9')
        self.lb_head.place(x=0, y=0, relwidth=1)

        """For creating frame"""

        self.frame1 = Frame(self.wn, background='#d9d9d9')
        self.frame1.place(x=50, y=100)

        self.lb_username = Label(self.frame1, text='User Name', font=('Calibri', 15, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_username.grid(row=0, column=0, padx=10, pady=10)

        self.lb_pass = Label(self.frame1, text='Password', font=('Calibri', 15, 'bold'), fg='blue', bg='#d9d9d9')
        self.lb_pass.grid(row=1, column=0, padx=10, pady=10)

        # Creating Entry
        self.ent_username = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_username.grid(row=0, column=1, padx=10, pady=10)

        self.ent_password = Entry(self.frame1, font=('arial', 10, 'bold'), show='*')
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        """Used for buttons"""

        self.btn_login = Button(self.wn, text='Login', bg='#1ab2ff', fg='white', font=('Calibri', 20, 'bold',),
                                command=self.btn_login_click)
        self.btn_login.place(x=80, y=220)

        self.btn_signup = Button(self.wn, text='Sign Up', bg='#1ab2ff', fg='white', font=('Calibri', 20, 'bold'),
                                 command=self.sign_up_handler)
        self.btn_signup.place(x=250, y=220)

    def sign_up_handler(self):

        newwindow = Toplevel(self.wn)
        registration.User_Form(newwindow)
        self.wn.withdraw()

    def btn_login_click(self):
        self.load()

    def load(self):
        le = os.path.getsize('C:\\Users\\Dell\\PycharmProjects\\number 8\\ss.txt')
        if self.ent_password.get() != '' and self.ent_username.get() != '':
            if le > 0:
                f = open('ss.txt', 'rb')
                id = pickle.load(f)
                f.close()
                for i, j in id.items():
                    if i == self.ent_username.get() and j[-1] == self.ent_password.get():
                        tkinter.messagebox.showinfo('Login Complete', 'Press OK to Continue')
                        self.wn.destroy()
                        wel_win = Tk()
                        employee.welcome(wel_win, i)
                        return
                else:

                    tkinter.messagebox.showerror('unsuccessful', 'invalid username or password')
        else:
            tkinter.messagebox.showerror('Empty', 'Please fill all the boxes.')


def main():
    wn = Tk()
    Login(wn)
    wn.mainloop()


if __name__ == '__main__':
    main()
