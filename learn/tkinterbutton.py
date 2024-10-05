from tkinter import *
root = Tk()

root.title('GAME')
root.iconbitmap('icon.ico')
root.geometry("500x500")

def my_click():
    my_lable = Label(root, text = "WELCOME TO THE COURSE", fg= '#3371FF')
    my_lable.pack()


mybutton = Button(root, text = "CLICK THIS", command = my_click, fg = 'black', bg = '#33FFCA', padx= 40, pady= 20)

mybutton.pack()
root.mainloop()


