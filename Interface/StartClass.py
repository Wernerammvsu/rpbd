import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
from HomeClass import home_page


class start_page:

    def __init__(self, get_con, get_window):
        self.con = get_con
        self.window = get_window
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()

        # --------------------------------------
        # ---------------LOGIN------------------
        # --------------------------------------

        self.frame_login = Frame(master=self.window, bg="gray22")

        self.login_text = Label(master=self.frame_login, text="login", bg="gray22")
        self.login_entry = Entry(master=self.frame_login)
        self.login_text.grid(row=0,column=0)
        self.login_entry.grid(row=0,column=1)
        self.password_text = Label(master=self.frame_login, text="password", bg="gray22")
        self.password_entry = Entry(master=self.frame_login)
        self.password_text.grid(row=1,column=0)
        self.password_entry.grid(row=1,column=1)
        self.login_btn = Button(master=self.frame_login, text='Log In', bg="gray22", command=self.login_clicked)
        self.login_btn.grid(row=2, columnspan = 2)

        self.frame_login.grid()

    def clear_screen(self):
        self.frame_login.grid_forget()

    def login_clicked(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        if self.check_log_pas(login, password):
            self.clear_screen()
            home_page(self.con, self.window)

    def check_log_pas(self, login, password):
        return self.con.execute(
            "select exists(select * from User where login = '" + login + "' and password = '" + password + "')").fetchone()[0]
