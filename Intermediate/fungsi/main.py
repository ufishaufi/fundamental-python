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

# weight = float(input('masukkan berat anda = '))
# height = float(input('masukkan tinggi anda = '))
# bmi = calculate_BMI(weight, height)
# print(bmi)

# functional programming
def add_ten(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 10))

# lambdas
def square(x):
    return x**2

print(square(4))
print((lambda x: x**2)(30))

# map
def add(x):
    return x + 2

newlist = [10, 20, 30, 40, 50]

result = list(map(add, newlist))
print(result)

result = list(map(lambda x: x + 2, newlist))
print(result)

# filter
newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13]

result =list(filter(lambda x: x % 2 == 0, newlist))
print(result)

# generator
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

def even_numbers(x):

    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(even_numbers(21)))

# exercise
def student_discount(price):
    price = price - (price * 10) / 100
    return  price

def additional_discount(price):
    price = price - (price * 5) / 100
    return price

selling_price = 100

print(additional_discount(student_discount(selling_price)))

result = (lambda x: x*(x + 5)**2)(5)
print(result)

def discount(price):
    price = (int) (price - (price * 10) / 100)
    return price

product_price = [100, 200, 300, 400, 500]
updated_price = map(discount, product_price)
print(list(updated_price))