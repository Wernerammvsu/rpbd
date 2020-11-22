#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
from tkinter import *
import sqlite3
from sqlite3 import Error
from StartClass import start_page
import pygame


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
window.geometry('1060x600')
window.resizable(width=False,height=False)

window.update_idletasks()
print(window.geometry())
start_page(con, window)

print(con.cursor().execute('select * from User').fetchall())

pygame.mixer.init()
pygame.mixer.music.load("2.mp3")
pygame.mixer.music.play(-1, 0.0)



window.mainloop()  # бесконечный цикл вызова окна
con.close()