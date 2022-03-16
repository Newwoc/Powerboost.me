from bs4 import BeautifulSoup
from urllib.request import urlopen
from array import *


quote_page = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=1&n=48'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')


#Scrape shop pages URLs and save in array
urls = [i['href'] for i in soup.find_all("a", href=True, class_="buybox--button")]
quote_page2 = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=2&n=48'
page2 = urlopen(quote_page2)
soup2 = BeautifulSoup(page2, 'html.parser')
for i in soup2.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])
quote_page3 = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=3&n=48'
page3 = urlopen(quote_page3)
soup3 = BeautifulSoup(page3, 'html.parser')
for i in soup3.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])
quote_page4 = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=4&n=48'
page4 = urlopen(quote_page4)
soup4 = BeautifulSoup(page4, 'html.parser')
for i in soup4.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])
quote_page5 = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=5&n=48'
page5 = urlopen(quote_page5)
soup5 = BeautifulSoup(page5, 'html.parser')
for i in soup5.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])
quote_page6 = 'https://www.stayfocused.de/supplements/trainingsbooster/?p=6&n=48'
page6 = urlopen(quote_page6)
soup6 = BeautifulSoup(page6, 'html.parser')
for i in soup6.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])



productUrl=[]
productTitle=[]
productInhaltsstoffe=[]
#Scrape productpage for Title, URLs 
for i in urls:
    productPage = i
    openProductPage=urlopen(productPage)
    productSoup=BeautifulSoup(openProductPage, 'html.parser')
    productTitle.append(productSoup.find('h1', {'class' : 'product--title'}))
    #productURL.append(i)
    #productInhaltsstoffe.append()

for i in productTitle:    
    print(i.text.strip()) #strip text between elements

for i in urls:    
    print(i)    

    
    
