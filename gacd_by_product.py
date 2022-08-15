
import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd

fullProduxtList =[]


def gacd_Rondo():    
    url="https://www.gacd.fr/article-0117122-rondoflex-plus.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="RONDOflex"
        dealer="GACD"
        ref_kavo="1.002.2179"
        pkavoname="RONDOflex Plus 360"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_Sonic2008L():    
    url="https://www.gacd.fr/article-0286185-detartreur-sonicflex-2008-l.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="SONICflex"
        dealer="GACD"
        ref_kavo="1.007.1604"
        pkavoname="SONICflex set 2008L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)        
        
def gacd_Sonic2003L():    
    url="https://www.gacd.fr/article-0115336-detartreur-sonicflex-2003.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="SONICflex"
        dealer="GACD"
        ref_kavo="1.000.8333"
        pkavoname="SONICflex set 2003L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_PF4():    
    url="https://www.gacd.fr/prophyflex-4-aeropolisseur-chapeau.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="PROPHYflex"
        dealer="GACD"
        ref_kavo="3.002.8000"
        pkavoname="PROPHYflex 4"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)            
                   
def gacd_E25L():    
    url="https://www.gacd.fr/article-3006303-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5550"
        pkavoname="EXPERTmatic E25L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def gacd_E25C():    
    url="https://www.gacd.fr/article-3006302-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5551"
        pkavoname="EXPERTmatic E25C"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_DuoPackE25L():    
    url="https://www.gacd.fr/duo-pack-expermatic-e25l-e25l-le-contre-angle-lumiere-bague-rouge-1-5.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.014.5499"
        pkavoname="Duo-Pack E25L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)
            
def gacd_E20L():    
    url="https://www.gacd.fr/article-3006301-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5540"
        pkavoname="EXPERTmatic E20L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)              

def gacd_E20C():    
    url="https://www.gacd.fr/article-3006300-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5541"
        pkavoname="EXPERTmatic E20C"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_DuopackE20L_E25L():    
    url="https://www.gacd.fr/duo-pack-mix-e25l-e20l-le-contre-angle-rouge-et-bleu.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.014.5475"
        pkavoname="Duo-Pack E25L / E20L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)
            
def gacd_DuopackE20L_E20L():    
    url="https://www.gacd.fr/duo-pack-e20l-20l.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.014.5505"
        pkavoname="Duo-Pack E20L / E20L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)            
             
def gacd_E15L():    
    url="https://www.gacd.fr/article-3006299-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5530"
        pkavoname="EXPERTmatic E15L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_E15C():    
    url="https://www.gacd.fr/article-3006298-contre-angle-expertmatic.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTmatic"
        dealer="GACD"
        ref_kavo="1.007.5531"
        pkavoname="EXPERTmatic E15C"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_E680L():    
    url="https://www.gacd.fr/article-3006306-turbine-experttorque.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTtorque"
        dealer="GACD"
        ref_kavo="1.006.8700"
        pkavoname="EXPERTtorque E680L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_E677L():    
    url="https://www.gacd.fr/article-3006307-turbine-experttorque.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTtorque"
        dealer="GACD"
        ref_kavo="1.007.3600"
        pkavoname="EXPERTtorque E677L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_DuoE680L():    
    url="https://www.gacd.fr/duo-pack-e680l-e680l-la-turbine-experttorque-e680l.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTtorque"
        dealer="GACD"
        ref_kavo="1.007.5478"
        pkavoname="EXPERTtorque Duo-Pack E680L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M25L():    
    url="https://www.gacd.fr/article-3024887-contre-angle-mastermatic-m25l-15.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3630"
        pkavoname="MASTERmatic M25L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M20L():    
    url="https://www.gacd.fr/article-3024890-manche-mastermatic-m20l-11.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3620"
        pkavoname="MASTERmatic M20L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M05L():    
    url="https://www.gacd.fr/contre-angle-mastermatic-mini-m05l-1-5.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3640"
        pkavoname="MASTERmatic M05L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M07L():    
    url="https://www.gacd.fr/article-3024889-manche-mastermatic-lux-m07l-2-71.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3610"
        pkavoname="MASTERmatic M07L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M29L():    
    url="https://www.gacd.fr/article-3024891-manche-mastermatic-lux-m29l-7-41.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3580"
        pkavoname="MASTERmatic M29L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M10L():    
    url="https://www.gacd.fr/piece-a-main-mastermatic-lux-m10l-1-1.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERmatic"
        dealer="GACD"
        ref_kavo="1.009.3570"
        pkavoname="MASTERmatic M10L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)


def gacd_M9000L():    
    url="https://www.gacd.fr/article-3015499-turbine-mastertorque-9000.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERtorque"
        dealer="GACD"
        ref_kavo="1.008.7900"
        pkavoname="MASTERtorque M9000L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_M8700L():    
    url="https://www.gacd.fr/article-3024278-turbine-mastertorque-mini-m8700l.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="MASTERtorque"
        dealer="GACD"
        ref_kavo="3.001.0000"
        pkavoname="MASTERtorque M8700L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_S11L():    
    url="https://www.gacd.fr/p-a-m-surgmatic-s11l-1-1.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="SURGmatic"
        dealer="GACD"
        ref_kavo="1.009.1010"
        pkavoname="SURGmatic S11L"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_S15L():    
    url="https://www.gacd.fr/catalog/product/view/id/64031/s/contre-angle-surgmatic-s15l-pro/"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="SURGmatic"
        dealer="GACD"
        ref_kavo="1.014.4000"
        pkavoname="SURGmatic S15L Pro"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_S201XL():    
    url="https://www.gacd.fr/contre-angle-surgmatic-s201-xl-pro-le-contre-angle.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="SURGmatic"
        dealer="GACD"
        ref_kavo="1.013.7541"
        pkavoname="SURGmatic S201 XL Pro"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def gacd_EXPERTsurg():    
    url="https://www.gacd.fr/article-3020206-expertsurg-lux-moteur-de-chirurgie.html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    section = soup.find_all("div",{"class":"column main"})
    for products in section:
        try:
            pname = products.find("h1",{"class":"page-title"}).get_text().strip()
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        gamme="EXPERTsurg"
        dealer="GACD"
        ref_kavo="1.008.3500"
        pkavoname="EXPERTsurg"
        try:
            
            sku=products.find("div",{"class":"reference-attribute-container"}).get_text().strip()
        except AttributeError as err:
            sku = 'None'

        #print(sku)
        try:
            price =  products.find("span",{"class": "price"}).text.strip()
        except AttributeError as err:
            price ='None' 
        link = url
        product_list ={

        'gamme': gamme,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'dealer': dealer,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': link,
        'Prit Net' :price
           
        }
        fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)




gacd_Rondo()
gacd_Sonic2008L()
gacd_Sonic2003L()
gacd_PF4()
gacd_E25L()
gacd_E25C()
gacd_DuoPackE25L()
gacd_E20L()
gacd_E20C()
gacd_DuopackE20L_E25L()
gacd_DuopackE20L_E20L()
gacd_E15L()
gacd_E15C()
gacd_E680L()
gacd_E677L()
gacd_DuoE680L()
gacd_M25L()
gacd_M20L()
gacd_M05L()
gacd_M07L()
gacd_M29L()
gacd_M10L()
gacd_M9000L()
gacd_M8700L()
gacd_S11L()
gacd_S15L()
gacd_S201XL()
gacd_EXPERTsurg()


print(len(fullProduxtList))

df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv("extraction/AOUT/conditionsGACD15082022.csv")



