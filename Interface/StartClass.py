from tkinter import *
from HomeClass import home_page


class start_page:

    def __init__(self, get_con, get_window):
        self.con = get_con
        self.window = get_window
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()
        self.welcome_page()

    def welcome_page(self):
        self.label = Label(master=self.window, bg="gray22", fg="white", font=("Baskerville Old Face", 16),
                           text='Добро пожаловать в базу данных по Игре Престолов\n'
                                'Пожалуйста, войдите в свой аккаунт\n'
                                'Или зарегистрируйтесь, если вы входите впервые. :)')
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-50)

        self.frame_chose = Frame(master=self.window, bg="gray22")
        self.chose_login_btn = Button(master=self.frame_chose, text='Вход', bg="gray22", fg="white",
                                      command=self.clicked_login_chose, font="Arial 11", width=14)
        self.chose_login_btn.grid(row=0, column=0, columnspan=2, sticky=SE, pady=5)
        self.chose_register_btn = Button(master=self.frame_chose, text='Регистрация', bg="gray22", fg="white",
                                         command=self.clicked_register_chose, font="Arial 11", width=14)
        self.chose_register_btn.grid(row=1, column=0, columnspan=2, sticky=SE, pady=5)
        self.frame_chose.place(relx=0.5, rely=0.5, anchor=CENTER)

    # --------------------------------------
    # ---------------LOGIN------------------
    # --------------------------------------
    def clicked_login_chose(self):
        self.clear_screen()
        self.frame_login = Frame(master=self.window, bg="gray22")

        self.login_text = Label(master=self.frame_login, text="Логин", bg="gray22", fg="white", font="Arial 11")
        self.login_entry = Entry(master=self.frame_login)
        self.login_text.grid(row=0, column=0, sticky=W, pady=5)
        self.login_entry.grid(row=0, column=1, sticky=N, pady=5)
        self.password_text = Label(master=self.frame_login, text="Пароль", bg="gray22", fg="white", font="Arial 11")
        self.password_entry = Entry(master=self.frame_login)
        self.password_text.grid(row=1, column=0, sticky=W)
        self.password_entry.grid(row=1, column=1, sticky=N)
        self.login_btn = Button(master=self.frame_login, text='Вход', bg="gray22", fg="white",
                                command=self.login_clicked, font="Arial 11", width=14)
        self.login_btn.grid(row=2, column=0, columnspan=2, sticky=SE, pady=5)

        self.back_btn = Button(master=self.frame_login, text='Назад', bg="gray22", fg="white",
                               command=self.back_clicked, font="Arial 11", width=14)
        self.back_btn.grid(row=3, column=0, columnspan=2, sticky=SE, pady=5)

        self.frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label = Label(master=self.window, bg="gray22", font="Ariel 14", text='Добро пожаловать', fg="white")
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-110)

    def clicked_register_chose(self):
        self.clear_screen()
        self.frame_register = Frame(master=self.window, bg="gray22")

        self.login_text = Label(master=self.frame_register, text="Логин", bg="gray22", fg="white", font="Arial 11",
                                width=18, anchor=W)
        self.login_entry = Entry(master=self.frame_register)
        self.login_text.grid(row=0, column=0, sticky=W, pady=2)
        self.login_entry.grid(row=0, column=1, sticky=N, pady=2)
        self.password_text = Label(master=self.frame_register, text="Пароль", bg="gray22", fg="white", font="Arial 11",
                                   width=18, anchor=W)
        self.password_entry = Entry(master=self.frame_register)
        self.password_text.grid(row=1, column=0, sticky=W, pady=2)
        self.password_entry.grid(row=1, column=1, sticky=N, pady=2)
        self.confirm_password_text = Label(master=self.frame_register, text="Повторите пароль", bg="gray22", fg="white",
                                           font="Arial 11", width=18, anchor=W)
        self.confirm_password_entry = Entry(master=self.frame_register)
        self.confirm_password_text.grid(row=2, column=0, sticky=W, pady=2)
        self.confirm_password_entry.grid(row=2, column=1, sticky=N, pady=2)
        self.register_btn = Button(master=self.frame_register, text='Регистрация', bg="gray22", fg="white",
                                   command=self.register_clicked, font="Arial 11", width=14)
        self.register_btn.grid(row=3, column=0, columnspan=2, sticky=SE, pady=2)

        self.back_btn = Button(master=self.frame_register, text='Назад', bg="gray22", fg="white",
                               command=self.back_clicked, font="Arial 11", width=14)
        self.back_btn.grid(row=4, column=0, columnspan=2, sticky=SE, pady=5)

        self.frame_register.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label = Label(master=self.window, bg="gray22", font="Ariel 14", text='Добро пожаловать', fg="white")
        self.label.place(relx=0.5, rely=0.5, anchor=S, y=-110)

    def clear_screen(self):
        for i in self.window.place_slaves():
            i.place_forget()

    def back_clicked(self):
        self.clear_screen()
        self.welcome_page()

    def login_clicked(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        id = self.con.execute(
            "select id from User where login = '" + login + "' and password = '" + password + "'").fetchone()
        if id:
            self.clear_screen()
            home_page(self.con, self.window, id[0])

    def register_clicked(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if self.check_log(login):
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Этот логин уже занят.\n'
                                    'Попробуйте выбрать другой логин.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        elif len(password) < 4:
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Пароль слишком короткий.\n'
                                    'Введите пароль не короче 4 символов.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        elif len(login) < 6:
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Логин слишком короткий.\n'
                                    'Введите логин не короче 6 символов.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        elif len(login) > 15:
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Логин слишком длинный.\n'
                                    'Введите логин не длиннее 15 символов.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        elif password != confirm_password:
            self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36, height=3,
                               text='Пароли не совпадают.\n'
                                    'Проверьте правильность.')
            self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
        else:
            constraint = '!@#$%^&*()-_=+[]{};:"<>,./| ' + "'"
            for i in password:
                if i in constraint:
                    self.label = Label(master=self.window, bg="yellow2", font="Ariel 14", fg="gray5", width=36,
                                       height=3,
                                       text='Введены недопустимые символы.\n'
                                            'Используйте только числа и буквы.')
                    self.label.place(relx=0.5, rely=0.5, anchor=S, y=140)
                    return
            if self.add_new_user(login, password):
                self.clear_screen()
                home_page(self.con, self.window)

    def add_new_user(self, login, password):
        self.con.cursor().execute("insert into User (login, password) values('" + login + "','" + password + "')")
        self.con.commit()
        return True

    def check_log(self, login):
        return self.con.execute(
            "select exists(select * from User where login = '" + login + "')").fetchone()[0]
