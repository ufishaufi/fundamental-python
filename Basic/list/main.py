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