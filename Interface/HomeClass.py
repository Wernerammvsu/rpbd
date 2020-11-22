#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from CastleClass import castle_page
from HouseClass import house_page
from AddNewPage import new_page
import StartClass


class home_page:
    def __init__(self, get_con, get_window, get_id):
        self.con = get_con
        self.bg = "gray22"
        self.window = get_window
        self.id = get_id
        self.admin = self.con.cursor().execute('select admin from User where id =' + str(self.id)).fetchone()[0]
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()

        self.clear_screen()
        self.draw_header()
        self.draw_image()

    def draw_image(self):
        self.canvas = tkinter.Canvas(self.window, height=175, width=1056)
        self.image = Image.open("../Images/Game.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.place(x=0, y=35, anchor='nw')

    def draw_header(self):
        self.frame_header = self.header()
        self.frame_header.place(x=0, y=0, anchor='nw')

    def header(self):
        frame_header = Frame(master=self.window, height=30, width=1060, bg=self.bg)

        frame_home_btn = Frame(master=frame_header)
        btn_home = Button(master=frame_home_btn, text="Главная", bg=self.bg, fg='white',
                          command=self.clicked_home)
        btn_home.pack()
        frame_home_btn.pack(side=LEFT, expand=1, anchor=W)

        frame_category_btn = Frame(master=frame_header)
        btn_category_castle = Button(master=frame_category_btn, text="Замки", bg=self.bg, fg='white',
                                     command=self.clicked_castle,
                                     width=15)
        btn_category_castle.grid(column=0, row=0)
        btn_category_house = Button(master=frame_category_btn, text="Дома", bg=self.bg, fg='white',
                                    command=self.clicked_house,
                                    width=15)
        btn_category_house.grid(column=1, row=0)
        btn_category_character = Button(master=frame_category_btn, text="Персонажи", bg=self.bg, fg='white',
                                        command=self.clicked_character, width=15)
        btn_category_character.grid(column=2, row=0)
        btn_category_actor = Button(master=frame_category_btn, text="Актеры", bg=self.bg, fg='white',
                                    command=self.clicked_actor,
                                    width=15)
        btn_category_actor.grid(column=3, row=0)

        frame_right_menu = Frame(master=frame_header, bg=self.bg)
        self.entry_search = Entry(master=frame_right_menu, bg="gray32", fg='white', width=15)
        self.entry_search.grid(column=0, row=0, sticky=E)
        btn_search = Button(master=frame_right_menu, text="Поиск", bg=self.bg, fg='white',
                            command=self.search, width=10)
        btn_search.grid(column=1, row=0, sticky=E)
        btn_exit = Button(master=frame_right_menu, text="Выход", bg=self.bg, fg='white',
                          command=self.clicked_exit, width=10)
        btn_exit.grid(column=2, row=0, sticky=E)

        frame_right_menu.pack(side=RIGHT, expand=1, anchor=E)

        if self.admin:
            self.btn_category_users = Button(master=frame_category_btn, text="Пользователи", bg="gray20",
                                             fg='white',
                                             command=self.clicked_users,
                                             width=15)
            self.btn_category_users.grid(column=4, row=0)
            Label(master=frame_header, text='', width=4, bg=self.bg).pack(side=RIGHT)
        else:
            Label(master=frame_header, text='', width=21, bg=self.bg).pack(side=RIGHT)

        frame_category_btn.pack(side=LEFT, expand=1, anchor=W)
        return frame_header

    def clear_screen(self):
        for i in self.window.place_slaves():
            i.place_forget()

        # --------------------------------------
        # ------------NAVIGATION----------------
        # --------------SECTOR------------------
        # --------------------------------------

    def clicked_home(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        home = Frame(bg=self.bg)

    def clicked_castle(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        if hasattr(self, 'castle'):
            self.castle.place(x=20, y=235, anchor='nw')
        else:
            self.castle = Frame(bg=self.bg)
            self.castle_sub = Frame(master=self.castle)
            self.castle_list = self.canvas_scroll(self.width-60, self.height-280, self.castle_sub)
            rowK = 0
            self.castle_buttons = []
            for i in self.con.cursor().execute('select name, id from Castle order by name').fetchall():
                self.castle_buttons.append(
                    Button(text=i[0], master=self.castle_list, font=14, bg=self.bg, fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT, command=lambda ID=i[1]: self.castle_info(ID)))
                self.castle_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            if self.admin:
                Button(master=self.castle, text = 'Добавить', font=20, bg="gray20", fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT, command=lambda type='castle': self.add_new_page(type)).grid(row=0, column=0, sticky=W)
            self.castle_sub.grid(row=1, column=0)
            self.castle.place(x=20, y=235, anchor='nw')

    def clicked_house(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        if hasattr(self, 'house'):
            self.house.place(x=20, y=235, anchor='nw')
        else:
            self.house = Frame(bg=self.bg)
            self.house_sub = Frame(master = self.house)
            self.house_list = self.canvas_scroll(self.width-60, self.height-280, self.house_sub)
            rowK = 0
            self.house_buttons = []
            for i in self.con.cursor().execute('select name, id from House order by name').fetchall():
                self.house_buttons.append(
                    Button(text=i[0], master=self.house_list, font=14, bg=self.bg, fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT,  command=lambda ID=i[1]: self.house_info(ID)))
                self.house_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            if self.admin:
                Button(master=self.house, text = 'Добавить', font=20, bg="gray20", fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT, command=lambda type='house': self.add_new_page(type)).grid(row=0, column=0, sticky=W)
            self.house_sub.grid(row=1, column=0)
            self.house.place(x=20, y=235, anchor='nw')

    def clicked_actor(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        if hasattr(self, 'actor'):
            self.actor.place(x=20, y=235, anchor='nw')
        else:
            self.actor = Frame()
            self.actor_list = self.canvas_scroll(self.width-60, self.height-280, self.actor)
            rowK = 0
            self.actor_buttons = []
            for i in self.con.cursor().execute('select name, surname from Actor order by name, surname').fetchall():
                self.actor_buttons.append(
                    Button(text=i[0] + " " + i[1], master=self.actor_list, font=14, bg=self.bg, fg='white',
                           activebackground="gray80", width=20, anchor=W, relief=FLAT))
                self.actor_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.actor.place(x=20, y=235, anchor='nw')



    def clicked_character(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        if hasattr(self, 'character'):
            self.character.place(x=20, y=235, anchor='nw')
        else:
            self.character = Frame()
            self.character_list = self.canvas_scroll(self.width-60, self.height-280, self.character)
            rowK = 0
            self.character_buttons = []
            for i in self.con.cursor().execute('select name, surname from Character order by name, surname').fetchall():
                self.character_buttons.append(
                    Button(text=i[0] + " " + i[1], master=self.character_list, font=14, bg=self.bg, fg='white',
                           activebackground="gray80", width=20, anchor=W, relief=FLAT))
                self.character_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.character.place(x=20, y=235, anchor='nw')

        # --------------------------------------
        # --------------ADMIN-------------------
        # --------------SECTOR------------------
        # --------------------------------------

    def clicked_users(self):
        self.clear_screen()
        self.draw_header()
        self.draw_image()
        self.users = Frame()
        self.users_list = self.canvas_scroll(self.width-60, self.height-280, self.users)
        rowK = 0
        self.users_ids = []
        self.users_logins = []
        self.buttons_showpass = []
        self.buttons_giveadmin = []
        self.buttons_denyadmin = []
        for i in self.con.cursor().execute('select id, admin, login, password from User').fetchall():
            self.users_ids.append(
                Label(text=('ID: ' + str(i[0]).ljust(3) + str(i[2]).ljust(20)), master=self.users_list, font=14, bg=self.bg,
                      fg='white'))
            self.users_ids[rowK].grid(row=rowK, column=0, sticky=W)
            self.users_logins.append(
                Label(text=('adm' * i[1] + 'usr' * (1 - i[1])), master=self.users_list, font=14, bg=self.bg,
                      fg='white'))
            self.users_logins[rowK].grid(row=rowK, column=1, sticky=E)
            self.buttons_showpass.append(
                Button(text='Просмотреть данные', master=self.users_list,
                       command=lambda ID=i[0]: self.show_pass(ID), bg="gray21", fg="gray70", relief=FLAT))
            self.buttons_showpass[rowK].grid(row=rowK, column=2, padx=5)
            self.buttons_giveadmin.append(
                Button(text='Дать права администратора', master=self.users_list,
                       command=lambda ID=i[0]: self.give_admin(ID), bg="gray21", fg="gray70", relief=FLAT))
            self.buttons_giveadmin[rowK].grid(row=rowK, column=3, padx=5)
            self.buttons_denyadmin.append(
                Button(text='Убрать права администратора', master=self.users_list,
                       command=lambda ID=i[0]: self.deny_admin(ID), bg="gray21", fg="gray70", relief=FLAT))
            self.buttons_denyadmin[rowK].grid(row=rowK, column=4, padx=5)

            rowK += 1
        self.users.place(x=20, y=235, anchor='nw')

    def show_pass(self, k):
        user_data = self.con.cursor().execute('select login, password, id from User where id = ' + str(k)).fetchone()
        if user_data[2]:
            messagebox.showinfo('Пароль', user_data[0].ljust(20) + '\n' + user_data[1].ljust(20))
        else:
            messagebox.showinfo('Получите права администратора', 'Ошибка')

    def give_admin(self, k):
        user_data = self.con.cursor().execute('select login, id from User where id = ' + str(k)).fetchone()
        answer = messagebox.askyesno(title='Дать права администратора',
                                     message='Вы уверены, что хотите дать\n' + user_data[0] + ' права администратора?')
        if answer and user_data[1] and user_data[1] != self.id:
            self.con.cursor().execute('update User set admin = 1 where id = ' + str(k))
            self.con.commit()
            messagebox.showinfo('Дать права администратора', 'Выполненно')
        else:
            messagebox.showinfo('Give adm', 'failed')
        self.clicked_users()

    def deny_admin(self, k):
        user_data = self.con.cursor().execute('select login, id from User where id = ' + str(k)).fetchone()
        answer = messagebox.askyesno(title='Убрать права администратора',
                                     message='Вы уверены, что хотите убрать у\n' + user_data[0] + ' права администратора?')
        if answer and user_data[1] and user_data[1] != self.id:
            self.con.cursor().execute('update User set admin = 0 where id = ' + str(k))
            self.con.commit()
            messagebox.showinfo('Deny adm', 'completed')
        else:
            messagebox.showinfo('Deny adm', 'failed')
        self.clicked_users()

    def add_new_page(self, type):
        self.clear_screen()
        new_page(self.con, self.window, self.id, type)

        # --------------------------------------
        # ------------NEXT-PAGE-----------------
        # -------------SECTOR-------------------
        # --------------------------------------

    def castle_info(self, ID):
        self.clear_screen()
        castle_page(self.con, self.window, self.id, ID)

    def house_info(self, ID):
        self.clear_screen()
        house_page(self.con, self.window, self.id, ID)

    def clicked_exit(self):
        self.clear_screen()
        StartClass.start_page(self.con, self.window)

    def search(self):
        text = self.entry_search.get()
        text = text.lower()
        if text:
            self.clear_screen()
            self.draw_header()
            self.draw_image()
            self.search_frame = Frame()
            self.search_list = self.canvas_scroll(self.width-60, self.height-280, self.search_frame)
            rowK = 0
            nothing = TRUE
            self.search_buttons = []

            description_pool = []

            for i in self.con.cursor().execute("select name, surname, id, description from Character").fetchall():
                if i[3].lower().find(text) != -1:
                    description_pool.append([i[0], i[1], i[3]])
            if description_pool:
                for i in description_pool:
                    self.search_buttons.append(
                    Button(text=i[0] + " " + i[1], master=self.search_list, font=14, bg=self.bg, fg='white',
                           activebackground="gray80", width=20, anchor=W, relief=FLAT))
                self.search_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
                nothing = FALSE

            for i in self.con.cursor().execute("select name, id, description from Castle").fetchall():
                if i[2].lower().find(text) != -1:
                    description_pool.append([i[0], i[1], i[2]])
            if description_pool:
                for i in description_pool:
                    self.search_buttons.append(
                        Button(text=i[0] , master=self.search_list, font=14, bg=self.bg, fg='white',
                               activebackground="gray80", width=20, anchor=W, relief=FLAT, command=lambda ID=i[1]: self.castle_info(ID)))
                    self.search_buttons[rowK].grid(row=rowK, column=0)
                    rowK += 1
                    nothing = FALSE
                if not nothing:
                    self.search_frame.place(x=20, y=235, anchor='nw')


        return

    def canvas_scroll(self, Width, Height, FRAME):

        def current_scroll(event):
            canvas_current.configure(scrollregion=canvas_current.bbox("all"), width=Width, height=Height)

        canvas_current = Canvas(FRAME, bg=self.bg, highlightthickness=0)
        current_list = Frame(canvas_current, bg=self.bg)
        current_scrollbar = Scrollbar(FRAME, orient="vertical", command=canvas_current.yview)
        canvas_current.configure(yscrollcommand=current_scrollbar.set)
        current_scrollbar.pack(side='right', fill='y')
        canvas_current.pack(side='left')
        canvas_current.create_window((0, 0), window=current_list, anchor='nw')
        current_list.bind("<Configure>", current_scroll)
        return current_list

    def time(self):
        return