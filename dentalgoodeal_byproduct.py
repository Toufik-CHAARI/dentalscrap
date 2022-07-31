import requests
from bs4 import BeautifulSoup 
import time  
import pandas as pd  

    






productlist=[]


def dentGooddealE25l():
    link= "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
    #urlist=["https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html","https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"]

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo = "1.007.5550"
            pkavoname = "EXPERTmatic E25L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            if "161713" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)       
       
#duopack E25L dentalgooddeal
def dentGooddealDuoPackE25l():
    link= "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
    #urlist=["https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html","https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"]

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo="1.014.5499"
            pkavoname="Duo-Pack E25L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            if "183395" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#E20L dentalgooddeal
def dentGooddealE20l():
    link= "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo="1.007.5540"
            pkavoname="EXPERTmatic E20L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            if "161711" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#dentalgooddeal e20c
def dentGooddealE20c():
    link= "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
    #urlist=["https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html","https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"]

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo="1.007.5541"
            pkavoname="EXPERTmatic E20C"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            if "161710" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#DENTALGOODDEAL E15L
def dentGooddealE15L():
    link= "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
    #urlist=["https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html","https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"]

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo="1.007.5530"
            pkavoname="EXPERTmatic E15L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            if "161709" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#DENTALGOODDEAL PROPHYFLEX4
def dentGooddealPF4():
    link= "https://www.dentalgooddeal.com/article_prophyflex_4_universel_kavo_180085_98054_68450.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "PROPHYflex 4"
            ref_kaVo="3.002.8000"
            pkavoname="PROPHYflex 4"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "180085" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#SONICflex 2008L
def dentGooddealSonic2008l():
    link= "https://www.dentalgooddeal.com/article_sonicflex_2008l_kavo_170165_94670_66292.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "SONICflex"
            ref_kaVo="1.005.9310"
            pkavoname="SONICflex 2008L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "170165" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#SONICflex 2003L
def dentGooddealSonic2003l():
    link= "https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "SONICflex"
            ref_kaVo="1.000.8333"
            pkavoname="SONICflex set 2003L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "162539" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#EXPERT E10C
def dentGooddealE10C():
    link= "https://www.dentalgooddeal.com/article_piece_a_main_expertmatic_e10_c_kavo_168019_94369_66024.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTmatic"
            ref_kaVo="1.007.5560"
            pkavoname="EXPERTmatic E10C"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "168019" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#EXPERTtorque
def dentGooddealE680l():
    link= "https://www.dentalgooddeal.com/article_experttorque_kavo_171321_94392_66060.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "EXPERTtorque"
            ref_kaVo="1.006.8700"
            pkavoname="EXPERTtorque E680L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "171321" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#MASTERtorque M9000L
def dentGooddealM9000l():
    link= "https://www.dentalgooddeal.com/article_mastertorque__kavo_master_series_171323_94383_66049.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "MASTERtorque"
            ref_kaVo="1.008.7900"
            pkavoname="MASTERtorque M9000L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "171323" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#SURGMATIC S11L
def dentGooddealS11l():
    link= "https://www.dentalgooddeal.com/article_p_a_m__surgmatic_s11l_1_1_kavo_183320_99106_68934.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "SURGmatic"
            ref_kaVo="1.009.1010"
            pkavoname="SURGmatic S11L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "183320" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)

#MASTERMATIC M10L
def dentGooddealm10l():
    link= "https://www.dentalgooddeal.com/article_piece_a_main_mastermatic_lux_m10l_kavo_183730_99399_69009.html"
    

    r= requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})

    for item in containers.find_all('div', class_="fiche_article_article"):
            dealer = "Dental Gooddeal"
            gamme = "MASTERmatic"
            ref_kaVo="1.009.3570"
            pkavoname="MASTERmatic M10L"            
            sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
            price =item.find('div',class_="article_prix").get_text().strip() 
            pname = item.find('img')['alt']
            
            if "183730" in sku:
                data ={
                    'dealer':dealer,
                    'gamme': gamme,
                    'ref_kaVo':ref_kaVo,
                    'pkavoname':pkavoname,
                    'sku':sku,
                    'price':price,
                    'pname':pname,
                    'link':link,
                    
                }
                productlist.append(data)
                
                return(productlist)
                time.sleep(2)


dentGooddealE15L()
dentGooddealDuoPackE25l()
dentGooddealE25l()
dentGooddealE20l()
dentGooddealE20c()
dentGooddealPF4()
dentGooddealSonic2008l()
dentGooddealSonic2003l()
dentGooddealE10C()
dentGooddealE680l()
dentGooddealM9000l()
dentGooddealS11l()
dentGooddealm10l()      





print(len(productlist))

df=pd.DataFrame(productlist)   
print(df.head())
df.to_csv("extraction/JUILLET/conditionsdentalgoogdeal19072022.csv")        

