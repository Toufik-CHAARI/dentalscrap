from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd

from henryschein_byproduct import M07L
#this one is working

productlist=[]

def Rondo():
    link = "https://www.discount-dentaire.fr/achat/rondoflex-plus-360-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="RONDOflex"
    ref_kaVo = "1.002.2179"
    pkavoname = "RONDOflex"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def E25L():
    link = "https://www.discount-dentaire.fr/achat/contre-angle-bague-rouge-kavo-expertmatic-e25l"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="EXPERTmatic"
    ref_kaVo = "1.007.5550"
    pkavoname = "EXPERTmatic E25L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def E20L():
    link = "https://www.discount-dentaire.fr/achat/contre-angle-bague-bleue-kavo-expertmatic-e20l"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="EXPERTmatic"
    ref_kaVo="1.007.5540"
    pkavoname="EXPERTmatic E20L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def E15L():
    link = "https://www.discount-dentaire.fr/achat/contre-angle-bague-verte-kavo-expertmatic-e15l"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="EXPERTmatic"
    ref_kaVo="1.007.5530"
    pkavoname="EXPERTmatic E15L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def E680L():
    link = "https://www.discount-dentaire.fr/achat/turbine-experttorque-e680l-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="EXPERTtorque"
    ref_kaVo="1.006.8700"
    pkavoname="EXPERTtorque E680L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def E677L():
    link = "https://www.discount-dentaire.fr/achat/turbine-experttorque-mini-e677-l-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="EXPERTtorque"
    ref_kaVo="1.007.3600"
    pkavoname="EXPERTtorque E677L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def M25L():
    link = "https://www.discount-dentaire.fr/achat/contre-angle-bague-rouge-kavo-mastermatic-m25l"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="MASTERmatic"
    ref_kaVo="1.009.3630"
    pkavoname="MASTERmatic M25L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def M20L():
    link = "https://www.discount-dentaire.fr/achat/manche-contre-angle-bague-bleue-kavo-mastermatic-m20l"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="MASTERmatic"
    ref_kaVo="1.009.3620"
    pkavoname="MASTERmatic M20L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def M9000L():
    link = "https://www.discount-dentaire.fr/achat/turbine-mastertorque-m9000-l-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="MASTERtorque"
    ref_kaVo="1.008.7900"
    pkavoname="MASTERtorque M9000L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def M8700L():
    link = "https://www.discount-dentaire.fr/achat/turbine-mastertorque-mini-m8700-l-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="MASTERtorque"
    ref_kaVo="3.001.0000"
    pkavoname="MASTERtorque M8700L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def Pf4():
    link ="https://www.discount-dentaire.fr/achat/aeropolisseur-prophyflex-4-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="PROPHYflex"
    ref_kaVo="3.002.8000"
    pkavoname="PROPHYflex 4"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

def Sonic2003l():
    link ="https://www.discount-dentaire.fr/achat/detartreur-sonicflex-2003-l-kavo"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' }
    r=requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    dealer = "DISCOUNT DENTAIRE"
    gamme ="SONICflex"
    ref_kaVo="1.000.8333"
    pkavoname="SONICflex set 2003L"

    try:
        pname= soup.find('div',class_="alpha m0").get_text().strip()
    except:
        pname="None"

    try:
        sku= soup.find('span',class_="text-bold has-color-theme-alt product_reference").get_text().strip()
    except:
        sku="No SKU"

    try:
        price= soup.find('div', class_="card-prices-new").get_text().strip()
    except:
        price="No Price"

    data={
        'dealer' : dealer,
        'gamme': gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'link':link,
        'price':price,
        'pname':pname,
        'sku' :sku,

    }    
    productlist.append(data)
    return(productlist)

E25L()
E20L()
E15L()
E677L()
E680L()
M25L()
M20L()
M9000L()
M8700L()
Pf4()
Sonic2003l()


print(len(productlist))

df=pd.DataFrame(productlist)   
print(df.head())
df.to_csv("extraction/AOUT/conditionsSAFIR15082022.csv")







