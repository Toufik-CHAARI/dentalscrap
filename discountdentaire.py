from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd
#this one is working


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }



r=requests.get(f'https://www.discount-dentaire.fr/marques/kavo?page=1',headers=headers)
soup = BeautifulSoup(r.content,'lxml')
productlist= soup.find_all('div',id="store_content")
#print(productlist)




for item in productlist:
    #print(item)
    link=item.find_all('div',class_="card-img")
    links=link.find_all('a')
    print(link)
    #link = item['data-redirection']    
    #links = baseurl+link
    #productlinks.append(links)
'''
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