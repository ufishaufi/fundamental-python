def triangle_area(base, height):
    area = base * height / 2
    return area

base = 10
height = 6
print(f'Dengan fungsi, segitiga dengan alas = {base} dan tinggi = {height}, yang mana hasilnya = {triangle_area(base, height)}')
print(f'Menghitung luas segitiga dengan fungsi, yang mana hasilnya = {triangle_area(20, 2)}')
print(f'Menghitung luas segitiga dengan fungsi, yang mana hasilnya = {triangle_area(100, 2)}')

def display_square():
    for x in range(1, 10):
        print(x * x)

display_square()