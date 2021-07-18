import tkinter
from tkinter.ttk import *
from PIL import ImageTk,Image
import time

window = tkinter.Tk()
window.title('CRYPTOLYSER')
window.iconbitmap('icon_U8f_icon.ico')
window.geometry('800x700')

top_image = tkinter.PhotoImage(file='canva1top.png')
top_image_label = Label(window, image=top_image, borderwidth=0).place(x=0, y=0)

label1 = tkinter.Label(window, text='Your Crypto-currency Analyser', fg='yellow', font=('Calibri Bold', 35), bg='#6fbf4c')
label1.place(x=80, y=45)

label2 = tkinter.Label(window, text='Choose your currency: ', font=('Sans Serif', 15)).place(x=60, y=180)


var = tkinter.StringVar(window, "1")

def show():
    if var.get() == 1 or '1':
        amount['text'] = 'Please choose option'
    elif var.get() == 'bitcoin':
        pass



rad_bitcoin = tkinter.Radiobutton(window, text='BITCOIN', variable=var, value='bitcoin', font=('Arial Bold',13)).place(x=60, y=230)
rad_dogecoin = tkinter.Radiobutton(window, text='DOGECOIN', variable=var, value='dogecoin', font=('Arial Bold',13)).place(x=190, y=230)
rad_ethereum = tkinter.Radiobutton(window, text='ETHEREUM', variable=var, value='ethereum', font=('Arial Bold',13)).place(x=330, y=230)
rad_polkadot = tkinter.Radiobutton(window, text='POLKADOT', variable=var, value='polkadot', font=('Arial Bold',13)).place(x=460, y=230)

label3 = tkinter.Label(window, text='Enter number of shares: ', font=('Sans Serif', 15)).place(x=60, y=280)
input1 = tkinter.Spinbox(window, font=('Arial Bold', 15), from_=1, to_=10).place(x=300, y=280)

label4 = tkinter.Label(window, text='Share value: ', font=('Sans Serif', 15)).place(x=60, y=330)
share_value = tkinter.Label(window, text='sample', font=('Sans Serif', 15)).place(x=180, y=330)

buy_butt = tkinter.Button(window, text='       BUY       ', font=('Arial Bold', 13), bg='forest green', borderwidth=0, fg='yellow', command=show).place(x=180, y=400)
sell_butt = tkinter.Button(window, text='       SELL       ', font=('Arial Bold', 13), bg='red3', borderwidth=0, fg='yellow').place(x=480, y=400)

info = tkinter.Label(window, text='s', font=('Sans Serif', 15))
info.place(x=100, y=650)

profit = tkinter.Label(window, text='Profit/Loss made till now: ', font=('Sans Serif', 15)).place(x=120, y=450)
amount = tkinter.Label(window, text='sample profit', font=('Sans Serif', 15))
amount.place(x=400, y=450)

percentage = tkinter.Label(window, text='Percentage: ', font=('Sans Serif', 15)).place(x=120, y=520)
per_amt = tkinter.Label(window, text='Sample ', font=('Sans Serif', 15)).place(x=400, y=520)

refresh = tkinter.PhotoImage(file='refresh.png')
refresh_butt = tkinter.Button(window, image=refresh, borderwidth=3).place(x=600, y=480)
label5 = tkinter.Label(window, text='s', font=('Sans Serif', 15)).place(x=580, y=520)

graph = tkinter.Button(window, text='Show in Live Graph',font=('Arial Bold', 13), borderwidth=3 ,fg='white', bg='deep sky blue').place(x=100, y=600)

graph7d = tkinter.Button(window, text='Plot 7 days Graph',font=('Arial Bold', 13), borderwidth=3, fg='white', bg='deep sky blue').place(x=300, y=600)

graph1m = tkinter.Button(window, text='Plot 1 month Graph',font=('Arial Bold', 13), borderwidth=3, fg='white', bg='deep sky blue').place(x=500, y=600)
window.mainloop()

