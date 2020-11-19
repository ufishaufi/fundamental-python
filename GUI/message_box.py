from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Title","This is awesome")

response = tkinter.messagebox.askquestion("Question 1","Do you like coffe ?")
if response == 'yes':
    print("Here is a coffe for you")

root.mainloop()