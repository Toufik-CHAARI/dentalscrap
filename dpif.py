import requests
from bs4 import BeautifulSoup
import pandas as pd
# does not work

baseurl='https://www.dentalpromotion.fr'
headers = {'User-Agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
url='https://www.dentalpromotion.fr/shop/page/4?search=kavo'

productlinks=[]

for x in range(1,2):
    r = requests.get(f'https://www.dentalpromotion.fr/shop/page/{x}?search=kavo', verify=False)
    soup = BeautifulSoup(r.content,'lxml')
    productlist = soup.find_all('div','an_shop_article an_redirection')
    
    for item in productlist:
        link=item['data-redirection']
        productlinks.append(baseurl +link)
        print(productlinks)
        
'''
dpiproducts =[]

#testlink='https://www.dentalpromotion.fr/shop/product/25-10075550-expert-matic-contre-angle-e25l-14210?attrib=0-153'
for link in productlinks: 
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')

    title =soup.find('div','an_shop_article_title').text.strip()
    sku= soup.find('div','an_shop_article_short_description').text.strip()  
    price = soup.find('div','an_shop_article_actual_price').text.strip()
    

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
df.to_csv('conditionsDPIFRANCE07032021.csv')

'''
'''
for item in productlist:
    for link in item.find_all('a',href=True):
        print (link['href'])

headers = {'User-Agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
url='https://www.dentalpromotion.fr/shop/page/4?search=kavo'
s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)
productlist = r.html.find('div.an_redirection"')
print(productlist.absolute_links)

for list in productlist:
    print(list.find('div',first=True).attrs['redirection'])




pageurl=productlist.find('div.an_redirection')
for page in pageurl:
    try:
        print(page).attrs['data-redirection']
    except:
        print('niet')    
'''

   









































