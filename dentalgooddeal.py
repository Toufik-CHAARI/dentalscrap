import requests
from bs4 import BeautifulSoup 
import time    

    




url1 = "https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html"
url2 = "https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"
url3 = "https://www.dentalgooddeal.com/article_mastertorque__kavo_master_series_171323_94383_66049.html"
url4 ="https://www.dentalgooddeal.com/article_prophyflex_4_universel_kavo_180085_98054_68450.html"
url5="https://www.dentalgooddeal.com/article_experttorque_kavo_171321_94392_66060.html"
url6="https://www.dentalgooddeal.com/article_p_a_m__surgmatic_s11l_1_1_kavo_183320_99106_68934.html"

urlist=[url1,url2,url3,url4,url5,url6]
#urlist=["https://www.dentalgooddeal.com/article_contre_angles_expertmatic_kavo_161709_94325_65961.html","https://www.dentalgooddeal.com/article_sonicflex_lux_2003l_kavo_162539_94568_66226.html"]
for url in urlist:
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    containers = soup.find("div",{"id":"divFicheArticleDescriptionProduits"})
                   

    for item in containers.find_all('div', class_="fiche_article_article"):
        sku = item.find('span',class_="fiche_article_article_ref").get_text().strip().split()[-1]    
        price =item.find('div',class_="article_prix").get_text().strip() 
        pname = item.find('img')['alt']
        
        print(sku,price,pname)


