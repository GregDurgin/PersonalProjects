
inputs = input('Student First Name?:')+input('Student Last Name?:')

class Students:
    all = []

    #universal variables
    def __init__(self, name: str, age: int, classes: list):

        assert age >= 0, f'Age {age} is not greater than 0'

        #characteristics \/
        self.name = name
        self.age = age
        self.classes = classes

        #executes

        Students.all.append(self) #adds

    def __repr__(self):
        return f"Name: {self.name}"
        return f"Age: {self.age}"
        return f"Classes: {self.classes}"



MikeShepard = Students('Mike Shepard', 19, ['history', 'math', 'langauge'])
JohnKrasinski = Students('John Krasinski', 20, ['history', 'german', 'math'])
#add infinite amount of students (working on making this functional by allowing the creation of new students using user input

# is there a way to do this without having to type out each students name?
if inputs == 'MikeShepard':
    inputs = MikeShepard
elif inputs == 'JohnKrasinski':
    inputs = JohnKrasinski
else:
    print('Student not found :(')

if inputs in Students.all:
    print(f'Name {inputs.name}')
    print(f'Age {inputs.age}')
    print(f"Courses {inputs.classes}")
pass