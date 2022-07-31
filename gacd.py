from requests_html import HTMLSession
import time
import pandas as pd
#method request for web_scrapping via https://www.youtube.com/watch?v=MeBU-4Xs2RU&list=PLUmNF2vh_P8rbtckS1NDrrqFINvh9eyD3&index=23&t=428s

#this is the right one MY FRIEND devellopped following gacd website update
# do not change


fullProduxtList =[]

for x in range (1,18):

    
    url="https://www.gacd.fr/nos-marques/k/kavo.html?is_ajax=1&p="    
        
    # opens the connection and downloads html page from url
    s = HTMLSession()
    r = s.get(url+ str(x))
    r.html.render(sleep=1)
    products = r.html.xpath('//*[@id="amasty-shopby-product-list"]/div[2]/ol',first=True)
    
    
    for items in products.absolute_links:
        r= s.get(items)
        url = items
        
        try:
            pname=r.html.find('span.base',first=True).text
        except AttributeError as err:  
            pname ='None'  
        #print(pname)
        
        
        try:
            sku=r.html.find('div.reference-attribute-container',first=True).text
        except AttributeError as err:
            sku = 'None'

        #print(sku)   
            
                   
        
        
        try:
            price =  r.html.find('span.price',first=True).text
        except AttributeError as err:
            price ='None'    
        #print(sku,pname,price,url)
         
        product_list ={
            'SKU' : sku,
            'Product_name' : pname,
            'Price': price,
            'URL': url
                    }
        fullProduxtList.append(product_list) 
        time.sleep(2)



df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsgacd20022022.csv')               


'''

products = r.html.find('ol',first=True)





for items in products.links:
    url = items
    r= s.get(items)
            
    pname=r.html.find('span.base',first=True).text
            
    try:
        sku=r.html.find('span.reference-attribute-value',first=True).text
    except:
        sku=('pas de sku')
    price =  r.html.find('span.price',first=True).text
    #print(pname,sku,price,url)

    product_list ={
        'SKU' : sku,
        'Product_name' : pname,
        'Price': price,
        'URL': url
                }
    fullProduxtList.append(product_list)
    time.sleep(1)    
     

'''


'''
df=pd.DataFrame(fullProduxtList)   
print(df.head())
df.to_csv('conditionsgacd06032021.csv')       
'''   
    
    
    
    
        

    

        
             
    
            
       
    



    