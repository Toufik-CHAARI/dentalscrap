import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd
#do not edit this version works well







fullProduxtList =[]
for x in range(1,16) :
    
    url ='https://www.promodentaire.com/catalogsearch/result/index/?marque=3668&p='
    h ='&q=kavo'
    r = requests.get(url +str(x)+h,headers={'User-Agent': 'Mozilla/5.0'})
    
    
    

    soup = BeautifulSoup(r.content,'html.parser')
    content = soup.find_all('li', class_='product-item')
    for products in content:
        sku = products.find('input',type='hidden').attrs['data-product-id']
        
        
        link = products.find('a').attrs['href']
        prod_name = products.find('h2', class_='product-item-title').text
        img = products.find('img',class_='product-image-photo').attrs['src']
        try:
            oldprice = products.find('span','old-price').text
        except :
            oldprice =('pas de public')
        
        try:
            newprice = products.find('span','new-price').text
        except :
            newprice = products.find('span','price-box-not-discounted').text
        

        product_list ={

        'référence' :    sku, 
        'Désignation' : prod_name,            
        'URL': link,
        'Image' : img,
        'Prix Public' : oldprice,
        'Prit Net' :newprice

            
        }
        
        fullProduxtList.append(product_list)
    time.sleep(2)



print(len(fullProduxtList))

df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionspromodentairetest.csv')    

            
           


    
                
                      
        
            
        
        
            
 
        
            
       
                    
        
        
          

        
   
        

   
   
  




         
           
        
        
        
      
        
            

