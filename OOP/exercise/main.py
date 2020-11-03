class Number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a = Number(3)
number_b = Number(4)
print(number_a * number_b)


class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter RAM size: ')
        self.memory = input('Enter memory size: ')
        self.processor = input('Enter processor: ')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(f'RAM size is: {self.ram}')
        print(f'Memory size is: {self.memory}')
        print(f'Processor is: {self.processor}')

class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color: ')

    def put_case_details(self):
        print(f'case color is: {self.casecolor}')

class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight: ')

    def displayweight(self):
        print(f'weight is: {self.weight}')

comp = Laptop('')
comp.getspecs()
comp.getweight()
comp.displayspecs()
comp.displayweight()

