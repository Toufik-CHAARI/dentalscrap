import requests
from bs4 import BeautifulSoup 
import time
from requests_html import HTMLSession

import pandas as pd






fullProduxtList =[]


def promoRONDOflex():
    link = "https://www.promodentaire.com/sableuse-rondoflex-plus.html"    
         
    
    
    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    soup = BeautifulSoup(r.content,'html.parser')
    containers = soup.find_all("div",{"class":"product-info-main"})

    for contain in containers :
        gamme="RONDOflex"
        dealer="PROMODENTAIRE"
        ref_kavo="1.002.2179"
        pkavoname="RONDOflex Plus 360"
        try :
            pname = contain.find("h1",class_="page-title").get_text().strip()
        except AttributeError as err:
            pname = 'None'
        link = link    
        

        try:
                price = contain.find('span','special-price').text
        except :
                price = contain.find('span','normal-price').text
        
        try:
            sku = contain.find("p",class_="sku-part").get_text().strip()
                
        
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
        
def promoSONIC2003L():
    url =[
              
        "https://www.promodentaire.com/detartreur-sonicflex-2003l.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="SONICflex"
            dealer="PROMODENTAIRE"
            ref_kavo="1.000.8333"
            pkavoname="SONICflex set 2003L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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
            
def promoPF4():
    url =[
              
        "https://www.promodentaire.com/prophyflex-4-aeropolisseur.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="PROPHYflex"
            dealer="PROMODENTAIRE"
            ref_kavo="3.002.8000"
            pkavoname="PROPHYflex 4"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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
  
def promoE25L():
    import time
    url="https://www.promodentaire.com/contre-angle-expertmatic-e25l-1.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTmatic"
    dealer="PROMODENTAIRE"
    ref_kavo="1.007.5550"
    pkavoname="EXPERTmatic E25L"

    try :
        pname = pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)


def promoDuoPackE25L():
    import time
    url="https://www.promodentaire.com/contre-angle-expertmatic-e25l-1.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTmatic"
    dealer="PROMODENTAIRE"
    ref_kavo="1.014.5499"
    pkavoname="Duo-Pack E25L"

    try :
        pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def promoE25C():
    url =[
              
        "https://www.promodentaire.com/contre-angle-expertmatic-e25c.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="EXPERTmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.007.5551"
            pkavoname="EXPERTmatic E25C"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoE15L():
    url =[
              
        "https://www.promodentaire.com/contre-angle-expertmatic-e15l.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="EXPERTmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.007.5530"
            pkavoname="EXPERTmatic E15L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoE15C():
    url =[
              
        "https://www.promodentaire.com/contre-angle-expertmatic-e15c.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="EXPERTmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.007.5531"
            pkavoname="EXPERTmatic E15C"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoE20L():
    import time
    url="https://www.promodentaire.com/contre-angle-expertmatic-e20l-2.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTmatic"
    dealer="PROMODENTAIRE"
    ref_kavo="1.007.5540"
    pkavoname="EXPERTmatic E20L"

    try :
        pname = pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def promoDuoPackE20L():
    import time
    url="https://www.promodentaire.com/contre-angle-expertmatic-e20l-2.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTmatic"
    dealer="PROMODENTAIRE"
    ref_kavo="1.014.5505"
    pkavoname="EXPERTmatic Duo Pack E20L"

    try :
        pname = pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[2]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)    

def promoDuoPackE20L_E25L():
    import time
    url="https://www.promodentaire.com/contre-angle-expertmatic-e20l-2.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTmatic"
    dealer="PROMODENTAIRE"
    ref_kavo="1.014.5475"
    pkavoname="Duo-Pack E25L / E20L"

    try :
        pname = pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)    

def promoE680L():
    import time
    url="https://www.promodentaire.com/turbine-experttorque-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTtorque"
    dealer="PROMODENTAIRE"
    ref_kavo="1.006.8700"
    pkavoname="EXPERTtorque E680L"

    try :
        pname = pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def promoE677L():
    import time
    url="https://www.promodentaire.com/turbine-experttorque-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    gamme="EXPERTtorque"
    dealer="PROMODENTAIRE"
    ref_kavo="1.007.3600"
    pkavoname="EXPERTtorque E677L"

    try :
        pname =  r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    


    try:
        price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[4]/span',first="True").text
    except AttributeError as err:
        price = "None"        
    
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[3]/div[1]',first="True").text

    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'dealer': dealer,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prit Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def promoM25L():
    url =[
              
        "https://www.promodentaire.com/contre-angle-mastermatic-m25l-1-5.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3630"
            pkavoname="MASTERmatic M25L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM20L():
    url =[
              
        "https://www.promodentaire.com/manche-mastermatic-m20l-1-1.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3620"
            pkavoname="MASTERmatic M20L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM05L():
    url =[
              
        "https://www.promodentaire.com/contre-angle-mastermatic-mini-m05l-1-5.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3640"
            pkavoname="MASTERmatic M05L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM07L():
    url =[
              
        "https://www.promodentaire.com/manche-mastermatic-lux-m07l-2-7-1.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3610"
            pkavoname="MASTERmatic M07L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM29L():
    url =[
              
        "https://www.promodentaire.com/manche-mastermatic-lux-m29l-7-4-1.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3580"
            pkavoname="MASTERmatic M29L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM10L():
    url =[
              
        "https://www.promodentaire.com/piece-a-main-mastermatic-lux-m10l-1-1.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.3570"
            pkavoname="MASTERmatic M10L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoM9000L():
    
    url="https://www.promodentaire.com/turbine-mastertorque-lux-m9000l.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
    r.html.render(sleep=1)
    
        
    gamme="MASTERtorque"
    dealer="PROMODENTAIRE"
    ref_kavo="1.008.7900"
    pkavoname="MASTERtorque M9000L"

    try :
        pname = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[2]/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    link = url    
    

    try:
            price = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[3]/div/div/span/span/span[2]',first="True").text
    except :
            price = "None"
    try:
        sku = r.html.xpath('//*[@id="table_all_variations"]/div[1]/div[2]/div[1]/div[1]',first="True").text    
    
    except AttributeError as err:
        sku = "None"
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

def promoM8700L():
    url =[
              
        "https://www.promodentaire.com/turbine-mastertorque-mini-m8700l.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="MASTERtorque"
            dealer="PROMODENTAIRE"
            ref_kavo="3.001.0000"
            pkavoname="MASTERtorque M8700L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoS11L(): 
    url =[
              
        "https://www.promodentaire.com/p-a-m-surgmatic-s11l-1-1.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="SURGmatic"
            dealer="PROMODENTAIRE"
            ref_kavo="1.009.1010"
            pkavoname="SURGmatic S11L"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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

def promoEXPERTsurg():
    url =[
              
        "https://www.promodentaire.com/expertsurg-lux-moteur-de-chirurgie.html",
        
         ]
    
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"product-info-main"})

        for contain in containers :
            gamme="EXPERTsurg"
            dealer="PROMODENTAIRE"
            ref_kavo="1.008.3500"
            pkavoname="EXPERTsurg"

            try :
                pname = contain.find("h1",class_="page-title").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link    
          
        
            try:
                    price = contain.find('span','special-price').text
            except :
                    price = contain.find('span','normal-price').text
            try:
                sku = contain.find("p",class_="sku-part").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
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



promoRONDOflex()

promoSONIC2003L()
promoPF4()
promoE25L()
promoE25C()
promoE20L()
promoDuoPackE25L()
promoDuoPackE20L()
promoDuoPackE20L_E25L()
promoE15L()
promoE15C()
promoE680L()
promoE677L()
promoM25L()
promoM20L()
promoM05L()
promoM07L()
promoM29L()
promoM10L()
promoM9000L()
promoM8700L()
promoS11L()
promoEXPERTsurg()



print(len(fullProduxtList))

df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('extraction/OCTOBRE/conditionspromodentaire08102022.csv')

