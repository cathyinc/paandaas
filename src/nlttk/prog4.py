def display4():
    code = '''class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        print(f"{child.name} is the child of {self.name}")

    def display_children(self):
        if self.children:
            print(f"{self.name}'s Children:")
            for child in self.children:
                print(child.name)
        else:
            print(f"{self.name} has no children.")


father = Person("John", 40, "Male")
mother = Person("Jane", 38, "Female")
son = Person("Alex", 12, "Male")
daughter = Person("Emma", 8, "Female")

father.add_child(son)
mother.add_child(daughter)

mother.add_child(son)
mother.add_child(daughter)

father.display_children()
mother.display_children()'''
    print(code)
