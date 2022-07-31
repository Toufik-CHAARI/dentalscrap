from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.megadental.fr/brands/kavo-?cat=16029&p=1"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")




filename = "extractmegap1.csv"
headers = "Reference,Prix,Designation,Image,Link \n"

f = open(filename,"w")
f.write(headers)

containers = page_soup.findAll("li",{"class":"item product product-item"})
for contain in containers :
    #contain = containers[1]
    #container = containers[0]

    product_name = contain.strong.text.strip()
    picture = contain.img.get('src')
    link = contain.a.get('href')

    prices = contain.findAll("span",{"class":"price"})

    price = prices[0].text.strip()
    

    refmeg = []
    refmeg = contain.findAll("div",{"class":"value"})
    if len(refmeg)== 0 :
        refmeg = ("is empty")
    else :          
        refmeg= refmeg[0].text.strip()



       
    #f.write(refmeg + "," + price.replace(",", "|") + "," + product_name + "," + picture + "\n")
    f.write(refmeg + ", " + price + ", " + product_name + ", " + picture + ", " + link + "\n")
    #writer.writerow([refmeg.encode('utf-8'), price.encode('utf-8'), product_name.encode('utf-8'),picture.encode('utf-8')])


f.close()
 

   


    