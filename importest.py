import requests
from bs4 import BeautifulSoup 

url ='https://www.promodentaire.com/catalogsearch/result/index/?marque=3668&p=1&q=kavo'
    
r = requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    
    

soup = BeautifulSoup(r.content,'html.parser')
content = soup.find_all('li', class_='product-item')


for products in content:
    sku = products.find('input', type='hidden')
    print(sku['data-product-id'])
    #garder (sku['data-product-id'])
    
    