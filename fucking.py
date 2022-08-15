import requests
from bs4 import BeautifulSoup 
import time    
import pandas as pd
from requests_html import HTMLSession


fullProduxtList =[]    


    
def MethodeMega():

    url ="https://www.megadental.fr/contre-angle-rouge-expertmatic-e25l-891-8741.html"
    s = HTMLSession()
    r= s.get(url)
    r.html.render(sleep=1)
    pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[3]/div/p/span[2]',first="True").text
    price = r.html.xpath('//*[@id="product-price-1436"]/span',first="True").text
    print(pname,sku,price)

def methodPromo():
    url ="https://www.promodentaire.com/turbine-experttorque-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[2]/span',first="True").text
    price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[4]/span',first="True").text
    sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[1]',first="True").text
    print(sku,pname,price)    



'''
    for contain in containers :
        gamme= "RONDOflex"
        dealer="MEGA DENTAL"
        ref_kavo="1.002.2179"
        pkavoname="RONDOflex Plus 360"
        try :
            pname = contain.find("h1",class_="page-title").get_text().strip()
        except AttributeError as err:
            pname = 'None'
        link = url    
        try :
            price = contain.find("span",{"class":"price"}).get_text().strip()
        except AttributeError as err:
            price = "None"
        try:
            sku = contain.find("div",class_="product attibute code_mega sku").get_text().strip()    
        
        except AttributeError as err:
            sku = "None"
        product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

'''