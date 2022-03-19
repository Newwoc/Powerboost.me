from posixpath import split
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import pandas as pd 




#define arrays
productUrl=[]
productName=[]
productPrice=[]
productDescription=[]
productContents=[]
productPictureUrl=[]
categoryPageUrls=[]
finishedProductPictureUrl=[]
finishedProductContents=[]
finishedProductDescription=[]
finishedProductPrice=[]    
finishedProductName=[]

#Scrape 'trainingsbooster' Category pages and saves every article URL in array
def getStayfocusedDotDeProductUrls():
    categoryPage = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=1&n=48')
    parsedPage = BeautifulSoup(categoryPage, 'html.parser')
    categoryPageUrls = [i['href'] for i in parsedPage.find_all("a", href=True, class_="buybox--button")]

    categoryPage2 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=2&n=48')
    parsedPage2 = BeautifulSoup(categoryPage2, 'html.parser')
    for i in parsedPage2.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage3 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=3&n=48')
    parsedPage3 = BeautifulSoup(categoryPage3, 'html.parser')
    for i in parsedPage3.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage4 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=4&n=48')
    parsedPage4 = BeautifulSoup(categoryPage4, 'html.parser')
    for i in parsedPage4.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage5 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=5&n=48')
    parsedPage5 = BeautifulSoup(categoryPage5, 'html.parser')
    for i in parsedPage5.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage6 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=6&n=48')
    parsedPage6 = BeautifulSoup(categoryPage6, 'html.parser')
    for i in parsedPage6.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])
    return categoryPageUrls    

#Scrape productpage for Product title, price and description              
def scrapeStayfocusedDotDeProducts():
    for i in getStayfocusedDotDeProductUrls():
        productPage = i
        openProductPage=urlopen(productPage)
        parsedProductPage = BeautifulSoup(openProductPage, 'html.parser')
        productName.append(parsedProductPage.find('h1', {'class' : 'product--title'}))
        productPrice.append(parsedProductPage.find('span', {'class' : 'price--content'}))
        productDescription.append(parsedProductPage.find('div', {'class' : 'product--description'}))
        productContents.append(parsedProductPage.find('div', {'class' : 'price--unit'}))    
        productPictureUrl.append(parsedProductPage.find('span', {'class' : 'image--element'}))
    return productName, productPrice, productDescription, productContents, productPictureUrl  

scrapeStayfocusedDotDeProducts()



dfArray = {"productName" : finishedProductName, "productPrice" : finishedProductPrice, "productDescription" : finishedProductDescription, "name5" : finishedProductPictureUrl, "productContents" : finishedProductContents}
df = pd.DataFrame.from_dict(dfArray, orient='index')
df.to_csv("submission4.csv",index=True,header=True, encoding='utf-8')




