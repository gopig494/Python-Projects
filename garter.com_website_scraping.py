import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
import re
import csv
import pandas as p

#open the browser
driver=webdriver.Chrome()

url="https://www.gartner.com/en/glossary/all-terms"

#open the url
driver.get(url)

#store the current url
urls=driver.current_url
#html data
obj=requests.get(urls)
#python readable html data
pyobj=BeautifulSoup(obj.content,features="html.parser")
#empty lists
a=[]
b=[]


#user defind function
def content(bc):
	con=1
	#find and append the content of data
	for j in bc.findAll("div",attrs={"class":"row"}):
		if con !=1:
			data=j.text.replace("\n"," ")
			b.append(data)
			break
		con+=1
		
#counts=0
for j in pyobj.findAll("div",attrs={"class":"item-wrapper"}):
	#count=0
	for i in re.finditer(r'<div class="search-item (.*?)">',str(j)):
		ab=i.group(1)
		#find the link text like .net from the web
		st=driver.find_element_by_link_text(ab)
		#click it
		st.click()
		#getting url
		urls=driver.current_url
		obj=requests.get(urls)
		lobj=BeautifulSoup(obj.content,features="html.parser")
		#find and append the word
		st1=lobj.find("div",attrs={"class":"col-md-12 col-sm-12"})
		a.append(st1.text)
		#function call
		content(lobj)
		#browse back
		driver.back()
		#for testing use below code 
		#if count ==5:
		#	break
		#count+=1
	#counts+=1
	#if counts ==5:
	#	break 
	
#frame and save the data's in csv file		
np=p.DataFrame({"WORD":a,"DESCRIPTION":b})	
np.to_csv('Details.csv',index=False,encoding="utf-8")
print("Check The Details.csv File For Details")
	
		