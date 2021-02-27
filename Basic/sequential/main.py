# Konstruksi dasar python
# Sequential = Eksekusi berurutan
print('Hello World! ', end ='')
print('by Shaufi')
print('Tanggal 25 Juli 2020')
print('-' * 20)

# numeric function

print(min(1, 2, 3, 4, 5))
print(abs(-203))

print()

# integer
print(1 + 1)
print(10)

print()

print(0o10)
print(0x10)
print(0b10)

print()

print(type(10))
print(type(0o10))
print(type(0x10))

print()

print(10)
print(0x10)
print(0b10)

# floating
print(4.2)
print(type(4.2))
print(4.)
print(.2)

print()

print(.4e7)
print(type(.4e7))
print(4.2e-4)

print()

print(1.79e308)
print(1.8e308)

print()

print(5e-324)
print(1e-325)

print()

# Complex Number
print(2 + 3j)
print(type(2 + 3j))

print()

print("I am string")
print(type("I am string"))

print()

print("This string contains a single quote (') character.")
print('This string contains a single quote (") character.')

print()

print("This string contains a single quote (\') character.")
print('This string contains a single quote (\") character.')

print('a\
b\
c')

print('foo\\bar')
print('foo\tbar')

print()

print("a\tb")
print("a\141\x61")
print("a\nb")
print('\u2192 \N{rightwards arrow}')

print()

print('foo\nbar')
print(r'foo\nbar')
print('foo\\bar')
print(R'foo\\bar')

print('''This string has a single (') and a double(") quote.''')
print("""This is a
string that spans
across several lines""")

print()

# boolean
print(type(True))
print(type(False))

print()

# variable assignment
n = 300
print(n)

a = b = c = 300
print(a, b, c)

print()

# variable types
var = 23.5
print(var)

var = "Now I'am a string"
print(var)

# object reference
n = 300
print(n)
print(type(n))
m = n
m = 400
n = "foo"
print(n)

n = 300
m = n
print(id(n))
print(id(m))

m = 400
print(id(m))

m = 300
n = 300
print(id(m))
print(id(n))

# variable name
name = "Bob"
age = 54
has_W2 = True
print(name, age, has_W2)

# Arithmetics operator
a = 4
b = 3
print(+a)
print(-b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

print(10 / 5)
print(type(10 / 5))

print(10 / 4)
print(10 // 4)
print(10 // -4)
print(-10 // 4)
print(-10 // -4)

x = 4
y = 6
print(x)
print(y)
z = x * 25 + y
print(z)

# Comparison Operator
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)

x = 1.1 + 2.2
print(x == 3.3)

tolerence = 0.00001
x = 1.1 + 2.2
print(abs(x-3.3) < tolerence)

x = 5
print(x <= 10)

print(type(x < 10))

t = x > 10
print(t)
print(type(t))

print(callable(x))
print(type(callable(x)))

t = callable(len)
print(t)
print(type(t))

x = 5
print(not x < 10)
print(not callable(x))

x = 5
print(x < 10 or callable(x))
print(x < 0 or callable(x))

print(bool(0), bool(0.0), bool(0.0 + 0j))
print(bool(-3), bool(3.14159), bool(1.0 + 1j))

print(bool(''), bool(""), bool(""""""))
print(bool('foo'), bool(" "), bool(''''''))

print(type([]))
print(bool([]))

print(type([1, 2, 3]))
print(bool([1, 2, 3]))

print(bool(None))

x = 3
print(bool(x))
print(not x)

x = 0.0
print(bool(x))
print(not x)

x = 3
y = 4
print(x or y)

x = 0.0       
y = 4.4
print(x or y)

x = 3
y = 4
print(x and y)

x = 0.0
y = 4.4
print(x and y)

a = 0
b = 1
print(a != 0 and (b / a) > 0)

string = 'foo bar'
s = string or '<default_value>'
print(s)

string = ''
s = string or '<default_value>'
print(s)

# Bitwise Operator
print('0b{:04b}'.format(0b1100 & 0b1010))
print('0b{:04b}'.format(0b1100 | 0b1010))
print('0b{:04b}'.format(0b1100 ^ 0b1010))
print('0b{:04b}'.format(0b1100 >> 2))
print('0b{:04b}'.format(0b0011 << 2))

# Identity Operator
x = 1001
y = 1000 + 1
print(x, y)
print(x == y)
print(x is y)

print(id(x))
print(id(y))

x = 10
y = 20
print(x is not y)

# Operator Precedence
print(20 + 4 * 10)

print(2 * 3 ** 4 * 5)

print(20 + 4 * 10)
print((20 + 4) * 10)

print(2 * 3 ** 4 * 5)
print(2 * 3 ** (4 * 5))

# Augmented Assignment Operators
a = 10
b = 20
c = a * 5 + b
print(c)

a = 10
a = a + 5
print(a)

b = 20
b = b * 3
print(b)
