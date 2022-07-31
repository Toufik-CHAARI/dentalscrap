import requests

from bs4 import BeautifulSoup 
import time
import pandas as pd
#does not work anymore keep just for training
headers={'User-Agent': 'Mozilla/5.0'}

fullProduxtList =[]
productlinks=[]
for x in range (1,2):
    r= requests.get(f'https://www.gacd.fr/nos-marques/k/kavo.html?is_ajax=1&p={x}')
    soup = BeautifulSoup(r.content,'html.parser')
    content = soup.find_all('ol', class_="products list items product-items")
    
    for item in content:
        for link in item.findAll('a',class_="product-item-link"):
            url = link['href']
            #print(url)
            productlinks.append(url)
        
    for link in productlinks:  
        r = requests.get(link,headers=headers )    
        soup = BeautifulSoup(r.content,'html.parser')
        try:
            sku = soup.find('span', class_='reference-attribute-value').get_text().strip()
        except AttributeError as err:
            sku="No sku"
        try:
            pname = soup.find('h1', class_='page-title').get_text()  
        except AttributeError as err:
            pname= "No product name"
        try:
            price = soup.find('span', class_='normal-price').get_text().strip()
        except AttributeError as err:
            price="No price"        
        try:
            url= link
        except AttributeError as err:
            url="pas d'url"
        print(sku,pname,price,url)

'''
for products in content:
    try:
        sku = products.find('div', class_='sku').get_text().strip()
    except AttributeError as err:
        sku="No sku"
    
    
    title = products.find('h2', class_='product-name').get_text()
    price = products.find('span', class_='price').get_text().strip()
    link = products.find('a').attrs['href']
    img =  products.find('a',class_="product-image")
    picture = products.img.get('src')
    '''

        
        
'''
        product_list ={
            'SKU' : sku,
            'Product_name' : title,
            'Price': price,
            'URL': link,
            'Picture':picture
        }
        fullProduxtList.append(product_list)
  
    time.sleep(2)    
    
    
df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsgacd23012022.csv')

'''