from requests_html import HTMLSession

import pandas as pd
#does not work



fullProduxtList =[]


#headers = {'User-Agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}



    

url ='https://www.dentalpromotion.fr/shop/page/2?search=kavo&attrib=0-153'  
s = HTMLSession()
r = s.get(url,headers=headers, verify=False)
#response = requests.request("GET", url, headers=headers, verify=False)



r.html.render(sleep=1)



#productlist = r.html.xpath('//*[@id="wrapwrap"]/main/div/div[2]/div[2]', first=True)
productlist = r.html.find('div.an_shop')
print(productlist.html)


#for item in productlist:

    #url= item
    #r= s.get(item)
    #print (item.find('div', first=True).attrs['data-redirection'])

'''    
    try:
        p_name = r.html.find('div.an_shop_article_title',first=True).text
    except:
        p_name = ('pas ne designation')
    try:
        price=r.html.find('span.oe_currency_value',first=True).text
    except:
        price=('pas de prix')    
    
    try:
        skuKav=r.html.xpath('//*[@id="wrap"]/div[2]/div[2]/div[2]').text            
    except:
        skuKav=('pas de sku')
    print(p_name)    
    


  '''  
    
'''

    url= item
    r= s.get(item)
    try:
        skuKav=r.html.find('h4',first=True).text
            
    except:
        skuKav=('pas de sku')

    try:
        p_name = r.html.find('h1.titre_produit',first=True).text
    except:
        p_name = ('pas ne designation') 
        
    try:
        price=r.html.find('span.prix',first=True).text
    except:
        price=('pas de prix')          

    product_list ={
        'SKU' : skuKav,
        'Product_name' : p_name,
        'Price': price,
        'URL': url
            
    }
    fullProduxtList.append(product_list)

print(len(fullProduxtList))
df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsdpifrance10042021.csv')        

'''