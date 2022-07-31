from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd
#this one is working

baseurl='https://www.dentalpromotion.fr'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
#url='https://www.dentalpromotion.fr/shop/page/4?search=kavo'
productlinks=[]


for x in range(1,6):
    r=requests.get(f'https://www.dentalpromotion.fr/shop/page/{x}?search=kavo&attrib=0-153',headers=headers, verify=False)
    soup = BeautifulSoup(r.content,'lxml')
    productlist= soup.find_all('div',class_='an_shop_article an_redirection')



    for item in productlist:
        link = item['data-redirection']    
        links = baseurl+link
        productlinks.append(links)
dpiproducts =[]
for link in productlinks:
#testlink='https://www.dentalpromotion.fr/shop/product/25-10075550-expert-matic-contre-angle-e25l-14210?attrib=0-153'
    r = requests.get(link,headers=headers,verify=False)
    soup = BeautifulSoup(r.content,'lxml')            
    title =soup.find('div',class_='singleProductName').text.strip()
    sku= soup.find('div','singleProductMetaValue').text.strip()
    price = soup.find('span','singleProductCurrentPrice').text.strip()
    link1 = link
    print(link1)
    
'''    
    
    products={
            'title' : title,
            'sku' : sku,
            'price' : price,
            'link' : link
            
        }
        

        
    dpiproducts.append(products)  
    print('Saving',products['title'])

df = pd.DataFrame(dpiproducts)
print(df.head(15))    
df.to_csv('conditionsDPIFRANCE31012022.csv')              

'''        

