from gtts import gTTS
import os

text = "amah ayo mandi"
output = gTTS(text=text, lang='id', slow = False)
output.save('output.mp3')

os.system("afplay output.mp3")
