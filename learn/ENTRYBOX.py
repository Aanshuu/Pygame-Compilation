from tkinter import *
root = Tk()

root.title('GAME')
root.iconbitmap('icon.ico')
root.geometry("800x500")

e = Entry(root, width = 30, fg = 'red')
e.grid(row=0, column=1)

ee = Entry(root, width = 30, fg = 'black')
ee.grid(row=0, column=2)


def clickme():
    my_lable = Label(root, text =  e.get() + " " +ee.get())
    my_lable.grid(row=3, column=1)
    e.delete(0, END)

def clickme2():
    my_lable = Label(root, text = 'Hello ' + ee.get())
    my_lable.grid(row=3, column=2)
    ee.delete(0, END)


mybutton = Button(root, text = "ENTER YOUR FIRST NAME ", fg = 'black', bg = '#33FFCA', padx= 50, pady= 20, command = clickme)
mybutton.grid(row=2, column= 1)


mybutton = Button(root, text = "ENTER YOUR LAST NAME ", fg = 'black', bg = '#33FFCA', padx= 50, pady= 20, command = clickme2)
mybutton.grid(row=2, column=2)

root.mainloop()
