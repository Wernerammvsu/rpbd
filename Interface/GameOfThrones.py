import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
from StartClass import start_page

def sql_connection():
    try:
        con = sqlite3.connect('GameOfThrones.db')
        return con
    except Error:
        print(Error)


con = sql_connection()

window = Tk()
window["bg"] = "gray22"
window.title("Game Of Thrones Data Base")
window.geometry('1060x1300')

start_page(con,window)





window.mainloop()  # бесконечный цикл вызова окна
con.close()