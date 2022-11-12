from email.quoprimime import quote
import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd


productlist =[]


def E25L ():
    url = "https://www.doctorstrong.fr/contre-angle-rouge-expertmatic-e25l-kavo-891-8741.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo = "1.007.5550"
    pkavoname = "EXPERTmatic E25L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname = 'None'
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku = 'None'
    try:
        price = soup.find("span",{"class":"special-price"}).text
    except AttributeError as err:
        price = 'None'
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def E25C ():
    url = "https://www.doctorstrong.fr/contre-angle-rouge-expertmatic-e25c-kavo-891-8740.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo = "1.007.5551"
    pkavoname = "EXPERTmatic E25C"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname ="None"

    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"

    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"

    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def E20L ():
    url = "https://www.doctorstrong.fr/contre-angle-expertmatic-bleu-avec-lumiere-e20l-kavo-891-8739.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.5540"
    pkavoname="EXPERTmatic E20L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"

    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def E20C ():
    url = "https://www.doctorstrong.fr/contre-angle-expertmatic-bleu-sans-lumiere-e20c-kavo-891-8738.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.5541"
    pkavoname="EXPERTmatic E20C"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:  
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:  
        price="None"
         
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def E15L ():
    url = "https://www.doctorstrong.fr/contre-angle-expertmatic-vert-avec-lumiere-e15l-kavo-891-8737.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.5530"
    pkavoname="EXPERTmatic E15L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname ="None"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"

    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def E15C ():
    url = "https://www.doctorstrong.fr/contre-angle-expertmatic-vert-sans-lumiere-e15c-kavo-891-8736.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.5531"
    pkavoname="EXPERTmatic E15C"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def E10C ():
    url = "https://www.doctorstrong.fr/piece-a-main-expertmatic-e10c-kavo-891-8735.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.5560"
    pkavoname="EXPERTmatic E10C"
    try :
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="Name"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price ="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def E680L ():
    url = "https://www.doctorstrong.fr/turbine-experttorque-e680l-kavo-891-8744.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.006.8700"
    pkavoname="EXPERTtorque E680L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def E677L ():
    url = "https://www.doctorstrong.fr/turbine-experttorque-mini-e677l-kavo-891-8742.html"
    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "EXPERTmatic"
    ref_kaVo="1.007.3600"
    pkavoname="EXPERTtorque E677L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="Name"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def M25L ():
    url = "https://www.doctorstrong.fr/contre-angle-m25l-kavo-890-5354.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3630"
    pkavoname="MASTERmatic M25L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname ="None"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def M05L ():
    url = "https://www.doctorstrong.fr/contre-angle-rouge-m05l-mini-mastermatic-kavo-890-5353.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3640"
    pkavoname="MASTERmatic M05L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def M20L ():
    url = "https://www.doctorstrong.fr/manche-de-contre-angle-m20l-kavo-890-5355.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3620"
    pkavoname="MASTERmatic M20L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname ="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def M07L ():
    url = "https://www.doctorstrong.fr/manche-contre-angle-vert-m07l-mastermatic-kavo-890-5356.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3610"
    pkavoname="MASTERmatic M07L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist) 


def M29L ():
    url = "https://www.doctorstrong.fr/manche-contre-angle-vert-m29l-mastermatic-kavo-890-5357.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3580"
    pkavoname="MASTERmatic M29L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname ="None"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist) 


def M10L ():
    url = "https://www.doctorstrong.fr/piece-a-main-m10l-kavo-890-5358.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTmatic"
    ref_kaVo="1.009.3570"
    pkavoname="MASTERmatic M10L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:    
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)



def M8700L ():
    url = "https://www.doctorstrong.fr/turbines-mastertorque-mini-t-te-kavo.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTtorque"
    ref_kaVo="3.001.0000"
    pkavoname="MASTERTtorque M8700L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"

    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def M9000L ():
    url = "https://www.doctorstrong.fr/turbines-mastertorque-kavo.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "MASTERTtorque"
    ref_kaVo="1.008.7900"
    pkavoname="MASTERTtorque M9000L"
    try: 
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku ="None"

    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def Rondo ():
    url = "https://www.doctorstrong.fr/rondoflex-plus-360-kavo-886-4072.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "RONDOflex"
    ref_kaVo="1.002.2179"
    pkavoname="RONDOflex Plus 360"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def Sonic2008l ():
    url = "https://www.doctorstrong.fr/detartreurs-sonicflex-kavo.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "SONICflex"
    ref_kaVo="1.007.1604"
    pkavoname="SONICflex set 2008L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def Sonic2003l ():
    url = "https://www.doctorstrong.fr/sonicflex-detartreur-2003l-inserts-567-kavo-882-5317.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "SONICflex"
    ref_kaVo="1.000.8333"
    pkavoname="SONICflex set 2003L"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"
    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)


def Prophyflex ():
    url = "https://www.doctorstrong.fr/prophyflex-4-kavo.html"


    r= requests.get(url ,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    dealer= "DOCTOR STRONG"
    gamme = "PROPHYflex"
    ref_kaVo="3.002.8000"
    pkavoname="PROPHYflex 4"
    try:
        pname = soup.find("span",{"class":"base"}).text
    except AttributeError as err:
        pname="None"
    try:
        sku= soup.find("div",{"class":"product attibute code_strong sku"}).text.split()[-1]
    except AttributeError as err:
        sku="None"
    try:    
        price = soup.find("span",{"class":"special-price"}).text.replace(' ','').strip()
    except AttributeError as err:
        price="None"

    data = {
        'dealer':dealer,
        'gamme' : gamme,
        'ref_kaVo' : ref_kaVo,
        'pkavoname' : pkavoname,
        'pname':pname,
        'sku':sku,
        'price':price,
        'url':url,
    }
    productlist.append(data)
    return(productlist)







E25L()
E25C()
E20L()
E25C()
E15L()
E15C()
E10C()
E680L()
E677L()
M25L()
M05L()
M20L()
M07L()
M29L()
M10L()
M8700L()
M9000L()
Rondo()
Sonic2008l()
Sonic2003l()
Prophyflex()



print(len(productlist))
df=pd.DataFrame(productlist)   
print(df.head())
df.to_csv('extraction/OCTOBRE/conditionsdoctorstrong08102022.csv')


