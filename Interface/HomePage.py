import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error


def home_page_draw(get_con,get_window):
    con = get_con
    window = get_window

    def clear_grid():
        clear = Frame(master=window, width=500, height=500, bg="gray22")
        clear.grid(row=2, column=0, sticky = W)

    def clicked_home():
        clear_grid()
        home = Frame(bg="gray22")



    def clicked_castle():
        clear_grid()
        castle = Frame(bg="gray22")
        rowK = 0
        for i in con.cursor().execute('select name from Castle').fetchall():
            Label(text=i[0], master=castle, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        castle.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


    def clicked_house():
        clear_grid()
        house = Frame(bg="gray22")

        rowK = 0
        for i in con.cursor().execute('select name from House').fetchall():
            Label(text=i[0], master=house, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        house.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


    def clicked_actor():
        clear_grid()
        actor = Frame(bg="gray22")
        rowK = 0
        for i in con.cursor().execute('select name, surname from Actor').fetchall():
            Label(text=i[0]+' '+i[1], master=actor, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        actor.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


    def clicked_character():
        clear_grid()
        character = Frame(bg="gray22", )
        rowK = 0
        for i in con.cursor().execute('select name, surname from Character').fetchall():
            Label(text=i[0]+' '+i[1], master=character, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
            rowK += 1
        character.grid(row=2, column=0, sticky=NW, padx=20, pady=20)



    frame_haeder = Frame()

    frame_home_btn = Frame(master = frame_haeder)
    btn_home = Button(master=frame_home_btn, text="HOME", bg="gray22", fg='white', command=clicked_home)
    btn_home.pack()
    frame_home_btn.grid(column=0, row=0)

    frame_category_btn = Frame(master = frame_haeder)
    btn_category_castle = Button(master=frame_category_btn, text="CASTLE", bg="gray22", fg='white', command=clicked_castle,
                                 width=15)
    btn_category_castle.grid(column=0, row=0)
    btn_category_house = Button(master=frame_category_btn, text="HOUSE", bg="gray22", fg='white', command=clicked_house,
                                width=15)
    btn_category_house.grid(column=1, row=0)
    btn_category_character = Button(master=frame_category_btn, text="CHARACTER", bg="gray22", fg='white',
                                    command=clicked_character, width=15)
    btn_category_character.grid(column=2, row=0)
    btn_category_actor = Button(master=frame_category_btn, text="ACTOR", bg="gray22", fg='white', command=clicked_actor,
                                width=15)
    btn_category_actor.grid(column=3, row=0)
    frame_category_btn.grid(column=1, row=0)

    frame_haeder.grid(row=0, column=0, sticky=W)

    canvas = tkinter.Canvas(window, height=175, width=1056)
    image = Image.open("../Images/Game.jpg")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.grid(rows=1, column=0)

