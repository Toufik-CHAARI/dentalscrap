import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd    

    
dpi_product =[]

    
def dpi_E25L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10075550-expert-matic-contre-angle-e25l-14210",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTmatic "
            ref_kavo="1.007.5550"
            pkavoname="EXPERTmatic E25L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)
    
def dpi_DUOE25L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10145499-contre-angle-expertmatic-e25l-rouge-duo-pack-31199",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTmatic "
            ref_kavo="1.014.5499"
            pkavoname="Duo-Pack E25L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_E20L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10075540-expert-matic-contre-angle-e20l-2068-lhc-14241",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTmatic "
            ref_kavo="1.007.5540"
            pkavoname="EXPERTmatic E20L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_DUOE20L_E25L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10145475-contre-angle-e25l-e20l-duo-pack-31196",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTmatic "
            ref_kavo="1.014.5475"
            pkavoname="Duo-Pack E25L/E20L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_E15L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10075530-expert-matic-contre-angle-e15l-2068-chc-14282",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTmatic "
            ref_kavo="1.007.5530"
            pkavoname="EXPERTmatic E15L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_E680L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10068700-expert-torque-turbine-e680l-660b-14107",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTtorque "
            ref_kavo="1.006.8700"
            pkavoname="EXPERTtorque E680L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_DUO_E680L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10145478-turbine-expertorque-e680l-duo-pack-31198",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTtorque "
            ref_kavo="1.007.5478"
            pkavoname="EXPERTtorque Duo-Pack E680L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)


def dpi_E677L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10073600-expert-torque-turbine-e677l-637-b-14236",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "EXPERTtorque "
            ref_kavo="1.007.3600"
            pkavoname="EXPERTtorque E677L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M25L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10093630-mastermatic-lux-m25l-14251",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERmatic "
            ref_kavo="1.009.3630"
            pkavoname="MASTERmatic M25L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M20L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10093620-mastermatic-lux-m20l-14250",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERmatic "
            ref_kavo="1.009.3620"
            pkavoname="MASTERmatic M20L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M05L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10093640-mastermatic-lux-m05l-mini-14225",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERmatic "
            ref_kavo="1.009.3640"
            pkavoname="MASTERmatic M05L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M07L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10093610-mastermatic-lux-m07l-14212",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERmatic "
            ref_kavo="1.009.3610"
            pkavoname="MASTERmatic M07L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M10L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10093570-mastermatic-lux-m10l-14202",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERmatic "
            ref_kavo="1.009.3570"
            pkavoname="MASTERmatic M10L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_M9000L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10087900-mastertorque-lux-turbine-m9000l-standard-14249",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "MASTERtorque "
            ref_kavo="1.008.7900"
            pkavoname="MASTERtorque M9000L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)




def dpi_SONIC2008L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10071604-sonicflex-2008l-quick-set-inserts-5a-6a-7a-14270",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "SONICflex"
            ref_kavo="1.007.1604"
            pkavoname="SONICflex set 2008L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

def dpi_SONIC2003L():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10008333-sonicflex-2003l-lux-3inserts-1clef-14137",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "SONICflex"
            ref_kavo="1.000.8333"
            pkavoname="SONICflex set 2003L"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)



def dpi_RONDOflex():
    url =[ 
            "https://www.dentalpromotion.fr/shop/product/25-10022179-rondoflex-plus-14181",
        ]
    for link in url:
        r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        containers = soup.find_all("div",{"class":"singleProductContainer"})

        for contain in containers :
            
            dealer= "DPI FRANCE"
            gamme= "RONDOflex"
            ref_kavo="1.002.2179"
            pkavoname="RONDOflex plus 360"

            try :
                pname = contain.find("div",class_="singleProductName").get_text().strip()
            except AttributeError as err:
                pname = 'None'
            link = link
            
            try :
                price = contain.find("span",{"class":"singleProductCurrentPrice"}).get_text().strip()
            except AttributeError as err:
                price = "None"

            try:
                sku = contain.find("div",class_="singleProductMetaValue").get_text().strip()    
            
            except AttributeError as err:
                sku = "None"
            
                
            product_list ={
                'SKU' : sku,
                'Product_name' : pname,
                'ref_kavo':ref_kavo,
                'pkavoname':pkavoname,
                'Price': price,
                'URL': link,
                'Dealer': dealer,
                'Gamme': gamme
                
            }
            dpi_product.append(product_list)
    time.sleep(2)
    return(dpi_product)

dpi_E25L()
dpi_DUOE25L()
dpi_E20L()
dpi_DUOE20L_E25L()
dpi_E15L()
dpi_E680L()
dpi_DUO_E680L()
dpi_E677L()
dpi_M25L()
dpi_M20L()
dpi_M05L()
dpi_M07L()
dpi_M10L()
dpi_M9000L()

dpi_SONIC2008L()
dpi_SONIC2003L()
dpi_RONDOflex()


print(len(dpi_product))

df=pd.DataFrame(dpi_product)   
print(df.head())
df.to_csv("extraction/AOUT/conditionsDPI15082022.csv")




    
