from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#to open the firefox browser

browser=webdriver.Firefox()

#To get web whatapp browser in chrome; Then scan with your QR code for login into webbrowser 

browser.get("https://web.whatsapp.com/")

sleep(3)

#after run the program scan the QR code in firefox browser

print("You need to scan the QR code For Open WhatsApp Web ")

#Attachment to be sent to particular user in whatsapp

whatapp_contact_name=input("Enter the contact name of the user  : ") #in your contact list
filepath=input("Enter file path  : ") #/home/gopi/Downloads/indhex.jpeg
msg = input('Enter your Message  : ')
count = int(input('Enter how many times you want to send this message  : '))

print("Check the whatsapp web")

#Search and go to the contact person message box

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(whatapp_contact_name))
user.click()

#To get location of attachment button

attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

#Attachs the given image in photos & videos 

image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

#Send the image or video to the contact person

send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')     
send_button.click()      

sleep(3)    

#send text messages

message_box=browser.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]')  

#this is loop for sending how many times a message to a contact person

for i in range(count+1):
	message_box.send_keys(msg + Keys.ENTER)
	
