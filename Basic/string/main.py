# string formatting

numbers = [4, 5, 6]
newString = "numbers: {0}, {1}, {2}".format(numbers[0], numbers[1], numbers[2])
print(newString)

newString = f"numbers{numbers[0]}, {numbers[1]}, {numbers[2]}"
print(newString)

x = 100
y = 200
a = f"{x}/{y}"
print(a)

# string function

print(':'.join(['Apel', 'Pisang', 'Mangga']))
newString = "Hello yang ada di sana"
print(newString.endswith("di sana"))
print(newString.upper())
print(newString.lower())
print(newString.replace("yang ada di sana", "yang ada di sini"))