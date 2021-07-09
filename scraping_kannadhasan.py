# scraping of http://www.kannadasanpathippagam.com/?route=common/home web.
from bs4 import BeautifulSoup
from time import sleep
import requests
import sqlite3
import pandas
import re
from selenium import webdriver
import os

res=requests.get('http://www.kannadasanpathippagam.com/?route=common/home')
sleep(1)
content=BeautifulSoup(res.content,features='html.parser')

#empty lists
cat_url=[] #7 #47 #category url store
cat=[]  #category title  # 10 to 51 required category range	
page_url=[1] #next and next page url store
string="" #for filtering '/' for file error in book titile
tem=""    #for filtering '/' for file error in book category
p_url_max=[] #after page 11 or amx page reach on each category
n=0  #range 
full_pg_url=[] #for store all page url's

#count
cat_count=10
	
#for storing in csv
category=[] #book category
book_titile=[] #book titles append	
	
#find the url of each category 
for i in content.findAll("a"):
	if i:
		cat.append(i.text)
	hyp=i.get("href")
	if hyp:
		if hyp.startswith("h"):
			cat_url.append(hyp)
			
#getting required url from the list
for k in range(7,47):
	ifs=cat_url[k]+"?page=1"
	ifd=cat_url[k]+"&page=1"
	print(cat[cat_count],'Category is working on')
	res=requests.get(cat_url[k])
	sleep(1)
	content=BeautifulSoup(res.content,features='html.parser')
	#get the all next and next pages url
	for l in content.findAll("div",attrs={"class":"links"}):
		for u in l.findAll("a"):
			pg=u.get("href")
			if pg not in page_url:
				page_url.append(pg)
				full_pg_url.append(pg)
	aw=int(len(page_url))
	print("length of page from",n,"to",aw)
	#getting next and next page
	while True:
		for con in range(n,aw):			
			if con==0:
				res1=requests.get(cat_url[k])
				sleep(2)
				content=BeautifulSoup(res1.content,features='html.parser')
			else:
				res1=requests.get(page_url[con])
				sleep(2)
				content=BeautifulSoup(res1.content,features='html.parser')

			#all book title finder of a page
			for r in content.findAll("div",attrs={"class":"row-fluid box-product"}):
				for images in r.findAll("img"):
					bk=images.get("title")
					if '/' in bk :
						for bks in bk:
							if bks.isalnum():
								string+=bks
						bk=string
					book_titile.append(bk)
					#category append for csv
					c=cat[cat_count]
					if '/' in c :
						for ck in c:
							if ck.isalnum():
								tem+=ck
						c=tem
					category.append(c)
					#images url finder  
					i_url=images.get("src")
					#print('imges url',i_url)
					rep=requests.get(i_url)
					sleep(5)
					print('Title :',bk,"is Working On")
					try:
						os.makedirs(f'/home/gopi/Pictures/kannadasanpathippagam/{c}')
						f=open(f'/home/gopi/Pictures/kannadasanpathippagam/{c}/{bk}.jpg','wb')
						f.write(rep.content)
						sleep(5)
					except FileExistsError:
						f=open(f'/home/gopi/Pictures/kannadasanpathippagam/{c}/{bk}.jpg','wb')
						f.write(rep.content)
						sleep(5)
					string=''
					tem=''
			print(f"Page {con+1} Completed")
		p_url_max.append(1)	
		#finding next next pages after reaching max page of each category	
		for l in content.findAll("div",attrs={"class":"links"}):
			for u in l.findAll("a"):
				pg=u.get("href")
				if pg not in full_pg_url:
					if pg not in ifs:
						if pg not in ifd:
							#print('Max page',pg)
							full_pg_url.append(pg)
							p_url_max.append(pg)
					
		if len(p_url_max)>1:
			page_url.clear()
			page_url=p_url_max.copy()
			p_url_max.clear()
			aw=len(page_url)
			n=1
			continue		
		print(cat[cat_count],'is Completed')
		p_url_max.clear()
		page_url.clear()
		#appending 1 for category first page take in range
		page_url.append(1)
		if cat[cat_count]=="ZEN":
			cat_count+=2
		elif cat[cat_count]=="Zig Zigler":
			cat_count+=2
		else:	
			cat_count+=1	
		n=0
		break
st=pandas.DataFrame({"Category":category,"Title":book_titile})
st.to_csv("kannadas.csv",index=False,encoding="utf-8")
print("Scraping Completed")
print("Check The kannadas.csv File For Details")