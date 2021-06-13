
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests 
from bs4 import BeautifulSoup
import pandas as ps


#user input of product
intt=input("Enter The Product Name For You Want To Search  :")

#print(dir(webdriver))

#open firefox 
browser=webdriver.Firefox()

#print(dir(webdriver.Firefox()))

#search the url
browser.get('https://www.flipkart.com/')

#close the login page
cl=browser.find_element_by_xpath('//button[@class ="_2KpZ6l _2doB4z"]')
cl.click()

#find the search box by using html element 
fi=browser.find_element_by_name("q")

#clear the box if any
fi.clear()

#send the user input into search box
fi.send_keys(intt)

#enter the search
fi.send_keys(Keys.RETURN)

#method 1
    #Get the url of searched page
geturl = browser.current_url

    #pass the url to beautifulsoup for getting the data's of the web page
data=requests.get(geturl)   #data=requests.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

    #conver and store the html data in python object
obj=BeautifulSoup(data.content,features="html.parser")

#method 2
#data=browser.page_source
#obj=BeautifulSoup(data,features="html.parser")

while True:
    #empty lists
    a=[]
    b=[]
    c=[]

    for g in obj.findAll('a',href=True,attrs={'class':'_1fQZEK'}):
        name=g.find('div',attrs={'class':'_4rR01T'})
        price=g.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
        spec=g.find('div',attrs={'class':'fMghEO'})
	#append
        a.append(name.text)
        b.append(price.text)
        c.append(spec.text)
    if a and b and c:
	#store the datas in csv file
        df=ps.DataFrame({'Product Name':a,'Price':b,'Specifications':c})
        df.to_csv('product_details.csv',index=False,encoding="utf-8")
        print("Check The Product_details.csv File For Details")
        break
    else:
        f=[]
        G=[]
        h=[]
        for g in obj.findAll('div',attrs={'class':'_4ddWXP'}):
            name=g.find('a',attrs={'class':'s1Q9rs'})
            price=g.find('div',attrs={'class':"_30jeq3"})
            #append
            f.append(name.text)
            G.append(price.text)
    
        for g in obj.findAll('div',attrs={'class':'_4ddWXP'}):
            if g.find('div',attrs={'class':'_3Djpdu'}):
                spec=g.find('div',attrs={'class':'_3Djpdu'})
                h.append(spec.text)
            
        for g in obj.findAll('div',attrs={"class":"_2B099V"}):
            name=g.find('div',attrs={"class":"_2WkVRV"})
            price=g.find('div',attrs={"class":"_30jeq3"})
            #append
            f.append(name.text)
            G.append(price.text)
            
        for g in obj.findAll('div',attrs={"class":"_2B099V"}):
            if g.find('a',attrs={"class":"IRpwTa"}):
                spec=g.find('a',attrs={"class":"IRpwTa"})
                h.append(spec.text)
                      
        if len(f) and len(G) == len(h):
            #store the datas in csv file
            df=ps.DataFrame({'Product Name':f,'Price':G,'Specifications':h})
            df.to_csv('pandas.csv',index=False,encoding="utf-8")
            print("Check The pandas.csv File For Details")
        else:
	    #store the datas in csv file
            df=ps.DataFrame({'Product Name':f,'Price':G})
            df.to_csv('product.csv',index=False,encoding="utf-8")
            print("Check The Product.csv File For Details")
    break
	
		