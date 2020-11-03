from OOP.inheritance.geometri.geometry import Geometry
from OOP.inheritance.geometri.rectangle import Rectangle
from OOP.inheritance.geometri.triangle import Triangle

b1 = Geometry()
p1 = Rectangle(10, 3)
s1 = Triangle(4, 2)

list_geometry = []
list_geometry.append(p1)
list_geometry.append(s1)

print('\npolymorphism')
for geometry in list_geometry:
    print(geometry.info())
