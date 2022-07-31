import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd


fullProduxtList =[]
for x in range(1,3) :


    url = "https://www.doctorstrong.fr/catalogsearch/result/index/?marque=KAVO&p="
    h='&q=kavo'

    r= requests.get(url+str(x)+h ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    containers = soup.find_all("li",{"class":"product-item"})
    for container in containers:
        title =container.find("strong",{"class":"product-item-name"}).text.strip()
        try:
            sku = container.find("div",{"class":"value"}).text.strip()
        except:
            sku = ('pas de sku')
        
        try:
            link = container.find('a',{"class":"product-item-link"}).attrs['href']
        except:
            link = ('no link')

        newprice = container.find("span",{"class":"besttiersprice-price"})
        try:
            newprice1= newprice.find("span",{"class":"price"}).text.strip()
        except:
            newprice1 =('pas de prix')


        product_list ={

            'référence' :    sku, 
            'Désignation' : title,            
            'URL': link,
            'Prit Net' :newprice1

                
            }
        fullProduxtList.append(product_list)      
    time.sleep(2)  

print(len(fullProduxtList))
df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsdoctorstrong.csv')