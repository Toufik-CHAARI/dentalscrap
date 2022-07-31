import requests
import time
from bs4 import BeautifulSoup
import pandas as pd 

product_list=[]


def E20L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-bleu-expertmatic-e20l-kavo/891-8739"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5540"
    pkavoname="EXPERTmatic E20L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E20C():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-bleu-expertmatic-e20c-kavo/891-8738"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5541"
    pkavoname="EXPERTmatic E20C"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def DuopackE20L():
    link="https://www.henryschein.fr/fr-fr/corp/p/nouveautes/nouveautes/duo-pack-e20l-10145505-kavo/897-4994"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.014.5505"
    pkavoname="EXPERTmatic Duo Pack E20L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E25L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-rouge-expertmatic-e25l-kavo/891-8741"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5550"
    pkavoname="EXPERTmatic E25L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E25C():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-rouge-expertmatic-e25c-kavo/891-8740"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5551"
    pkavoname="EXPERTmatic E25C"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def DuoPackE25l():
    link="https://www.henryschein.fr/fr-fr/corp/p/nouveautes/nouveautes/duo-pack-e25l-10145499-kavo/897-4993"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.014.5499"
    pkavoname="Duo-Pack E25L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def DuoPackE25_E20L():
    link="https://www.henryschein.fr/fr-fr/corp/p/nouveautes/nouveautes/duo-pack-e25-l-e20-l-10145475-kavo/897-4991"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.014.5475"
    pkavoname="Duo-Pack E25L / E20L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E15L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-vert-expertmatic-e15l-kavo/891-8737"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5530"
    pkavoname="EXPERTmatic E15L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E15C():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-vert-expertmatic-e15c-kavo/891-8736"

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5531"
    pkavoname="EXPERTmatic E15C"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def DuoE680L():
    link="https://www.henryschein.fr/fr-fr/corp/p/nouveautes/nouveautes/duo-pack-e680l-10145478-kavo/897-4992"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTtorque"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.5478"
    pkavoname="EXPERTtorque Duo-Pack E680L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E680L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/turbine-experttorque-e680l-kavo/891-8744"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTtorque"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.006.8700"
    pkavoname="EXPERTtorque E680L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def E677L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/turbine-experttorque-e677l-kavo/891-8742"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTtorque"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.3600"
    pkavoname="EXPERTtorque E677L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M25L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-m25l-mastermatic-kavo/890-5354"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3630"
    pkavoname="MASTERmatic M25L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M20L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/manche-de-contre-angle-m20l-mastermatic-kavo/890-5355"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3620"
    pkavoname="MASTERmatic M20L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M05L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/contre-angle-m05l-mini-mastermatic-kavo/890-5353"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3640"
    pkavoname="MASTERmatic M05L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M07L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/manche-de-contre-angle-m07l-mastermatic-kavo/890-5356"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3610"
    pkavoname="MASTERmatic M07L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M29L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/manche-de-contre-angle-m29l-mastermatic-kavo/890-5357"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3580"
    pkavoname="MASTERmatic M29L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M10L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/piece-a-main-mastermatic-m10l-kavo/890-5358"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.3570"
    pkavoname="MASTERmatic M10L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M9000L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/turbine-mastertorque-m9000l-grise-raccord-kavo-kavo/890-2498"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERtorque"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.008.7900"
    pkavoname="MASTERmatic M9000L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def M8700L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/turbine-mastertorque-mini-lux-8700l-kavo/892-8673"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERtorque"
    dealer ="HENRY SCHEIN"
    ref_kavo="3.001.0000"
    pkavoname="MASTERmatic M8700L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Sonic2008L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/detartreurs/sonicflex-2008l-kavo-avec-3-inserts-5a-6a-7a/950-7995"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="SONICflex"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.007.1604"
    pkavoname="SONICflex set 2008L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Sonic2003L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/detartreurs/sonicflex-2003l-kavo-avec-3-inserts-5-6-7/882-5317"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="SONICflex"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.000.8333"
    pkavoname="SONICflex set 2003L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Rondoflex():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/aeropolisseurs/rondoflex-plus-360-kavo/886-4072"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="RONDOflex"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.002.2179"
    pkavoname="RONDOflex Plus 360"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Pf4():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/aeropolisseurs/prophyflex-4-bleu-kavo-raccord-kavo/895-4519"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="PROPHYflex"
    dealer ="HENRY SCHEIN"
    ref_kavo="3.002.8000"
    pkavoname="PROPHYflex 4"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def S11L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/contre-angles-et-pam-de-chirurgie-implantologie/piece-a-main-surgmatic-s11l-kavo/892-7785"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="SURGmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.1010"
    pkavoname="SURGmatic S11L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def S15L():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/instrumentation-rotative/surgmatic-s15l-pro-kavo/897-7733"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="SURGmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.014.4000"
    pkavoname="SURGmatic Pro S15L"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def S201XL():
    link="https://www.henryschein.fr/fr-fr/corp/p/nouveautes/nouveautes/surgmatic-s201-xl-pro-avec-tete-1-013-7541-kavo/952-2690"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="SURGmatic"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.013.7541"
    pkavoname="SURGmatic Pro S201XL"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Mastersurg():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/moteurs-de-chirurgie-implantologie/moteur-mastersurg-lux-kavo/889-0340"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="MASTERsurg"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.009.1200"
    pkavoname="MASTERsurg"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

def Expertsurg():
    link="https://www.henryschein.fr/fr-fr/corp/p/petit-equipement/moteurs-de-chirurgie-implantologie/moteur-expertsurg-kavo/892-7776"
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    contain = soup.find("div",{"class":"product"})


    gamme="EXPERTsurg"
    dealer ="HENRY SCHEIN"
    ref_kavo="1.008.3500"
    pkavoname="EXPERTsurg"

    try :
        pname = soup.find('h1',class_="title").text
    except AttributeError as err:
        pname = 'No Product Name'



    try :
        price = contain.find("div",{"class":"product-price"}).get_text().strip().replace(' ¤','€')
    except AttributeError as err:
        price = "None"

    try:
        sku = contain.find("small",class_="x-small").get_text().strip().split()[-5].replace(' ','')    
    except AttributeError as err:
        sku = "None"      

    link = link


    data5 ={

    'gamme':gamme,
    'pkavoname':pkavoname,
    'ref_kavo':ref_kavo,
    'dealer':dealer,         
    'pname':pname,
    'price':price,
    'sku':sku,            
    'link':link,
                
    }

    product_list.append(data5)
    time.sleep(2)
    
    return(product_list)

E20L()
E20C()
DuopackE20L()
E25L()
E25C()
DuoPackE25l()
DuoPackE25_E20L()
E15L()
E15C()
DuoE680L()
E680L()
E677L()
M25L()
M20L()
M05L()
M07L()
M29L()
M10L()
M9000L()
M8700L()
Sonic2008L()
Sonic2003L()
Rondoflex()
Pf4()
S11L()
S15L()
S201XL()
Mastersurg()
Expertsurg()


print(len(product_list))

df=pd.DataFrame(product_list)   
print(df.head())
df.to_csv("extraction/JUILLET/conditionsHSF19072022.csv")


