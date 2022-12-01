class Person:
    def __init__(self, name, age): # конструктор
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + str(self.name) + ", age: " + str(self.age)

    def __repr__(self):
        return "name: " + str(self.name) + ", age: " + str(self.age)

    def getting_older(self, years):
        self.age += years


class Student(Person):
    def __init__(self, name, age, group): # конструктор
        super().__init__(name, age)
        self.group = group

    def __str__(self):
        return super().__str__() + ", group: " + self.group
    

    '''
    def __repr__(self):
        return "name: " + str(self.name) + ", age: " + str(self.age)

    def getting_older(self, years):
        self.age += years
    
    def __add__(self, other):
        new_name = self.name[::2] + other.name[1::2]
        new_age = (self.age + other.age) // 2
        return Student(new_name, new_age)
    '''


if __name__ == "__main__":
    danila = Person("Danila", 17)
    kirill = Student("Kirill", 19, 'ШАД-112')
    print(danila, kirill, sep='\n')
