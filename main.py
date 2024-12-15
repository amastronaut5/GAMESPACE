from tkinter import *
import os
# import pygame
# from turtle import Screen,Turtle
# import random

import turtle

#COLOR = #b7bac5
#
#
#

turtle.TurtleScreen._RUNNING=True
window = Tk()
window.title("GameSpace")
# window.config(padx=100,pady=100)
window.config(bg="black")
window.resizable(0,0)

canvas = Canvas(width=600, height=800, highlightthickness=0)
img = PhotoImage(file="images/galaxy-cosmic-outer.png")
canvas.create_image(300, 400, image=img)
canvas.create_text(300, 100, text="WELCOME TO GAMESPACE !", fill="LIGHT GREEN", font=("space game", 40, "normal"))
canvas.create_text(300, 150, text="Your personal gaming station...", fill="CADETBLUE",
                   font=("space game", 15, "normal"))
canvas.create_text(100, 540, text="SNAKE GAME", fill="CYAN", font=("ANKH SANCTUARY", 15, "normal"))
canvas.create_text(300, 540, text="CROSS THE ROAD", fill="CYAN", font=("ANKH SANCTUARY", 15, "bold"))
canvas.create_text(500, 540, text="PONG GAME", fill="CYAN", font=("ANKH SANCTUARY", 15, "normal"))
canvas.create_text(100, 640, text="QUIZZLER", fill="CYAN", font=("ANKH SANCTUARY", 15, "normal"))
canvas.create_text(300, 350, text="Which game do you want to play ?", fill="cyan", font=("Agency FB", 25, "bold"))
canvas.pack()




def open_snake():
    with open('E:/AKSHAT/to_be_backed_up/PycharmProjects/GameSpace/games/SNAKE GAME/snake_MAIN.PY', "r") as file:
        code = file.read()
        exec(code)


def cross_road():
    with open('games/car_crossing/crossing_main.py', 'r') as file:
        code = file.read()
        exec(code)


def pong_game():
    with open('games/pong_game/pong_MAIN.py', 'r') as file:
        code = file.read()
        exec(code)


def quizzler_game():
    with open('C:/Users/MEHTA/PycharmProjects/QUIZZLER/main.py','r') as file:
        code = file.read()
        exec(code)

game_is_on = True
while game_is_on:

    snake_img = PhotoImage(file="images/snake.png")
    snake_button = Button(text="SNAKE GAME", image=snake_img, fg="cyan", highlightthickness=0, command=open_snake)
    snake_button.place(x=50, y=450)


    turtle_road_img = PhotoImage(file="images/ROAD_TURTLE.png")
    turtle_game_button = Button(image=turtle_road_img, text="CROSS THE ROAD", highlightthickness=0, command=cross_road)
    #,command=os.system("/Users/Mehta/PycharmProjects/turtle-crossing-start/main.py")
    turtle_game_button.place(x=250, y=450)

    pong_img = PhotoImage(file="images/pong.png")
    pong_button = Button(image=pong_img, text="PONG GAME", highlightthickness=0, command=pong_game)
    #,command=os.system("/Users/Mehta/PycharmProjects/PONG GAME/MAIN.py")
    pong_button.place(x=450, y=450)

    quizzler_img = PhotoImage(file="images/quizzler.png")
    quizzler_button = Button(image=quizzler_img, text="QUIZZLER",highlightthickness=0,command=quizzler_game)
    quizzler_button.place(x= 50,y=570)
    window.mainloop()

