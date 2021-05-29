intt=input("Enter What Do You Need To Search in Google  :")
from selenium import webdriver
#print(dir(webdriver))
browser=webdriver.Firefox()
#print(dir(webdriver.Firefox()))
browser.get('https://google.com')
from selenium.webdriver.common.keys import Keys
fi=browser.find_element_by_name("q")
fi.clear()
fi.send_keys(intt)
fi.send_keys(Keys.RETURN)
