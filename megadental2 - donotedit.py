
import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd
#this one works perfectly

'''

url = 'https://www.megadental.fr/brands/kavo-?cat=16029&p=1'
r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content,'html.parser')

print (r.status_code)
'''
fullProduxtList =[]

for x in range (1,27):    
    url = "https://www.megadental.fr/brands/kavo-?p="
    
    r= requests.get(url + str(x),headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    containers = soup.find_all("li",{"class":"item product product-item"})
    for contain in containers :
    #contain = containers[1]
    #container = containers[0]

        product_name = contain.strong.text.strip()
        picture = contain.img.get('src')
        link = contain.a.get('href')
        prices = contain.findAll("span",{"class":"price"})
        price = prices[0].text.strip()        

        refmeg = []
        refmeg = contain.findAll("div",{"class":"value"})
        if len(refmeg)== 0 :
            refmeg = ("is empty")
        else :          
            refmeg= refmeg[0].text.strip()
            
        product_list ={
            'SKU' : refmeg,
            'Product_name' : product_name,
            'Price': price,
            'URL': link,
            'Picture':picture
        }
        fullProduxtList.append(product_list)
        #print(len(fullProduxtList))
    time.sleep(2)    

df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsmega24022022.xls')
       
   



 

   


    