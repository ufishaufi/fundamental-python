def triangle_area(base, height):
    area = base * height / 2
    return area

base = 10
height = 6
print(f'Dengan fungsi, segitiga dengan alas = {base} dan tinggi = {height}, yang mana hasilnya = {triangle_area(base, height)}')
print(f'Menghitung luas segitiga dengan fungsi, yang mana hasilnya = {triangle_area(20, 2)}')
print(f'Menghitung luas segitiga dengan fungsi, yang mana hasilnya = {triangle_area(100, 2)}')

print()

def display_square():
    for x in range(1, 10):
        print(x * x)

display_square()

print()

# Passing arguments to function
def add(a,b):
    print(a + b)

add(10,20)

print()

# Making function return
def add(a,b):
    c = a + b
    return c

result = add(100,200)
print(result)

print()

# Passing function as argument
def add(a,b):
    return a + b

def square(c):
    return c * c

result = square(add(2, 3))
print(result)

print()

# exercise
def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi

weight = float(input('masukkan berat anda = '))
height = float(input('masukkan tinggi anda = '))
bmi = calculate_BMI(weight, height)
print(bmi)