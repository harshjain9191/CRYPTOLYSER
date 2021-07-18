# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time
#
# def getDataSource():
#     flag = True
#     try:
#         c_opt = Options()
#         c_opt.add_argument('--headless')
#         # driver = webdriver.PhantomJS(r'phantomjs.exe')
#         driv = webdriver.Chrome(r'chromedriver.exe', options=c_opt)
#         driv.get(r'https://in.investing.com/crypto/')
#         return driv
#
#     except:
#         print("No internet connection")
#         flag = False
#
# def updateValue(driver):
#
#     crptlist = []
#     html_doc = driver.page_source
#     soup = BeautifulSoup(html_doc, 'lxml')
#     tag1 = soup.find_all('td', class_='price js-currency-price')
#     for x in tag1:
#         crptlist.append(x.text)
#
#     return [crptlist[0], crptlist[1], crptlist[7], crptlist[8]]
#
# driv = getDataSource()
# for i in range(5):
#     print(updateValue(driv))
#     time.sleep(3)

f = 0.3455352
print('{:.2f}'.format(f))