import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('GameOfThrones.db')
        return con
    except Error:
        print(Error)


con = sql_connection()


def clicked_home():
    window.update()
    return


def clicked_castle():
    window.update()
    castle = Frame(bg="gray22")
    rowK = 0
    for i in con.cursor().execute('select name from Castle').fetchall():
        Label(text=i[0], master=castle, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
        rowK += 1
    castle.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


def clicked_house():
    window.update()
    house = Frame(bg="gray22")

    rowK = 0
    for i in con.cursor().execute('select description from House').fetchall():
        Label(text=i[0], master=house, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
        rowK += 1
    house.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


def clicked_actor():
    window.update()
    actor = Frame(bg="gray22")
    rowK = 0
    for i in con.cursor().execute('select name from Actor').fetchall():
        Label(text=i[0], master=actor, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
        rowK += 1
    actor.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


def clicked_character():
    window.update()
    character = Frame(bg="gray22")
    rowK = 0
    for i in con.cursor().execute('select name from Character').fetchall():
        Label(text=i[0], master=character, font=14, bg="gray22", fg='white').grid(row=rowK, column=0, sticky=W)
        rowK += 1
    character.grid(row=2, column=0, sticky=NW, padx=20, pady=20)


window = Tk()
window["bg"] = "gray22"
window.title("Game Of Thrones Data Base")
window.geometry('1060x1300')

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

canvas = tkinter.Canvas(window, height=175, width=1060)
image = Image.open("Game.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(rows=1, column=0)

window.mainloop()  # бесконечный цикл вызова окна
con.close()
