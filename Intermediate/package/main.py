# import Intermediate.package.geometri.segitiga as gs
from Intermediate.package.geometri.rectangle import rectangle_area, info as pj
from Intermediate.package.geometri.triangle import triangle_area, info as sg

print(sg())
print(f'hitung luas segitiga {triangle_area(10, 3)}')

print(pj())
print(f'hitung luas rectangle {rectangle_area(10, 1, 3)}')
