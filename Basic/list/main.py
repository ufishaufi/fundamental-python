# tipe data skalar => tipe data sederhana
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ["Eko", "Dwi", "Tri", "Catur"]
anak.append("Limo")
print(anak)

# sapa anak ke-2
print(f'\nanak ketiganya namanya {anak[2]}')

for a in anak:
    print(f'Hai, {a}!')

print("\ncara ribet")
for a in range(0, len(anak)):
    print(f'Hai {anak[a]}!')

food = ['telur', 'pizza', 'cupcake', 'burger', 'salmon']
print(food[2])
food.append('kue')
print(food)
food.insert(3, 'tacos')
print(food)

# List Slicing
numbers = [0, 100, 200, 300, 400, 500, 600]
print(numbers[1:6:3])

# List Comprehension
list_new = [x**2 for x in range(10) if x**2 % 2 == 0 ]
print(list_new)

# exercise
new_list = list(range(1, 100))

for x in new_list:
    if x % 2 == 0:
        print(x, end=' ')