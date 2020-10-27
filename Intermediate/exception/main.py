# try except
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('Ada pembagian dengan nilai 0')

# try except finally
try:
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError:
    print('Ada pembagian dengan nilai 0')
finally:
    print('Program ini akan terus berjalan walau muncul error')

# file handling
file = open("demo.txt", 'w')
# perintah yang berhubungan dengan file
file.close()


# exercise
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Ada pembagian dengan nilai 0')
        return 0

x = float(input('Masukkan nilai = '))
y = float(input('Masukkan nilai yang ingin dibagi dengan angka = '))
result = divide(x, y)
print(result)
