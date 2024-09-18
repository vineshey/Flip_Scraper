import pandas as pd
import requests
from bs4 import BeautifulSoup
ProductName=[]
Prices=[]
Description=[]
Reviews=[]


for i in  range(2,5):
    url="https://www.flipkart.com/search?q=smrtphones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    r = requests.get(url, headers=headers)
   
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="DOjaWF gdgoEp")
    names=box.find_all("div", class_="KzDlHZ")
    
    for i in names:
        name=i.text
        ProductName.append(name)

    prices=box.find_all("div",class_="Nx9bqj _4b5DiR")
    
    for i in prices: 
        name=i.text
        Prices.append(name)
   
    Desc=box.find_all("ul",class_="G4BRas")
    
    for i in Desc:
        name=i.text
        Description.append(name)
        print("\n")
  


    reviews=box.find_all("div", class_="XQDdHH")
    
    for i in reviews:
        name=i.text
        Reviews.append(name)

df=pd.DataFrame({"Product Name":ProductName,"Prices":Prices,"Description":Description,"Reviews":Reviews})

print(df)

df.to_csv("C:/Users/ACER/OneDrive/Desktop/scraper/flipkart_mobiles_under_50K.csv")
