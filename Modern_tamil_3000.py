import re
from time import sleep 
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
import os 
import requests

opts=webdriver.FirefoxOptions()
opts.headless=True
driver=webdriver.Firefox(options=opts)
driver.get("https://app.memrise.com/course/796956/modern-tamil-in-3000-words/1/?action=prev")
sleep(1)
url=driver.current_url
resp=requests.get(url)
sleep(1)
content=BeautifulSoup(resp.content,features='html.parser')

tamil=[]
english=[]

for l in content.findAll("div",attrs={"class":"col_a col text"}):
	#print(l.text)
	tamil.append(l.text)
	
for l in content.findAll("div",attrs={"class":"col_b col text"}):
	#print(l.text)
	english.append(l.text)
	
	
i=2	
while i<=143:	
	st=driver.find_element_by_link_text(f"Level {i}")
	st.click()
	url=driver.current_url
	resp=requests.get(url)
	content=BeautifulSoup(resp.content,features='html.parser')
	for l in content.findAll("div",attrs={"class":"col_a col text"}):
		#print(l.text)
		tamil.append(l.text)
	
	for l in content.findAll("div",attrs={"class":"col_b col text"}):
		#print(l.text)
		english.append(l.text)
	print(f"page {i} Completed") 
	i+=1
	

ab=pandas.DataFrame({"Tamil Word":tamil,"English Word":english})
ab.to_csv('tamil_english.csv',index=False,encoding="utf-8")
print("Scraping Completed ")