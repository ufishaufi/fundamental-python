from OOP.encapsulasi.geometri.rectangle import Rectangle
from OOP.encapsulasi.geometri.triangle import Triangle

p1 = Rectangle(10, 3)
s1 = Triangle(4, 2)

print(p1.info(), end='')
print(f' dengan luasnya adalah = {p1.rectangle_area()}cm\u00b2')

print(s1.info(), end='')
print(f' dengan luasanya adalah = {s1.triangle_area()}cm\u00b2')