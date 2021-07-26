import tkinter
from tkinter.ttk import *

windows = tkinter.Tk()
windows.title('CRYPTOLYSER')
windows.geometry('1000x700')



label1 = tkinter.Label(windows, text = "Your cryptocurrency analyser", font = ('Arial Bold',30))
label1.grid(column = 0, row = 0)

input1 = tkinter.Entry(windows, width=20)

input1.grid(column=1, row=1, ipady=3)

def butt1_click():
    label1.config(text = "Bitcoin Selected Value = "+input1.get(), font = ('Alergian Bold', 20))

button1 = tkinter.Button(windows, text='Bitcoin', fg = 'yellow', bg = 'blue', command=butt1_click, borderwidth=0)
button1.grid(column = 0, row = 1, ipadx=7, ipady=7, pady=6)

style= Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "cyan")

dropdown1 = Combobox(windows)
dropdown1['values'] = ("Bitcoin","Dogecoin","Ethernal")
dropdown1.current(0)
dropdown1.grid(column=0, row=4, ipady=5)
windows.mainloop()