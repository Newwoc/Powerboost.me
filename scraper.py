from posixpath import split
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#Scrape 'trainingsbooster' Category pages and saves every article URL in array
categoryPage = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=1&n=48')
soup = BeautifulSoup(categoryPage, 'html.parser')
urls = [i['href'] for i in soup.find_all("a", href=True, class_="buybox--button")]

categoryPage2 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=2&n=48')
soup2 = BeautifulSoup(categoryPage2, 'html.parser')
for i in soup2.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])

categoryPage3 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=3&n=48')
soup3 = BeautifulSoup(categoryPage3, 'html.parser')
for i in soup3.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])

categoryPage4 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=4&n=48')
soup4 = BeautifulSoup(categoryPage4, 'html.parser')
for i in soup4.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])

categoryPage5 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=5&n=48')
soup5 = BeautifulSoup(categoryPage5, 'html.parser')
for i in soup5.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])

categoryPage6 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=6&n=48')
soup6 = BeautifulSoup(categoryPage6, 'html.parser')
for i in soup6.find_all("a", href=True, class_="buybox--button"):
    urls.append(i['href'])


#define arrays
productUrl=[]
productTitle=[]
productPrice=[]
productDescription=[]
productContents=[]
productPictureUrl=[]

#Scrape productpage for Product title, price and description 
for i in urls:
    productPage = i
    openProductPage=urlopen(productPage)
    parsedProductPage = BeautifulSoup(openProductPage, 'html.parser')
    productTitle.append(parsedProductPage.find('h1', {'class' : 'product--title'}))
    productPrice.append(parsedProductPage.find('span', {'class' : 'price--content'}))
    productDescription.append(parsedProductPage.find('div', {'class' : 'product--description'}))
    productContents.append(parsedProductPage.find('div', {'class' : 'price--unit'}))
    productPictureUrl.append(parsedProductPage.find('span', {'class' : 'image--element'}))
             


for i in productTitle:    
    print(i.text) #strips html text between elements and prints product title

for i in urls:    
    print(i)    

for i in productPrice:
    print(i.text) 

for i in productDescription:
    print(i.text) 

for i in productContents:
    print(i.text)
    
for i in productPictureUrl:
    print((i['data-img-small'])) #strips image from tag
    print((i['data-img-large']))

    