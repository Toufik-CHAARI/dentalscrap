import requests
from bs4 import BeautifulSoup 
import time    

    
fulldentaladdict_e25l =[]

    
#url = "https://www.megadental.fr/brands/kavo-?p=1"
url5 = "https://www.dental-addict.be/fr/contre-angles/16113679-contre-angle-expertmatic-e25l-dual-pack.html"

r5= requests.get(url5,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r5.content,'html.parser')
containers = soup.find_all("div",{"class":"primary_block row"})


for contain in containers :
 

    try :
        product_name = contain.find("h1",class_="page-heading").get_text().strip()
    except AttributeError as err:
        product_name = 'None'

    


     
        


    link = url5
    
    try :
        prices = contain.find("p",{"class":"our_price_display"}).get_text().strip()
    except AttributeError as err:
        prices = "None"

        
    



    try:
        sku = contain.find("span",class_="editable").get_text().strip()    
    
    except AttributeError as err:
        sku = "None" 
     
     
       
    product_list ={
        'SKU' : sku,
        'Product_name' : product_name,
        'Price': prices,
        'URL': link,
        
    }
    fulldentaladdict_e25l.append(product_list)
print(fulldentaladdict_e25l)



