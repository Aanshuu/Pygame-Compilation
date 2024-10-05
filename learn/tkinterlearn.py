from tkinter import *
root = Tk()

root.title('GAME')
root.iconbitmap('icon.ico')
root.geometry("500x500")


my_lable = Label(root, text = ' HI ')
my_lable2 = Label(root, text = ' HOW ARE YOU ')

my_lable.grid(row=0, column=1)
my_lable2.grid(row=1,column=2)

root.mainloop()
