import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
from HomeClass import home_page
from AdminClass import admin_page


class start_page:

    def __init__(self, get_con, get_window):
        self.con = get_con
        self.window = get_window
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()
        self.label = Label(master=self.window, bg="gray22", fg="white", font=("Baskerville Old Face", 16),
                           text='Welcome to "Game of Thrones" database\n'
                                'please enter to DB using your account\n'
                                'or register if you are first time here. :)')
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-50)

        self.frame_chose = Frame(master=self.window, bg="gray22")
        self.chose_login_btn = Button(master=self.frame_chose, text='Log In', bg="gray22", fg="white",
                                command=self.clicked_login_chose, font="Arial 11", width=14)
        self.chose_login_btn.grid(row=0, column=0, columnspan=2, sticky=SE, pady=5)
        self.chose_register_btn = Button(master=self.frame_chose, text='Register', bg="gray22", fg="white",
                                command=self.clicked_register_chose, font="Arial 11", width=14)
        self.chose_register_btn.grid(row=1, column=0, columnspan=2, sticky=SE, pady=5)
        self.frame_chose.place(relx=0.5, rely=0.5, anchor=CENTER)

    # --------------------------------------
    # ---------------LOGIN------------------
    # --------------------------------------
    def clicked_login_chose(self):
        self.clear_screen()
        self.frame_login = Frame(master=self.window, bg="gray22")

        self.login_text = Label(master=self.frame_login, text="login", bg="gray22", fg="white", font="Arial 11")
        self.login_entry = Entry(master=self.frame_login)
        self.login_text.grid(row=0, column=0, sticky=W, pady=5)
        self.login_entry.grid(row=0, column=1, sticky=N, pady=5)
        self.password_text = Label(master=self.frame_login, text="password", bg="gray22", fg="white", font="Arial 11")
        self.password_entry = Entry(master=self.frame_login)
        self.password_text.grid(row=1, column=0, sticky=W)
        self.password_entry.grid(row=1, column=1, sticky=N)
        self.login_btn = Button(master=self.frame_login, text='Log In', bg="gray22", fg="white",
                                command=self.login_clicked, font="Arial 11", width=14)
        self.login_btn.grid(row=2, column=0, columnspan=2, sticky=SE, pady=5)

        self.frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label=Label(master=self.window, bg="gray22", font="Ariel 14", text='ривет добро пожаловать в мой клуб Феечек winks\n'
                                                  'Соблюдайте пожалуста пролшу вас мои правила\n'
                                                  '1 не оскорблять меня\n'
                                                  '2 соблюддать правила\n'
                                                  '3 улабыться\n'
                                                  '4 мои слова закон\n'
                                                  '5 веселитсяяя')
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-110)


    def clicked_register_chose(self):
        self.clear_screen()
        self.frame_register = Frame(master=self.window, bg="gray22")

        self.login_text = Label(master=self.frame_register, text="login", bg="gray22", fg="white", font="Arial 11", width=18, anchor=W)
        self.login_entry = Entry(master=self.frame_register)
        self.login_text.grid(row=0, column=0, sticky=W, pady=2)
        self.login_entry.grid(row=0, column=1, sticky=N, pady=2)
        self.password_text = Label(master=self.frame_register, text="password", bg="gray22", fg="white", font="Arial 11", width=18, anchor=W)
        self.password_entry = Entry(master=self.frame_register)
        self.password_text.grid(row=1, column=0, sticky=W, pady=2)
        self.password_entry.grid(row=1, column=1, sticky=N, pady=2)
        self.confirm_password_text= Label(master=self.frame_register, text="confirm passowrd", bg="gray22", fg="white", font="Arial 11", width=18, anchor=W)
        self.confirm_password_entry = Entry(master=self.frame_register)
        self.confirm_password_text.grid(row=2, column=0, sticky=W, pady=2)
        self.confirm_password_entry.grid(row=2, column=1, sticky=N, pady=2)
        self.register_btn = Button(master=self.frame_register, text='Register', bg="gray22", fg="white",
                                command=self.register_clicked, font="Arial 11", width=14)
        self.register_btn.grid(row=3, column=0, columnspan=2, sticky=SE, pady=2)

        self.frame_register.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label=Label(master=self.window, bg="gray22", font="Ariel 14", text='ривет добро пожаловать в мой клуб Феечек winks\n'
                                                  'Соблюдайте пожалуста пролшу вас мои правила\n'
                                                  '1 не оскорблять меня\n'
                                                  '2 соблюддать правила\n'
                                                  '3 улабыться\n'
                                                  '4 мои слова закон\n'
                                                  '5 веселитсяяя')
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-110)


    def clear_screen(self):
        for i in self.window.place_slaves():
            i.place_forget()

    def login_clicked(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        user = self.check_log_pas(login, password)
        if user[0]:
            self.clear_screen()
            if user[1]:
                admin_page(self.con, self.window)
            else:
                home_page(self.con, self.window)

    def register_clicked(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if self.check_log(login):
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='This login is already taken.\n'
                                    'Try to LogIn or use another login.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        elif password != confirm_password:
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Passwords do not match.\n'
                                    'Check them carefully.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        else:
            constraint = '!@#$%^&*()-_=+[]{};:"<>,./| '+"'"
            for i in password:
                if i in constraint:
                    self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                                       text='Here is some constraint symbol.\n'
                                            'Use only letters and numbers please.')
                    self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
                    return
            if self.add_new_user(login,password):
                self.clear_screen()
                home_page(self.con, self.window)


    def add_new_user(self, login, password):
        self.con.cursor().execute("insert into User (login, password) values('" + login + "','" + password + "')")
        self.con.commit()
        return True

    def check_log_pas(self, login, password):
        r1 = self.con.execute(
            "select exists(select * from User where login = '" + login + "' and password = '" + password + "')").fetchone()[0]
        if r1:
            r2 = self.con.execute(
            "select admin from User where login = '" + login + "' and password = '" + password + "'").fetchone()[0]
        else:
            r2 = 0
        return r1, r2


    def check_log(self, login):
        return self.con.execute(
            "select exists(select * from User where login = '" + login + "')").fetchone()[0]
