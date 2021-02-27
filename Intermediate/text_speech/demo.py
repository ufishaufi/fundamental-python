from gtts import gTTS
import os

text = open('demo_speech.txt', 'r').read()

language = 'id'
output = gTTS(text=text, lang=language, slow=False)
output.save('file.mp3')
os.system("afplay file.mp3")