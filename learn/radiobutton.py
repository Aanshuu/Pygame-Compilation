from tkinter import *
root = Tk()

root.title('GAME')
root.iconbitmap('icon.ico')
root.geometry("800x500")

#not needed now





my_text = Label(root, text ="Welcome", font = ("Helvetica", 30), fg = "black")
my_text.pack(pady = 50)

my_button1 = Button(root, text="Exit")
my_button1.pack(pady = 20)