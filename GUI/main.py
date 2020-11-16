from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Style().configure('red/white.TButton', foreground='red', background='white')
ttk.Style().configure('blue/white.TButton', foreground='blue', background='white')

# Label
label1 = Label(root, text="Hello World")

label1.pack()

# Frames
newFrame = Frame(root)
newFrame.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = ttk.Button(newFrame, text="Click Here", style='red/white.TButton')
button2 = ttk.Button(otherframe, text="Click Here", style='blue/white.TButton')

button1.pack()
button2.pack()

root.mainloop()
