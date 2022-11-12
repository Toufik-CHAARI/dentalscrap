import requests
from bs4 import BeautifulSoup 
import time    
import pandas as pd
from requests_html import HTMLSession


fullProduxtList =[]    


    

def megaRONDOflex():
    url ="https://www.megadental.fr/rondoflex-plus-360-kavo-886-4072.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)    
    gamme= "RONDOflex"
    dealer="MEGA DENTAL"
    ref_kavo="1.002.2179"
    pkavoname="RONDOflex Plus 360"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-11716"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList

        
def megaSONICflex2008L():
    url = "https://www.megadental.fr/detartreurs-sonicflex-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)  
    gamme="SONICflex"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.1604"
    pkavoname="SONICflex set 2008L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-35074"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' : sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
   

def megaSONICflex2003L():
    url ="https://www.megadental.fr/sonicflex-detartreur-2003l-inserts-567-882-5317.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="SONICflex"
    dealer ="MEGA DENTAL"
    ref_kavo="1.000.8333"
    pkavoname="SONICflex set 2003L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13658"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' : sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
                
      
def megaPROPHYflex():
    url ="https://www.megadental.fr/prophyflex-4-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="PROPHYflex"
    dealer ="MEGA DENTAL"
    ref_kavo="3.002.8000"
    pkavoname="PROPHYflex 4"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-37086"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[3]/div/p/span[2]',first="True").text
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
               

def megaE25L():
    url = "https://www.megadental.fr/contre-angle-rouge-expertmatic-e25l-891-8741.html"     
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5550"
    pkavoname="EXPERTmatic E25L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1436"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price

    }
    fullProduxtList.append(product_list)
    return fullProduxtList
                       

def megaE25C():
    url ="https://www.megadental.fr/contre-angle-rouge-expertmatic-e25c-891-8740.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5551"
    pkavoname="EXPERTmatic E25C"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1435"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price

    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaDuoPackE25L():
    url ="https://www.megadental.fr/duo-pack-contre-angle-expertmatic-e25le25l-897-4993.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5499"
    pkavoname="Duo-Pack E25L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-38145"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaDuoPackE25_E20L():
    url ="https://www.megadental.fr/duo-pack-contres-angles-expertmatic-e25l-e20l-897-4991.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)         
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5475"
    pkavoname="Duo-Pack E25L / E20L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-38144"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)          

def megaDuoPackE20L():
    url ="https://www.megadental.fr/duo-pack-contre-angle-expertmatic-e20le20l-897-4994.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=2)         
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5505"
    pkavoname="Duo-Pack E20L / E20L"
    try :
        pname = r.html.xpath('//*[@id="html-body"]/div[5]/div/div/div/ol/li[5]/a',first="True" ).text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-38146"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
      


def megaE20L():
    url =  "https://www.megadental.fr/contre-angle-expertmatic-bleu-avec-lumiere-e20l-891-8739.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)         
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5540"
    pkavoname="EXPERTmatic E20L"
    try :
        pname =  r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price =  r.html.xpath('//*[@id="product-price-1428"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)              
      
def megaE20C():
    url = "https://www.megadental.fr/contre-angle-expertmatic-bleu-sans-lumiere-e20c-891-8738.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5541"
    pkavoname="EXPERTmatic E20C"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1427"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
    
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaE15L():
    url ="https://www.megadental.fr/contre-angle-expertmatic-vert-avec-lumiere-e15l-891-8737.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5530"
    pkavoname="EXPERTmatic E15L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price =  r.html.xpath('//*[@id="product-price-1434"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku =  r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[3]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :  sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaDuoPackE15L():
    url ="https://www.megadental.fr/duo-pack-e15l-897-8665.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)         
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5559"
    pkavoname="Duo-Pack E15L / E15L"
    try :
        pname = r.html.xpath('//*[@id="html-body"]/div[5]/div/div/div/ol/li[5]/a',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-44889"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)  



def megaE15C():
    url ="https://www.megadental.fr/contre-angle-expertmatic-vert-sans-lumiere-e15c-891-8736.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)       
    gamme="EXPERTmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5531"
    pkavoname="EXPERTmatic E15C"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1433"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div/p/span[2]',first="True").text
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaDuoE680L():
    url = "https://www.megadental.fr/duo-pack-e680l-897-4992.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.5478"
    pkavoname="EXPERTtorque Duo-Pack E680L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-38499"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku =  r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)


def megaE680L():
    url = "https://www.megadental.fr/turbine-experttorque-e680l-891-8744.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="EXPERTtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="1.006.8700"
    pkavoname="EXPERTtorque E680L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1438"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div/p/span[2]',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaE677L():
    url ="https://www.megadental.fr/turbine-experttorque-mini-e677l-891-8742.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)   
    gamme="EXPERTtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="1.007.3600"
    pkavoname="EXPERTtorque E677L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-1437"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaM25L():
    url = "https://www.megadental.fr/contre-angle-m25l-890-5354.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3630"
    pkavoname="MASTERmatic M25L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13675"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)          

def DuoPackM25L():
    url = "https://www.megadental.fr/duo-pack-m25lm25l-897-8663.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5561"
    pkavoname="Duo-Pack MASTERmatic M25L"
    try :
        pname = r.html.xpath('//*[@id="html-body"]/div[5]/div/div/div/ol/li[5]/a',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-44887"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 


def DuoPackM25LM05L():
    url = "https://www.megadental.fr/duo-pack-m25lm05l-897-8664.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5567"
    pkavoname="Duo-Pack MASTERmatic M25L / M20L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[2]/h1',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-44888"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div/p/span[2]',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def DuoPackM9000L():
    url = "https://www.megadental.fr/duo-pack-m9000lm9000l-897-8662.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.5479"
    pkavoname="Duo-Pack MASTERtorque M9000L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[2]/h1',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-44886"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div/p/span[2]',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 



def megaM20L():
    url = "https://www.megadental.fr/manche-de-contre-angle-m20l-890-5355.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3620"
    pkavoname="MASTERmatic M20L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13676"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)             

def megaM05L():
    url ="https://www.megadental.fr/contre-angle-rouge-m05l-mini-mastermatic-890-5353.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3640"
    pkavoname="MASTERmatic M05L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13674"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)


def megaM07L():
    url ="https://www.megadental.fr/manche-contre-angle-vert-m07l-mastermatic-890-5356.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)           
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3610"
    pkavoname="MASTERmatic M07L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13677"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)
            
def megaM29L():
    url ="https://www.megadental.fr/manche-contre-angle-vert-m29l-mastermatic-890-5357.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3580"
    pkavoname="MASTERmatic M29L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13678"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)             

def megaM10L():
    url ="https://www.megadental.fr/piece-a-main-m10l-890-5358.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)   
    gamme="MASTERmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.3570"
    pkavoname="MASTERmatic M10L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-13673"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
        
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaM9000L():
    url ="https://www.megadental.fr/turbines-mastertorque-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    gamme="MASTERtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="1.008.7900"
    pkavoname="MASTERtorque M9000L"
    try :
        pname = r.html.xpath('//*[@id="html-body"]/div[5]/div/div/div/ol/li[5]/a',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-37718"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaM8700L():
    url ="https://www.megadental.fr/turbines-mastertorque-mini-t-te-kavo.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="MASTERtorque"
    dealer ="MEGA DENTAL"
    ref_kavo="3.001.0000"
    pkavoname="MASTERtorque M8700L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-37731"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[3]/div/p/span[2]',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaS11L():
    url ="https://www.megadental.fr/kavo-surgmatic-instruments-892-7785.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)        
    gamme="SURGmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.1010"
    pkavoname="SURGmatic S11L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-16732"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

    'gamme': gamme,
    'dealer': dealer,
    'ref_kavo':ref_kavo,
    'pkavoname':pkavoname,
    'référence' :    sku, 
    'Désignation' : pname,            
    'URL': url,
    'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaS15L():
    url = "https://www.megadental.fr/surgmatic-s15-pro-897-7733.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)       
    gamme="SURGmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.014.4000"
    pkavoname="SURGmatic Pro S15L"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-42277"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text    
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 
            
def megaS201XL():
    url ="https://www.megadental.fr/surgmatic-contre-angle-s201-xl-pro-952-2690.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)     
    gamme="SURGmatic"
    dealer ="MEGA DENTAL"
    ref_kavo="1.013.7541"
    pkavoname="SURGmatic Pro S201XL"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-32752"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2) 

def megaMASTERsurg():
    url ="https://www.megadental.fr/mastersurg-lux-889-0340.html" 
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    gamme="MASTERsurg"
    dealer ="MEGA DENTAL"
    ref_kavo="1.009.1200"
    pkavoname="MASTERsurg"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-4133"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)
            
def megaEXPERTsurg():
    url ="https://www.megadental.fr/moteur-de-chirurgie-expertsurg--kavo-892-7776.html"
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    gamme="EXPERTsurg"
    dealer ="MEGA DENTAL"
    ref_kavo="1.008.3500"
    pkavoname="EXPERTsurg"
    try :
        pname = r.html.xpath('//*[@id="maincontent"]/div[2]/h1/span',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('//*[@id="product-price-16771"]/span',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('//*[@id="maincontent"]/div[3]/div/div[2]/section[1]/div/div/div[3]/div[1]/div[2]/div',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)

def megaQuattrocare():
    url =""
    s = HTMLSession()
    r= s.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    r.html.render(sleep=1)
    gamme="QUATTROcare"
    dealer ="MEGA DENTAL"
    ref_kavo="1.008.3805"
    pkavoname="QUATTROcare Plus 2124A"
    try :
        pname = r.html.xpath('',first="True").text
    except AttributeError as err:
        pname = 'None'
    url = url    
    try :
        price = r.html.xpath('',first="True").text
    except AttributeError as err:
        price = "None"
    try:
        sku = r.html.xpath('',first="True").text
    
    except AttributeError as err:
        sku = "None"
    product_list ={

        'gamme': gamme,
        'dealer': dealer,
        'ref_kavo':ref_kavo,
        'pkavoname':pkavoname,
        'référence' :    sku, 
        'Désignation' : pname,            
        'URL': url,
        'Prix Net' :price
           
    }
    fullProduxtList.append(product_list)
    return fullProduxtList
    time.sleep(2)




megaRONDOflex()

megaSONICflex2008L()
megaSONICflex2003L()
megaPROPHYflex()
megaE25L()
megaE25C()
megaDuoPackE25L()
megaDuoPackE25_E20L()

megaDuoPackE20L()

megaE20L()
megaE20C()
megaE15L()
megaDuoPackE15L()
megaE15C()
megaDuoE680L()
megaE680L()
megaE677L()
megaM25L()
DuoPackM25LM05L()
megaM20L()
megaM05L()
DuoPackM25L()
megaM07L()
megaM29L()
megaM10L()
megaM9000L()
DuoPackM9000L()
megaM8700L()
megaS11L()
megaS15L()
megaS201XL()
megaMASTERsurg()
megaEXPERTsurg()
 



print(len(fullProduxtList))

df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv("extraction/NOVEMBRE/test2.csv")

