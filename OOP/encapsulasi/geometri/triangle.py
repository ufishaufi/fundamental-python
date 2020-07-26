class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def info(self):
        return f'ini adalah object dari segitiga dengan alas = {self.base}cm, dan tinggi = {self.height}cm'

    def triangle_area(self):
        return self.base * self.height / 2