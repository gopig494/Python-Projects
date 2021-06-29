#scrap  :http://www.viruba.com/categories.aspx


from selenium import webdriver as web
from bs4 import BeautifulSoup as beauti
import requests as req
import re 
from time import sleep
import os
import pandas 

opts=web.FirefoxOptions()
opts.headless = True
driver = web.Firefox(options=opts)
driver.get("http://www.viruba.com/categories.aspx")
sleep(2)
url=driver.current_url
con=req.get(url)
var=beauti(con.content,features="html.parser")

a=[]  #separation
az=[]  #புத்தக தலைப்புகள்
ag=[]  #பதிப்பு ஆண்டு
bg=[]  #பதிப்பு
cg=[]   #ஆசிரியர்
dg=[]   #பதிப்பகம்
eg=[]   #புத்தகப் பிரிவு
fg=[]   #பக்கங்கள்

count=0

for cat in var.findAll("div",attrs={"class":"main"}):
	for fin in cat.findAll("a"):
		#category link finder
		for de in re.finditer(r'<a href="(ctotalbooks.*)"><span>.*<\/span><\/a>',str(fin)):
			#category=fin.text
			asd=("http://www.viruba.com/"+de.group(1))
			surl=req.get(asd)
			sleep(1)
			scon=beauti(surl.content,features="html.parser")
			sleep(1)
			abc=""
			for h in scon.findAll("img"):
				war=h.get("title")
				if war:
					for i in war:
						if i!=" ":
							abc+=i
				if abc!="":
					az.append(abc)
				abc=""
					
	        #find the book details one by one
			for af in scon.findAll("div",attrs={"id":"MainContent_UpdatePanel1"}):
				for kk in af.findAll("table",attrs={"frame":"border"}):
					for jj in kk.findAll("span",attrs={"class":"label001"}):
						#tempory list appending
						a.append(jj.text.replace("\n",""))
                    #append the values
					ag.append(a[1])
					bg.append(a[3])
					cg.append(a[5])
					kd=""
					for mk in a[7]:
						if mk!=" ":
							kd+=mk
					dg.append(kd)
					ad=""
					for lb in a[11]:
						if lb!=" ":
							ad+=lb
					eg.append(ad)
					fg.append(a[13])
					#print(ag)
					#print(bg)
					a.clear()
					
			#file handling and image saving
			for g in scon.findAll('img'):
				img=g.get("src")
				aurl=("http://www.viruba.com/"+img)
				#print(aurl)
				if aurl != "http://www.viruba.com/Img_Admin/banner.jpg":
					try:
						os.makedirs(f"/home/gopi/Pictures/Scrapimages/{eg[count]}/{dg[count]}")
						ac=open(f"/home/gopi/Pictures/Scrapimages/{eg[count]}/{dg[count]}/{az[count]}.jpg","wb")
						st=req.get(aurl)
						sleep(2)
						ac.write(st.content)
						sleep(1)
					except FileExistsError:
						try:
							st=req.get(aurl)
							sleep(2)
							aml=st.content
							plo=open(f"/home/gopi/Pictures/Scrapimages/{eg[count]}/{dg[count]}/{az[count-1]}.jpg","rb")
							ytl=plo.read()
							if aml==ytl:
								ac=open(f"/home/gopi/Pictures/Scrapimages/{eg[count]}/{dg[count]}/{az[count]}1.jpg","wb")
								st=req.get(aurl)
								sleep(2)
								ac.write(st.content)
								sleep(1)
						except:
							pass
							
						ac=open(f"/home/gopi/Pictures/Scrapimages/{eg[count]}/{dg[count]}/{az[count]}.jpg","wb")
						st=req.get(aurl)
						sleep(2)
						ac.write(st.content)
						sleep(1)
					count+=1						
		print("புத்தகப் பிரிவு :",eg[count-1],"Completed")	
#save the data's
succ=pandas.DataFrame({"புத்தகப் பிரிவு":eg,"புத்தக தலைப்புகள்":az,"ஆசிரியர்":cg,"பதிப்பகம்":dg,"பதிப்பு ஆண்டு":ag,"பதிப்பு":bg,"பக்கங்கள்":fg})
succ.to_csv("viruba.csv" ,index=False, encoding="utf-8")