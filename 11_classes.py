### Classes ###

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def walk(self):
        print(f"{self.name} esta caminando")

my_person = Person("Michaell", "Antonio")
print(f"Mi nombre es {my_person.name} {my_person.surname}")
my_person.walk()