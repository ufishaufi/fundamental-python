# Adding data to file
"""
file = open("demo_speech.txt", 'w')
file.write('Saya sedang belajar python untuk materi handling file')
file.close()

# read file
file = open("demo_speech.txt", 'r')
content = file.read()
content = file.readline()
print(content)
file.close()

# Append data to file
file = open("demo_speech.txt", 'a')
file.write('\nSaya sedang belajar')
file.close()
"""

# exercise
f = open("demo.txt", 'w')
f.write('Halo')
f.close()

f = open("demo.txt", 'r')
print(f.read())
f.close()

f = open("demo.txt", 'a')
f.write('\nHalo juga')
f.close()
