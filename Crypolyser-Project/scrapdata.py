from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter
from tkinter.ttk import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import multiprocessing
import time


# Scrapping data from source:

"""
Scraping Data from website::
"""

def getDataSource():
    flag = True
    try:
        # driver = webdriver.PhantomJS(r'phantomjs.exe')
        c_opt = Options()
        c_opt.add_argument('--headless')
        driver = webdriver.Chrome(r'chromedriver.exe', options=c_opt)
        driver.get(r'https://in.investing.com/crypto/')
        return driver
    except:
        print("No internet connection")
        flag = False

driver = getDataSource()

def updateValue(driver):

    crptlist = []
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'lxml')
    tag1 = soup.find_all('td', class_='price js-currency-price')
    for x in tag1:
        crptlist.append(x.text)

    return [crptlist[0], crptlist[1], crptlist[3], crptlist[8]]
          #[bitcoin,     ethereum,     binance,     polkadot]

def update7dValue(driver):
    list7d = []
    value_list = []
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'lxml')
    tag = soup.find_all('td', class_='js-currency-change-7d')
    for x in tag:
        list7d.append(x.text)
    for i in [0,1,3,8]:
        list7d[i] = convertIntoFloat7d(list7d[i])
    return [list7d[0], list7d[1], list7d[3], list7d[8]]

def update1mValue(driver):
    list7d = []
    value_list = []
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'lxml')
    tag = soup.find_all('td', class_='js-currency-change-24h')
    for x in tag:
        list7d.append(x.text)
    for i in [0,1,3,8]:
        list7d[i] = convertIntoFloat7d(list7d[i])
    return [list7d[0], list7d[1], list7d[3], list7d[8]]

def convertIntoFloat(x):
    y = ''
    for i in range(len(x)):
        if x[i]=='.' or  x[i].isdigit():
            y += x[i]
    return float(y)

def convertIntoFloat7d(x):
    y = ''
    for i in range(len(x)):
        if x[i]=='.' or  x[i].isdigit() or x=='-':
            y += x[i]
    return float(y)


""""
PLOTTING FUNCTIONS ::
"""

x = []
bitcoin_y = []
count = 0
def animateBitcoin(i):
    global count
    x.append(count)
    if (len(x) >= 30):
        x.pop(0)
        bitcoin_y.pop(0)
    bitcoin_y.append(convertIntoFloat(updateValue(driver)[0]))
    time.sleep(1)
    plt.cla()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Bitcoin')
    plt.plot(x, bitcoin_y, c='r')
    count += 1

def animateEthereum(i):
    global count
    x.append(count)
    if (len(x) >= 30):
        x.pop(0)
        bitcoin_y.pop(0)
    bitcoin_y.append(convertIntoFloat(updateValue(driver)[1]))
    time.sleep(1)
    plt.cla()
    plt.plot(x, bitcoin_y, color='g')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Ethereum')
    count += 1

def animateBinaca(i):
    global count
    x.append(count)
    if (len(x) >= 30):
        x.pop(0)
        bitcoin_y.pop(0)
    bitcoin_y.append(convertIntoFloat(updateValue(driver)[2]))
    time.sleep(1)
    plt.cla()
    plt.plot(x, bitcoin_y, color='hotpink')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Binaca')
    count += 1

def animatePolkadot(i):
    global count
    x.append(count)
    if (len(x) >= 30):
        x.pop(0)
        bitcoin_y.pop(0)
    bitcoin_y.append(convertIntoFloat(updateValue(driver)[3]))
    time.sleep(1)
    plt.cla()
    plt.plot(x, bitcoin_y, color='#FFFFFF')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Polkadot')
    count += 1

def plotLiveBitcoin():
    print("Plotting live")
    anim = FuncAnimation(plt.gcf(), animateBitcoin, 6000)
    plt.show()
    driver.quit()

def plotLiveEthereum():

    anim = FuncAnimation(plt.gcf(), animateEthereum, 6000)
    plt.show()
    driver.quit()

def plotLivePolkadot():

    anim = FuncAnimation(plt.gcf(), animatePolkadot, 6000)
    plt.show()
    driver.quit()

def plotLiveBinaca():

    anim = FuncAnimation(plt.gcf(), animateBinaca, 6000)
    plt.show()
    driver.quit()

def buildGraphLive():
    print("Building graph")
    print(var.get())
    if var.get() == 'bitcoin':
        print("process",1)
        process1 = multiprocessing.Process(target=plotLiveBitcoin)
        process1.start()
    elif var.get() == 'ethereum':
        print("process",2)
        process2 = multiprocessing.Process(target=plotLiveEthereum)
        process2.start()
    elif var.get() == 'polkadot':
        process3 = multiprocessing.Process(target=plotLivePolkadot)
        process3.start()
    elif var.get() == 'binance':
        process4 = multiprocessing.Process(target=plotLiveBinaca)
        process4.start()

def plot7dGraph():
    xlab = ['Bitcoin', 'Ethereum', 'Binance', 'Dogecoin']
    ylab = update7dValue(driver)

    barlist = plt.bar(xlab, ylab, width=0.3)
    for i in range(4):
        if(ylab[i]<0):
            barlist[i].set_color('r')
        else:
            barlist[i].set_color('g')
    plt.title('Value changed in 7 Days')
    plt.show()
    driver.quit()


def build7dGraph():

    process7d = multiprocessing.Process(target=plot7dGraph)
    process7d.start()

def plot1mGraph():
    xlab = ['Bitcoin', 'Ethereum', 'Binance', 'Dogecoin']
    ylab = update1mValue(driver)

    barlist = plt.bar(xlab, ylab, width=0.3)
    for i in range(4):
        if(ylab[i]<0):
            barlist[i].set_color('r')
        else:
            barlist[i].set_color('g')
    plt.title('Value changed in 1 Month')
    plt.show()
    driver.quit()


def build1mGraph():

    process1m = multiprocessing.Process(target=plot1mGraph)
    process1m.start()

"""
GUI Functions::
"""

def show():
    global choice, bitcoin_value, value_now, buy_value
    if var.get() == 'bitcoin':
        bitcoin_value = updateValue(driver)[0]
        share_value['text'] = bitcoin_value
        choice = 1
        print(choice)
    elif var.get() == 'binance':
        bitcoin_value = updateValue(driver)[2]
        share_value['text'] = bitcoin_value
        choice = 3
        print(choice)
    elif var.get() == 'ethereum':
        bitcoin_value = updateValue(driver)[1]
        share_value['text'] = bitcoin_value
        choice = 2
        print(choice)
    elif var.get() == 'polkadot':
        bitcoin_value = updateValue(driver)[3]
        share_value['text'] = bitcoin_value
        choice = 4
        print(choice)
    elif var.get() == '1' or 1:
        share_value['text'] = 'Please choose option'


def buy():
    global var, buy_value, item
    item = var.get()
    info.config(text='Item Buy: '+str.upper(item), fg='green')
    var.set('1')
    buy_value = bitcoin_value
    buy_value = convertIntoFloat(buy_value)
    buy_butt['state'] = 'disabled'

def sell():
    global buy_value
    buy_value = 0
    info.config(text='Item sold: ' + str.upper(item), fg='red')
    amount.config(text = '')
    amount_pic.config(text='')

    buy_butt['state'] = 'normal'


def checkProfitOrLoss():

    global buy_value
    if choice==1:
        value_now = updateValue(driver)[0]
    elif choice == 2:
        value_now = updateValue(driver)[1]
    elif choice == 3:
        value_now = updateValue(driver)[2]
    elif choice == 4:
        value_now = updateValue(driver)[3]
    else:
        label5['text'] = 'Choose option first'
        return None
    noOfShares = convertIntoFloat(input1.get())
    value_now = convertIntoFloat(value_now)
    if(buy_value==0):
        label5['text'] = 'Buy the Share first'
    else:
        profit = value_now - buy_value
        getPercentage(profit)
        if profit>0:
            amount.config(text='{:.5f}'.format(noOfShares*profit), fg='green')
        else:
            amount.config(text='{:.5f}'.format(noOfShares*profit), fg='red')


def getPercentage(profit):
    percentage = (profit/buy_value) * 100
    if(percentage<0):
        per_amt.config(text='{:.2f}'.format(percentage), fg='red')
        amount_pic.config(image=down, fg='red')
    else:
        per_amt.config(text='{:.2f}'.format(percentage), fg='green')
        amount_pic.config(image=up, fg='red')


"""
GRAPHICAL USER INTERFACE OF APPLICATION: 
"""

# Declaring window for application

if __name__ == '__main__':

    bitcoin_value = 0
    buy_value = 0
    choice = 0
    value_now = 0
    item = ''
    count = 0
    range_value = 0
    x = []
    bitcoin_y = []


    window = tkinter.Tk()
    window.title('CRYPTOLYSER')
    window.iconbitmap('icon_U8f_icon.ico')
    window.geometry('800x700')
    window.resizable(False,False)

    var = tkinter.StringVar(window, "1")
    down = tkinter.PhotoImage(file='down.png')
    up = tkinter.PhotoImage(file='up.png')

    # background Image Color of the Heading
    top_image = tkinter.PhotoImage(file='canva1top.png')
    top_image_label = Label(window, image=top_image, borderwidth=0).place(x=0, y=0)

    # Heading label
    label1 = tkinter.Label(window, text='Your Crypto-currency Analyser', fg='yellow', font=('Calibri Bold', 35),
                           bg='#6fbf4c')
    label1.place(x=80, y=45)

    #Choice Label Heading
    label2 = tkinter.Label(window, text='Choose your currency: ', font=('Sans Serif', 15)).place(x=60, y=180)

    #Choices Radio button
    rad_bitcoin = tkinter.Radiobutton(window, text='BITCOIN', variable=var, value='bitcoin',
                                      font=('Arial Bold', 13),command=show).place(x=60, y=230)
    rad_dogecoin = tkinter.Radiobutton(window, text='BINANCE', variable=var, value='binance',
                                       font=('Arial Bold', 13),command=show).place(x=190, y=230)
    rad_ethereum = tkinter.Radiobutton(window, text='ETHEREUM', variable=var, value='ethereum',
                                       font=('Arial Bold', 13),command=show).place(x=330, y=230)
    rad_polkadot = tkinter.Radiobutton(window, text='POLKADOT', variable=var, value='polkadot',
                                       font=('Arial Bold', 13),command=show).place(x=460, y=230)

    # number of share Label Heading and input
    label3 = tkinter.Label(window, text='Enter number of shares: ', font=('Sans Serif', 15)).place(x=60, y=280)
    input1 = tkinter.Spinbox(window, font=('Arial Bold', 15), from_=1, to_=10)
    input1.place(x=300, y=280)

    # value of per share
    label4 = tkinter.Label(window, text='Share value: ', font=('Sans Serif', 15)).place(x=60, y=330)
    share_value = tkinter.Label(window, text='00.00', font=('Sans Serif', 15))
    share_value.place(x=180, y=330)

    # BUY and SELL buttons
    buy_butt = tkinter.Button(window, text='       BUY       ', font=('Arial Bold', 13), bg='forest green', borderwidth=0,
                              fg='yellow', command=buy)
    buy_butt.place(x=180, y=400)
    sell_butt = tkinter.Button(window, text='       SELL       ', font=('Arial Bold', 13), bg='red3', borderwidth=0,
                               fg='yellow',command=sell)
    sell_butt.place(x=480, y=400)

    info = tkinter.Label(window, text=' ', font=('Sans Serif', 15))
    info.place(x=100, y=650)

    #Profit and loss headings
    profit = tkinter.Label(window, text='Profit/Loss made till now: ', font=('Sans Serif', 15), fg='black').place(x=120, y=450)
    amount = tkinter.Label(window, text=' ', font=('Sans Serif', 15))
    amount.place(x=400, y=450)

    #percdentsge of profit and loss headings
    percentage = tkinter.Label(window, text='Percentage: ', font=('Sans Serif', 15)).place(x=120, y=520)
    amount_pic = tkinter.Label(window, font=('Sans Serif', 17))
    amount_pic.place(x=330, y=520)
    per_amt = tkinter.Label(window, text=' ', font=('Sans Serif', 15))
    per_amt.place(x=400, y=520)

    #refresh button to refresh profit and loss
    refresh = tkinter.PhotoImage(file='refresh.png')
    refresh_butt = tkinter.Button(window, image=refresh, borderwidth=3, command=checkProfitOrLoss).place(x=600, y=480)
    label5 = tkinter.Label(window, text=' ', font=('Sans Serif', 15))
    label5.place(x=550, y=520)

    #Graph buttons
    graph = tkinter.Button(window, text='Show in Live Graph', font=('Arial Bold', 13), borderwidth=3, fg='white',
                           bg='deep sky blue', command=buildGraphLive).place(x=100, y=600)

    graph7d = tkinter.Button(window, text='Plot 7 days Graph', font=('Arial Bold', 13), borderwidth=3, fg='white',
                             bg='deep sky blue', command=build7dGraph).place(x=300, y=600)

    graph1m = tkinter.Button(window, text='Plot 1 month Graph', font=('Arial Bold', 13), borderwidth=3, fg='white',
                             bg='deep sky blue', command=build1mGraph).place(x=500, y=600)

    window.mainloop()
    driver.quit()