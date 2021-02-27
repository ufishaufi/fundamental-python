class Teddy:
    quantity = 200

    # instance attribute & constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_colour(self, color):
        print('This is a method')
        self.color = color

teddy1 = Teddy('Ted','Red')
print(teddy1.name, end=' ')
print(teddy1.color)

teddy2 = Teddy('Rob','Brown')
print(teddy2.name, end=' ')
print(teddy2.color)

teddy1.change_colour('Orange')
print(teddy1.name, end=' ')
print(teddy1.color)