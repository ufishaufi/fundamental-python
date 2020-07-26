from OOP.inheritance.geometri.rectangle import Rectangle
from OOP.inheritance.geometri.triangle import Triangle
from OOP.inheritance.geometri.geometry import Geometry

g1 = Geometry()
p1 = Rectangle(10, 3)
s1 = Triangle(4, 2)

print(p1.info(), end='')
print(f' dengan luasnya adalah = {p1.rectangle_area()}cm\u00b2')

print(s1.info(), end='')
print(f' dengan luasanya adalah = {s1.triangle_area()}cm\u00b2')

print('\nMencoba membuat object dari kelas Bangun Ruang')
print(g1.info())
print(g1.calculate_area())

