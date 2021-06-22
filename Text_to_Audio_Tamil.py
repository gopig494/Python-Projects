#online
#linux
#pip3 install gTTS pyttsx3 playsound

# all available languages along with their IETF tag
#print(gtts.lang.tts_langs())

import gtts
from playsound import playsound

#1
#read the docx file of data 
intp=open("/home/gopi/Desktop/mahatma_gandhi.docx",'r')
red=intp.read()

# make request to google to get synthesis
tts = gtts.gTTS(red)

# save the audio file
tts.save("mahatma_gandhi.mp3")

# play the audio file
playsound("mahatma_gandhi.mp3")
