import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error


class home_page:
    def __init__(self, get_con, get_window):
        self.con = get_con
        self.window = get_window
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()

        # --------------------------------------
        # ------------TOP-BUTONS----------------
        # --------------INSERT------------------
        # --------------------------------------

        self.frame_haeder = Frame()

        self.frame_home_btn = Frame(master=self.frame_haeder)
        self.btn_home = Button(master=self.frame_home_btn, text="HOME", bg="gray22", fg='white',
                               command=self.clicked_home)
        self.btn_home.pack()
        self.frame_home_btn.grid(column=0, row=0)

        self.frame_category_btn = Frame(master=self.frame_haeder)
        self.btn_category_castle = Button(master=self.frame_category_btn, text="CASTLE", bg="gray22", fg='white',
                                          command=self.clicked_castle,
                                          width=15)
        self.btn_category_castle.grid(column=0, row=0)
        self.btn_category_house = Button(master=self.frame_category_btn, text="HOUSE", bg="gray22", fg='white',
                                         command=self.clicked_house,
                                         width=15)
        self.btn_category_house.grid(column=1, row=0)
        self.btn_category_character = Button(master=self.frame_category_btn, text="CHARACTER", bg="gray22", fg='white',
                                             command=self.clicked_character, width=15)
        self.btn_category_character.grid(column=2, row=0)
        self.btn_category_actor = Button(master=self.frame_category_btn, text="ACTOR", bg="gray22", fg='white',
                                         command=self.clicked_actor,
                                         width=15)
        self.btn_category_actor.grid(column=3, row=0)
        self.frame_category_btn.grid(column=1, row=0)

        self.frame_haeder.grid(row=0, column=0, sticky=W)

        # --------------------------------------
        # ---------------IMAGE------------------
        # --------------INSERT------------------
        # --------------------------------------

        self.canvas = tkinter.Canvas(self.window, height=175, width=1056)
        self.image = Image.open("../Images/Game.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(rows=1, column=0)

    def clear_screen(self):
        self.clear = Frame(master=self.window, width=self.width, height=self.height, bg="gray22")
        self.clear.grid(row=0, column=0)

    def clear_grid(self):
        self.clear = Frame(master=self.window, width=500, height=500, bg="gray22")
        self.clear.grid(row=2, column=0, sticky=W)

    def clicked_home(self):
        self.clear_grid()
        home = Frame(bg="gray22")

    def clicked_castle(self):
        self.clear_grid()
        self.castle = Frame(bg="gray22")
        rowK = 0
        for i in self.con.cursor().execute('select name from Castle').fetchall():
            Label(text=i[0], master=self.castle, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        self.castle.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_house(self):
        self.clear_grid()
        self.house = Frame(bg="gray22")

        rowK = 0
        for i in self.con.cursor().execute('select name from House').fetchall():
            Label(text=i[0], master=self.house, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        self.house.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_actor(self):
        self.clear_grid()
        self.actor = Frame(bg="gray22")
        rowK = 0
        for i in self.con.cursor().execute('select name, surname from Actor').fetchall():
            Label(text=i[0] + ' ' + i[1], master=self.actor, font=14, bg="gray22", fg='white').grid(row=rowK, column=0,
                                                                                                    sticky=W)
            rowK += 1
        self.actor.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_character(self):
        self.clear_grid()
        self.character = Frame(bg="gray22", )
        rowK = 0
        for i in self.con.cursor().execute('select name, surname from Character').fetchall():
            Label(text=i[0] + ' ' + i[1], master=self.character, font=14, bg="gray22", fg='white').grid(row=rowK,
                                                                                                        column=0,
                                                                                                        sticky=W)
            rowK += 1
        self.character.grid(row=2, column=0, sticky=NW, padx=20, pady=20)
