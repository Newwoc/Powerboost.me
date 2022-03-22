from posixpath import split
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import pandas as pd 




#define arrays
productUrl=[]
productName=[]
productPrice=[]
productUrl=[]
productDescription=[]
productContents=[]
productPictureUrl=[]
categoryPageUrls=[]
strippedProductPictureUrl=[]
strippedProductContents=[]
strippedProductDescription=[]
strippedProductPrice=[]    
strippedProductName=[]
productNutrition=[]
strippedProductNutrition=[]

#Scrape 'trainingsbooster' Category pages and saves every article URL in array
def getStayfocusedDotDeProductUrls():
    categoryPage = urlopen('https://www.muskelmacher-shop.de/supplements/trainingsbooster/?p=1&n=48')
    parsedPage = BeautifulSoup(categoryPage, 'html.parser')
    categoryPageUrls = [i['href'] for i in parsedPage.find_all("a", href=True, class_="buybox--button")]

    categoryPage2 = urlopen('https://www.muskelmacher-shop.de/supplements/trainingsbooster/?p=2&n=48')
    parsedPage2 = BeautifulSoup(categoryPage2, 'html.parser')
    for i in parsedPage2.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage3 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=1&n=48')
    parsedPage3 = BeautifulSoup(categoryPage3, 'html.parser')
    for i in parsedPage3.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage4 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=2&n=48')
    parsedPage4 = BeautifulSoup(categoryPage4, 'html.parser')
    for i in parsedPage4.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])


    categoryPage5 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=3&n=48')
    parsedPage5 = BeautifulSoup(categoryPage5, 'html.parser')
    for i in parsedPage5.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage6 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=4&n=48')
    parsedPage6 = BeautifulSoup(categoryPage6, 'html.parser')
    for i in parsedPage6.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage7 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=5&n=48')
    parsedPage7 = BeautifulSoup(categoryPage7, 'html.parser')
    for i in parsedPage7.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])

    categoryPage8 = urlopen('https://www.stayfocused.de/supplements/trainingsbooster/?p=6&n=48')
    parsedPage8 = BeautifulSoup(categoryPage8, 'html.parser')
    for i in parsedPage8.find_all("a", href=True, class_="buybox--button"):
        categoryPageUrls.append(i['href'])
    return categoryPageUrls    

#Scrape productpage for Product title, price and description              
def scrapeProducts():
    for i in getStayfocusedDotDeProductUrls():
        productPage = i
        openProductPage=urlopen(productPage)
        parsedProductPage = BeautifulSoup(openProductPage, 'html.parser')
        productName.append(parsedProductPage.find('h1', {'class' : 'product--title'}))
        productPrice.append(parsedProductPage.find('span', {'class' : 'price--content'}))
        productDescription.append(parsedProductPage.find('div', {'class' : 'product--description'}))
        productContents.append(parsedProductPage.find('div', {'class' : 'price--unit'}))    
        productPictureUrl.append(parsedProductPage.find('span', {'class' : 'image--element'}))
        productNutrition.append(parsedProductPage.find('div', {'class' : 'dreisc-tab-text-container'}))
    return productName, productPrice, productDescription, productContents, productPictureUrl, productNutrition  

scrapeProducts()


for i in productName:    
    strippedProductName.append(i.text) #strips html text between elements

for i in categoryPageUrls:    
    productUrl.append(i.text) 

for i in productPrice:
    strippedProductPrice.append(i.text) 

for i in productDescription:
    strippedProductDescription.append(i.text) 

for i in productContents:
    strippedProductContents.append(i.text)
    
for i in productNutrition:
    try:
        strippedProductNutrition.append(i.text)
    except:
        print("no text to strip")

for i in productPictureUrl:
    strippedProductPictureUrl.append(((i['data-img-small']),(i['data-img-large']))) #strips image url from html tag




dfArray = {"productName" : strippedProductName, "productPrice" : strippedProductPrice, "productDescription" : strippedProductDescription, "strippedPictureUrl" : strippedProductPictureUrl, "productContents" : strippedProductContents, "productNutrition" : strippedProductNutrition}
df = pd.DataFrame.from_dict(dfArray, orient='index')
df.transpose()
df.to_csv("submission12.csv",index=True,header=True, encoding='utf-8')




