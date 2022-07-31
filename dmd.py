import requests
from bs4 import BeautifulSoup 
import time    

    




 





urlist=["https://dmdentaire.fr/contre-angles/240-contre-angle-kavo-expertmatic-e25l-bague-rouge.html",
"https://dmdentaire.fr/contre-angles/249-contre-angle-kavo-mastermatic-lux-m07l-bague-verte.html",
"https://dmdentaire.fr/contre-angles/250-contre-angle-kavo-mastermatic-lux-m29l-bague-verte.html",
"https://dmdentaire.fr/pieces-main-droite/251-piece-a-main-droite-kavo-mastermatic-lux-m10l.html",
"https://dmdentaire.fr/contre-angles/259-contre-angle-kavo-surgmatic-s201-xl-pro.html",
"https://dmdentaire.fr/contre-angles/260-contre-angle-kavo-surgmatic-s201-l-pro.html",
"https://dmdentaire.fr/pieces-a-main-de-chirurgie/261-piece-a-main-droite-kavo-surgmatic-s11-l.html",
"https://dmdentaire.fr/turbines/238-turbine-kavo-experttorque-e680l.html",
 "https://dmdentaire.fr/turbines/239-turbine-kavo-experttorque-mini-e677l.html",
 "https://dmdentaire.fr/contre-angles/240-contre-angle-kavo-expertmatic-e25l-bague-rouge.html",
 "https://dmdentaire.fr/appareils-abrasion/217-appareil-abrasion-kavo-rondoflex-plus-360-raccord-kavo-multiflex-465-lrn.html",
 "https://dmdentaire.fr/contre-angles/241-contre-angle-kavo-expertmatic-e20l-bague-bleue.html",
 "https://dmdentaire.fr/contre-angles/242-contre-angle-kavo-expertmatic-e15l-bague-verte.html",
 "https://dmdentaire.fr/pieces-main-droite/243-piece-a-main-droite-kavo-expertmatic-e10c.html",
 "https://dmdentaire.fr/turbines/244-turbine-kavo-mastertorque-m9000l.html",
 "https://dmdentaire.fr/turbines/245-turbine-kavo-mastertorque-mini-m8700l.html",
 "https://dmdentaire.fr/contre-angles/246-contre-angle-kavo-mastermatic-lux-m25l-bague-rouge.html",
 "https://dmdentaire.fr/contre-angles/247-contre-angle-kavo-mastermatic-lux-m05l-bague-rouge.html",
 "https://dmdentaire.fr/contre-angles/248-contre-angle-kavo-mastermatic-lux-m20l-bague-bleue.html",
]
for url in urlist:
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    containers = soup.find("div",class_="row product-info-row")
    pname= containers.find("h1",class_="h1 page-title").get_text().strip()
    price = containers.find("span",class_='product-price').get_text().strip()               
    sku = "No SKU"
    url = url
    print (pname,price,sku,url)
    
    


