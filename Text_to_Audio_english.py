#offline
#sudo apt install espeak ffmpeg libespeak1 #for linux
#pip3 install pyttsx3
#1

import pyttsx3 as p

#read the docx file of data 
intp=open("/home/gopi/Desktop/mocinterview.docx",'r')
red=intp.read()

#initialization
var=p.init()

# get details of speaking rate
var.setProperty("rate",110)

#get the volume level
var.setProperty("volume",2)

# set another voice
var.setProperty("voices", "voices[1].id")

# convert this text to speech 
var.say(red)

# saving speech audio into a file
var.save_to_file(red, "/home/gopi/Desktop/Audio.mp3")

#run
var.runAndWait()



