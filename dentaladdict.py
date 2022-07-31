from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd
#this one is working
productlinks=[]
for x in range (1,5):
    

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    #url='https://www.dentalpromotion.fr/shop/page/4?search=kavo'
    r=requests.get(f'https://www.dental-addict.be/fr/recherche?controller=search&orderby=position&orderway=desc&search_query=kavo&submit_search=&p={x}',headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    productlist= soup.find_all('ul',class_='product_list product_list_default')
    for item in productlist:
        for link in item.find_all ('a', href=True):
            productlinks.append(link['href'])
    
    dentaladdictProduct =[]
for link in productlinks:
    #print(link)
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    try :
        product_name = soup.find("h1",class_="page-heading").get_text().strip()
    except AttributeError as err:
        product_name = 'None'
    url=link 
    
    
    try :
        prices = soup.find("p",{"class":"our_price_display"}).get_text().strip()
    except AttributeError as err:
        prices = "None"

    try:
        sku = soup.find("span",class_="editable").get_text().strip()    
    
    except AttributeError as err:
        sku = "None" 
   
    
    
    
    products={
            'title' : product_name,
            'sku' : sku,
            'price' : prices,
            'link' : link
            
        }
        

        
    dentaladdictProduct.append(products)
    print(dentaladdictProduct)

    

    print('Saving',products['title'])

df = pd.DataFrame(dentaladdictProduct)
print(df.head(15))    
df.to_csv('conditionsdentaladdict022022.csv')              

        

