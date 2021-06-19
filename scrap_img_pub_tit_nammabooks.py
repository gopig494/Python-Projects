#scrap the web of https://nammabooks.com/index.php?route=product/category&path=85&page=1
import os
import requests as r
from selenium import webdriver as w
from bs4 import BeautifulSoup as B
import pandas as p
import re
from time import sleep

opts=w.FirefoxOptions()
opts.headless = True
driver = w.Firefox(options=opts)
#opts.set_headless(headless=True)
#driver=w.Firefox(options=obj)
driver.get("https://nammabooks.com/index.php?route=product/category&path=85")
for G in range(1,10):
    print("Please Wait For Getting Images From Web")
    if G == 1:
        res=r.get("https://nammabooks.com/index.php?route=product/category&path=85")
        sleep(1)
        check=str(res)
    else:
        res=r.get(f"https://nammabooks.com/index.php?route=product/category&path=85&page={G}")
        sleep(1)
        check=str(res)
    if check == "<Response [200]>" or "<Response [404]>":
        ob=B(res.content,features="html.parser")
        sleep(1)
        for each in ob.findAll("div",attrs={"class":"wrapper-fluid banners-effect-5"}):
            for i in re.finditer(r'<h4><a href="(https://nammabooks.com/.*?)">.*?<\/a><\/h4>',str(each)):
                ck=i.group(1)
                sto=r.get(ck)
                sleep(1)
                rep=str(sto)
                if rep == "<Response [200]>" or "<Response [404]>":
                    stm=B(sto.content,features="html.parser")
                    sleep(1)
                    for fm in stm.findAll("div",attrs={"class":"content-product-right col-md-7 col-sm-12 col-xs-12"}):
                        title=fm.find("div",attrs={"class":"title-product"}).text
                        tit=title.replace("\n","")
                        publisher=fm.find("div",attrs={"class":"model"}).text
                        pub=publisher[12:]
                        for img in stm.find_all("img"):
                            ab=img.get("data-src")
                            if ab:
                                try:
                                    os.makedirs(f"/home/gopi/Pictures/ScrapImages/{pub}")
                                    ac=open(f"/home/gopi/Pictures/ScrapImages/{pub}/{tit}.jpg","wb")
                                    st=r.get(ab)
                                    sleep(2)
                                    ac.write(st.content)
                                    sleep(1)
                                except FileExistsError:
                                    ac=open(f"/home/gopi/Pictures/ScrapImages/{pub}/{tit}.jpg","wb")
                                    st=r.get(ab)
                                    sleep(2)
                                    ac.write(st.content)
                                    sleep(1)
                else:
                    print(ck,"Is Not Found")     
            print("Page",G,"Completed")
    else:
        print("Error Page Not Found")    
print("Scraping Completed ")
