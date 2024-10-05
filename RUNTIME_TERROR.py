import pygame
from tkinter import *

root = Tk()

root.title('RUNTIME TERROR')
root.iconbitmap('icon.ico')
root.geometry("800x800")

img1 = PhotoImage(file = "background1.png")
my_lable = Label(root, image = img1)
my_lable.place(x=0,y=0, relwidth=1, relheight=1)

def call():
    root.destroy()
    import spacewar
    spacewar.main()

def call2():
    root.destroy()
    import Hangman
    Hangman.main()

def call3():
    root.destroy()
    import snake
    snake.main()

def call4():
    root.destroy()
    import colour_game
    colour_game.my_window()

def call5():
    root.destroy()
    import pong
    pong.main()


my_text = Label(root, text ="Welcome To", font = ("Helvetica", 30), fg = 'white', bg = '#222831')
my_text.pack(pady = 50)

my_text = Label(root, text ="Choose the game you want to play!!!!", font = ("Helvetica", 20), fg = 'white', bg = '#222831')
my_text.pack(pady = 20)

my_frame = Frame(root, bg = '#222831')
my_frame.pack(pady =20)

my_button1 = Button(my_frame, text="SPACEWAR", command = call, font =("Helvetica", 15))
my_button1.pack(pady = 10)

my_button2 = Button(my_frame, text="HANGMAN", font =("Helvetica", 15), command = call2 )
my_button2.pack(pady = 10)

my_button3 = Button(my_frame, text="SNAKE", font =("Helvetica", 15), command = call3)
my_button3.pack(pady = 10)

my_button2 = Button(my_frame, text="COLOUR GAME", font =("Helvetica", 15), command= call4)
my_button2.pack(pady = 10)

my_button3 = Button(my_frame, text="PONG", font =("Helvetica", 15), command = call5)
my_button3.pack(pady = 10)

root.mainloop()