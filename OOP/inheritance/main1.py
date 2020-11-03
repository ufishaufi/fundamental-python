class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input('Enter name: ')
        self.age = input('Enter age: ')

    def put_data(self):
        print(f'hello my name is {self.name}')
        print(f'my age is {self.age}')

# iheritance
class ScienceStudent(Student):
    def science(self):
        print('This is a science method')

a = ScienceStudent('','')
a.get_data()
a.put_data()