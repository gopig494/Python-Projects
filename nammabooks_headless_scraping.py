#scrap the web of https://nammabooks.com/index.php?route=product/category&path=85&page=1

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

T=[]
A=[]
P=[]
S=[]
D=[]

for G in range(1,10):
    if G == 1:
        res=r.get("https://nammabooks.com/index.php?route=product/category&path=85")
        sleep(1)
        check=str(res)
    else:
        res=r.get(f"https://nammabooks.com/index.php?route=product/category&amp;path=85&amp;page={G}")
        sleep(1)
        check=str(res)
    if check == "<Response [200]>" or "<Response [404]>":
        ob=B(res.content,features="html.parser")
        sleep(1)
        for each in ob.findAll("div",attrs={"class":"wrapper-fluid banners-effect-5"}):
            for i in re.finditer(r'<h4><a href="(https://nammabooks.com/.*?)">.*?<\/a><\/h4>',str(each)):
                ck=i.group(1)
                #print(ck)
                sto=r.get(ck)
                sleep(1)
                #print(sto)
                rep=str(sto)
                #count=0
                if rep == "<Response [200]>" or "<Response [404]>":
                    #print(count)
                    stm=B(sto.content,features="html.parser")
                    sleep(1)
                    for fm in stm.findAll("div",attrs={"class":"content-product-right col-md-7 col-sm-12 col-xs-12"}):
                        title=fm.find("div",attrs={"class":"title-product"}).text
                        tit=title.replace("\n","")
                        autor=fm.find("span",attrs={"itemprop":"name"}).text
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
                            print("Title Not Found")
                        if autor:
                            A.append(autor)
                        else:
                            print("Author Not Found")
                        if pub:
                            P.append(pub)
                        else:
                            print("Publisher Not Found")
                        if sto:
                            S.append(sto)
                        else:
                            S.append("Status Not Found")
                        if dest:
                            D.append(dest)
                        else:
                            D.append("It Has No Description")
                else:
                    print(ck,"Is Not Found")     
            print("Page",G,"Completed")
    else:
        print("Error Page Not Found")
        
ab=p.DataFrame({"Title":T,"Author":A,"Publisher":P,"Stock Avilability":S,"Description":D})
ab.to_csv('tamil.csv',index=False,encoding="utf-8")
print("Scraping Completed ")
print("Check The tamil.csv File For Details")

                    



















