# string formatting

numbers = [4, 5, 6]
newString = "numbers: {0}, {1}, {2}".format(numbers[0], numbers[1], numbers[2])
print(newString)

a = "{x}/{y}".format(x = 100, y = 200)
print(a)

newString = f"numbers{numbers[0]}, {numbers[1]}, {numbers[2]}"
print(newString)

x = 100
y = 200
a = f"{x}/{y}"
print(a)

# string function

print(':'.join(['Apel', 'Pisang', 'Mangga']))
newString = "Halo yang ada di sana"
print(newString.startswith("Helo"))
print(newString.endswith("di sana"))
print(newString.upper())
print(newString.lower())
print(newString.replace("yang ada di sana", "yang ada di sini"))

# String Manipulation
# String operator
s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)
print(s + t + u)
print('Go team' + '!!!')

s = 'foo.'
print(s * 4)
print(4 * s)
print('foo' * -8)

s = 'foo'
print(s in 'That\'s food for thought.')
print(s in 'That\'s good for now.')
print('z' not in 'abc')
print('z' not in 'xyz')

# Built -in String Function
print(ord('a'))
print(ord('#'))

print(ord('€'))
print(ord('∑'))

print(chr(97))
print(chr(35))
print(ord('€'))
print(ord('∑'))

s = 'I am a string.'
print(len(s))

print(str(49.2))
print(str(3 + 4j))
print(str(3 + 29))
print(str('foo'))

s = 'foobar'
print(s[0])
print(s[1])
print(s[3])
print(len(s))
print(s[len(s) - 1])

s = 'foobar'
print(s[-1])
print(s[-2])
print(len(s))
print(s[-len(s)])

# String Slicing
s = 'foobar'
print(s[2:5])
print(s[:4])
print(s[0:4])
print(s[2:])
print(s[2:len(s)])
print(s[:4] + s[4:])
print(s[:4] + s[4:] == s)

t = s[:]
print(id(s))
print(id(t))
print(s is t)
print(s[2:2])
print(s[4:2])

print(s[-5:-2])
print(s[1:4])
print(s[-5:-2] == s[1:4])

print(s[0:6:2])
print(s[1:6:2])

s = '12345' * 5
print(s)
print(s[::5])
print(s[4::5])
print(s[::-5])

s = 'If Comrade Napoleon says it, it must be right.'
print(s[::-1])

n = 20
m = 25
prod = n * m
print('The product of', n, 'and', m, 'is', prod)

var = 'Bark'
print(f'A dog says {var}!')
print(f"A dog says {var}!")
print(f'''A dog says {var}!''')

s = s[:3] + 'x' + s[4:]
print(s)

s = 'foobar'
s = s.replace('b', 'x')
print(s)

s = 'foO BaR BAZ quX'
print(s.capitalize())

s = 'foo123#BAR#.'
print(s.capitalize())

print('FOO Bar 123 baz qUX'.lower())
print('FOO Bar 123 baz qUX'.swapcase())

print('the sun also rises'.title())
print("what's happened to ted's IBM stock?".title())

print('FOO Bar 123 baz qUX'.upper())

print('foo goo moo'.count('oo'))
print('foo goo moo'.count('oo', 0, 8))

print('foobar'.endswith('bar'))
print('foobar'.endswith('baz'))
print('foobar'.endswith('oob', 0, 4))
print('foobar'.endswith('oob', 2, 4))

# bytes Objects
b = b'foo bar baz'
print(b)
print(type(b))