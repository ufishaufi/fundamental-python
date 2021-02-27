from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def textToSpeech():
    text = entry.get()
    language = 'id'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output_new.mp3')
    os.system("afplay output_new.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 250, window=button)

root.mainloop()