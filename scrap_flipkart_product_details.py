
import requests 
from bs4 import BeautifulSoup
import pandas as ps

#get the page source
data=requests.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")

#convert and store the html data in python object

obj=BeautifulSoup(data.content,features="html.parser")

#empty lists
a=[]
b=[]
c=[]


for g in obj.findAll('a',href=True,attrs={'class':'_1fQZEK'}):
	name=g.find('div',attrs={'class':'_4rR01T'})
	price=g.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
	spec=g.find('div',attrs={'class':'fMghEO'})
	
	a.append(name.text)
	b.append(price.text)
	c.append(spec.text)
	
#store the datas in csv file 
df=ps.DataFrame({'Product Name':a,'Price':b,'Specifications':c})
df.to_csv('product_details.csv',index=False,encoding="utf-8")
	
