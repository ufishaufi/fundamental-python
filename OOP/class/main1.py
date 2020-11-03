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

student1 = Student('','')
student1.get_data()
student1.put_data()