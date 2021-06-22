
import requests 
from bs4 import BeautifulSoup
import pandas as ps

intt=input('Enter the URL of FLIPKART web page  :  ')
#get the page source
data=requests.get(intt)

#convert and store the html data in python object

obj=BeautifulSoup(data.content,features="html.parser")

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
	
		