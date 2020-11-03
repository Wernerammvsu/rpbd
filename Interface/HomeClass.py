import tkinter
from tkinter import *
from PIL import Image, ImageTk
from CastleClass import castle_page

class home_page:
    def __init__(self, get_con, get_window, get_id):
        self.con = get_con
        self.window = get_window
        self.id = get_id
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()

        # --------------------------------------
        # ------------TOP-BUTONS----------------
        # --------------INSERT------------------
        # --------------------------------------

        self.frame_haeder = Frame()

        self.frame_home_btn = Frame(master=self.frame_haeder)
        self.btn_home = Button(master=self.frame_home_btn, text="Главная", bg="gray22", fg='white',
                               command=self.clicked_home)
        self.btn_home.pack()
        self.frame_home_btn.grid(column=0, row=0)

        self.frame_category_btn = Frame(master=self.frame_haeder)
        self.btn_category_castle = Button(master=self.frame_category_btn, text="Замки", bg="gray22", fg='white',
                                          command=self.clicked_castle,
                                          width=15)
        self.btn_category_castle.grid(column=0, row=0)
        self.btn_category_house = Button(master=self.frame_category_btn, text="Дома", bg="gray22", fg='white',
                                         command=self.clicked_house,
                                         width=15)
        self.btn_category_house.grid(column=1, row=0)
        self.btn_category_character = Button(master=self.frame_category_btn, text="Персонажи", bg="gray22", fg='white',
                                             command=self.clicked_character, width=15)
        self.btn_category_character.grid(column=2, row=0)
        self.btn_category_actor = Button(master=self.frame_category_btn, text="Актеры", bg="gray22", fg='white',
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
        self.canvas.grid(row=1, column=0)

    def clear_screen(self):
        for i in self.window.grid_slaves():
            i.grid_forget()

    def clear_grid(self):
        if hasattr(self, 'castle'):
            self.castle.grid_forget()
        if hasattr(self, 'house'):
            self.house.grid_forget()
        if hasattr(self, 'character'):
            self.character.grid_forget()
        if hasattr(self, 'actor'):
            self.actor.grid_forget()

    def clicked_home(self):
        self.clear_grid()
        home = Frame(bg="gray22")

    def clicked_castle(self):
        self.clear_grid()
        if hasattr(self, 'castle'):
            self.castle.grid(row=2, column=0, sticky=NW, padx=20, pady=20)
        else:
            self.castle = Frame(bg="gray22")
            rowK = 0
            self.castle_buttons = []
            for i in self.con.cursor().execute('select name, id from Castle').fetchall():
                self.castle_buttons.append(
                    Button(text=i[0], master=self.castle, font=14, bg="gray22", fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT, command=lambda ID=i[1]: self.castle_info(ID)))
                self.castle_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.castle.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_house(self):
        self.clear_grid()
        if hasattr(self, 'house'):
            self.house.grid(row=2, column=0, sticky=NW, padx=20, pady=20)
        else:
            self.house = Frame(bg="gray22")

            rowK = 0
            self.house_buttons = []
            for i in self.con.cursor().execute('select name from House').fetchall():
                self.house_buttons.append(
                    Button(text=i[0], master=self.house, font=14, bg="gray22", fg='white', activebackground="gray80",
                           width=20, anchor=W, relief=FLAT))
                self.house_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.house.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_actor(self):
        self.clear_grid()
        if hasattr(self, 'actor'):
            self.actor.grid(row=2, column=0, sticky=NW, padx=20, pady=20)
        else:
            self.actor = Frame(bg="gray22")
            rowK = 0
            self.actor_buttons = []
            for i in self.con.cursor().execute('select name, surname from Actor').fetchall():
                self.actor_buttons.append(
                    Button(text=i[0] + " " + i[1], master=self.actor, font=14, bg="gray22", fg='white',
                           activebackground="gray80", width=20, anchor=W, relief=FLAT))
                self.actor_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.actor.grid(row=2, column=0, sticky=NW, padx=20, pady=20)

    def clicked_character(self):
        self.clear_grid()
        if hasattr(self, 'character'):
            self.character.grid(row=2, column=0, sticky=NW, padx=20, pady=20)
        else:
            self.character = Frame(bg="gray22", )
            rowK = 0
            self.character_buttons = []
            for i in self.con.cursor().execute('select name, surname from Character').fetchall():
                self.character_buttons.append(
                    Button(text=i[0] + " " + i[1], master=self.character, font=14, bg="gray22", fg='white',
                           activebackground="gray80", width=20, anchor=W, relief=FLAT))
                self.character_buttons[rowK].grid(row=rowK, column=0)
                rowK += 1
            self.character.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


    def castle_info(self, ID):
        self.clear_screen()
        castle_page(self.con, self.window, self.id, ID)
