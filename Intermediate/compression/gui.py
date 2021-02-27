import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file to compress")
    return filename

def compression(i, o):
    compress(i, o)


windows =tk.Tk()
windows.title("Compression engine")
windows.geometry("600x400")

# input_entry = tk.Entry(windows)
# output_entry = tk.Entry(windows)

input_label = tk.Label(windows, text="File to be compressed")
output_label = tk.Label(windows, text="Name of the compressed file")

compress_button = tk.Button(windows, text="Compress", command=lambda:compression(open_file(), "compressedoutput1.txt"))


# input_label.grid(row=0, column=0)
# input_entry.grid(row=0, column=1)
# output_label.grid(row=1, column=0)
# output_entry.grid(row=1, column=1)
compress_button.grid(row=3, column=1)

windows.mainloop()