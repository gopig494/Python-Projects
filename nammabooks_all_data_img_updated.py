#scrap the web of https://nammabooks.com/index.php?route=product/category&path
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas 
import re 
import os 
from time import sleep

opts =webdriver.FirefoxOptions()
opts.headless=True
driver=webdriver.Firefox(options=opts)
driver.get("https://nammabooks.com/index.php?route=product/category&path")
sleep(1)
rurl=driver.current_url
sleep(1)
res=requests.get(rurl)
sleep(1)
html=BeautifulSoup(res.content,features="html.parser")

imgs=[] #images url list
other=[] #filter append
link=[] #href append

T=[]
A=[]
P=[]
S=[]
D=[]
num=[] #link text append
cat=[] #category
numl=[]
nukl=[]

for a in html.findAll("a"):
	stli=a.get("href")
	for h in re.finditer(r"(#ca.*)",str(stli)):
		gp=h.group(1)
		other.append(gp)
	if stli and stli!="#":
		if stli not in other:
			link.append(stli)

#print(link[545])
#print(link[114])

#unwanted links append
ab=[link[171],link[172],link[173],link[174],link[175],link[176],link[178],link[179],link[180],link[181],link[182],link[183]]

orl=[]
st=114
while st<546:
	if link[st] not in ab and link[st] != link[177] :
		orl.append(link[st])
	st+=1
	
#category finder
category=[]
ct=0
for a in html.findAll("a"):  #114 #353
	if ct > 114 and ct < 353:
		if ct != 174 and ct != 175 and ct != 176 and ct != 177 and ct != 178 and ct != 179 and ct != 180 and ct != 181 and ct != 182 and ct != 183 and ct != 184 and ct != 185 and ct != 186 and ct != 187: #174 #187
			mnp=a.text.replace("\s\n\t","")
			if mnp:
				category.append(a.text)				
				#print("ct",ct,a.text)				
	ct+=1
hi=0
#category page open
for i in orl:
	print(i,"is Working On")
	driver.get(i)
	resp=requests.get(i)
	sleep(1)
	ht=BeautifulSoup(resp.content,features="html.parser")
	try:
		#find total number of pages
		for Gk in ht.findAll("a"):
			nu=Gk.text
			if nu.isnumeric():
				num.append(nu)
		lem=len(num)+1
	except:
		lem=1
	num.clear()
	#page changing loop	
	while True:
		#1
		if int(lem) <=9:
			for G in range(0,int(lem)+1): 
				check=""
				if G == 0:
					rest=requests.get(i)
					sleep(1)
					check=str(rest)
				if G != 1 and G != 0:
					amt=str(G)
					#print("page first",amt)
					clk=driver.find_element_by_link_text(amt)
					clk.click()
					sleep(1)
					urtl=driver.current_url
					rest=requests.get(urtl)
					sleep(1)
					check=str(rest)					
           
				#getting each book details
				if check == "<Response [200]>" or "<Response [404]>":
					ob=BeautifulSoup(rest.content,features="html.parser")
					sleep(1)
					#find the book details
					for each in ob.findAll("div",attrs={"class":"wrapper-fluid banners-effect-5"}):
						for i in re.finditer(r'<h4><a href="(https://nammabooks.com/.*?)">.*?<\/a><\/h4>',str(each)):
							ck=i.group(1)
							#print(ck)
							sto=requests.get(ck)
							sleep(1)
							#print(sto)
							rep=str(sto)
							#count=0
							if rep == "<Response [200]>" or "<Response [404]>":
								#print(count)
								stm=BeautifulSoup(sto.content,features="html.parser")
								sleep(1)
								for fm in stm.findAll("div",attrs={"class":"content-product-right col-md-7 col-sm-12 col-xs-12"}):
									cat.append(category[hi])
									title=fm.find("div",attrs={"class":"title-product"}).text
									tit=title.replace("\n","")
									try:
										autor=fm.find("span",attrs={"itemprop":"name"}).text
									except:
										autor=""
									publisher=fm.find("div",attrs={"class":"model"}).text
									pub=publisher[12:]
									stock=fm.find("div",attrs={"class":"stock"}).text
									sto=stock[9:]
									description=stm.find("div",attrs={"class":"tab-pane active"}).text
									des=description.replace("\n","")
									dest=des.replace("\t","")[20:]
									if tit:
										T.append(tit)
									else:
										T.append("Title Not Found")
									if autor:
										A.append(autor)
									else:
										A.append("Author Not Found")
									if pub:
										P.append(pub)
									else:
										P.append("Publisher Not Found")
									if sto:
										S.append(sto)
									else:
										S.append("Status Not Found")
									if dest:
										D.append(dest)
									else:
										D.append("It Has No Description")  

									#image writing on local	
									for img in stm.find_all("img"):
										ab=img.get("data-src")
										if ab:
											imgs.append(ab)
									try:
										try:
											os.makedirs(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}")
											ac=open(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}/{tit}.jpg","wb")
											st=requests.get(imgs[3])
											sleep(2)
											ac.write(st.content)
											sleep(1)
										except FileExistsError:
											ac=open(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}/{tit}.jpg","wb")
											st=requests.get(imgs[3])
											sleep(2)
											ac.write(st.content)
											sleep(1)
									except:
										pass
									imgs.clear()
							else:
								print("Pange Not Found")	       
				else:		
					print("Pange Not Found")
				if G!=0:
					print(category[hi],"page",G,"Completed")
			nukl.clear()
		#2
		if int(lem) > 9:
			for G in nukl: 
				amt=str(G)
				#print("page second",amt)
				clk=driver.find_element_by_link_text(amt)
				clk.click()
				sleep(1)
				urtl=driver.current_url
				rest=requests.get(urtl)
				sleep(1)
				check=str(rest)
				#getting each book details
				if check == "<Response [200]>" or "<Response [404]>":
					ob=BeautifulSoup(rest.content,features="html.parser")
					sleep(1)
					#find the book details
					for each in ob.findAll("div",attrs={"class":"wrapper-fluid banners-effect-5"}):
						for i in re.finditer(r'<h4><a href="(https://nammabooks.com/.*?)">.*?<\/a><\/h4>',str(each)):
							ck=i.group(1)
							#print(ck)
							sto=requests.get(ck)
							sleep(1)
							#print(sto)
							rep=str(sto)
							#count=0
							if rep == "<Response [200]>" or "<Response [404]>":
								#print(count)
								stm=BeautifulSoup(sto.content,features="html.parser")
								sleep(1)
								for fm in stm.findAll("div",attrs={"class":"content-product-right col-md-7 col-sm-12 col-xs-12"}):
									cat.append(category[hi])
									title=fm.find("div",attrs={"class":"title-product"}).text
									tit=title.replace("\n","")
									try:
										autor=fm.find("span",attrs={"itemprop":"name"}).text
									except:
										autor=""
									publisher=fm.find("div",attrs={"class":"model"}).text
									pub=publisher[12:]
									stock=fm.find("div",attrs={"class":"stock"}).text
									sto=stock[9:]
									description=stm.find("div",attrs={"class":"tab-pane active"}).text
									des=description.replace("\n","")
									dest=des.replace("\t","")[20:]
									if tit:
										T.append(tit)
									else:
										T.append("Title Not Found")
									if autor:
										A.append(autor)
									else:
										A.append("Author Not Found")
									if pub:
										P.append(pub)
									else:
										P.append("Publisher Not Found")
									if sto:
										S.append(sto)
									else:
										S.append("Status Not Found")
									if dest:
										D.append(dest)
									else:
										D.append("It Has No Description")  

									#image writing on local	
									for img in stm.find_all("img"):
										ab=img.get("data-src")
										if ab:
											imgs.append(ab)
									try:
										try:
											os.makedirs(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}")
											ac=open(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}/{tit}.jpg","wb")
											st=requests.get(imgs[3])
											sleep(2)
											ac.write(st.content)
											sleep(1)
										except FileExistsError:
											ac=open(f"/home/gopi/Pictures/ScrapImages/{category[hi]}/{pub}/{tit}.jpg","wb")
											st=requests.get(imgs[3])
											sleep(2)
											ac.write(st.content)
											sleep(1)
									except:
										pass
									imgs.clear()
							else:
								print("Pange Not Found")	       
				else:		
					print("Pange Not Found")
				if G!=0:
					print(category[hi],"page",G,"Completed")
			nukl.clear()

		#finding more pages of each category after rach page 9	
		ob=BeautifulSoup(rest.content,features="html.parser")
		sleep(1)
		for Gkp in ob.findAll("a"):
			nut=Gkp.text
			if nut.isnumeric():
				numl.append(nut)
		for lop in numl:
			if int(lop)>int(amt) :
				nukl.append(lop)
		numl.clear()
		if nukl:
			print(nukl)
			lem=nukl[0]
			continue
		else:
			print(category[hi],"Completed")		
			hi+=1
			break		
			
#frame the data and save as csv
ab=pandas.DataFrame({"Category":cat,"Title":T,"Author":A,"Publisher":P,"Stock Avilability":S,"Description":D})
ab.to_csv('nammabooks.csv',index=False,encoding="utf-8")
print("Scraping Completed ")
print("Check The nammabooks.csv File For Details")

                    