class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def info(self):
        return f'ini adalah object dari persegi panjang dengan panjang = {self.length}cm,' \
               f' dan lebar = {self.width}cm'

    def rectangle_area(self):
        return self.length * self.width