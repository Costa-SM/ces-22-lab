class Person():
    def __init__(self, name, age, gender):
        self.age = age
        self.gender = gender
        print(name, "'s age is", age)
        print(name, "'s gender is", gender)

class Parent(Person):
    def __init__(self, parent_name, parent_age, parent_gender):
        super().__init__(parent_name, parent_age, parent_gender)
        self.parent_name = parent_name
        
        print(parent_name, " is a child's parent")

    def get_name(self):
        return self.parent_name

#class Child(Person, Parent):
#    def __init__(self, child_name, child_age, child_gender):
#        super().__init__(child_name, child_age, child_gender)
#        print(child_name, "'s parent is", )


Person('Jose', 15, 'M')
Parent('Abilio', 40, 'M')
