class Dog:
    def __init__(self, dogsname):
        self.dogsname = dogsname

    def display(self):
        print(f"{self.dogsname} Stats:")
        print(self.dogsname)
        if hasattr(self, "cutey"):
            print(self.cutey)
        if hasattr(self, "youth"):
            print(self.youth)
        if hasattr(self, "oldness"):
            print(self.oldness)
        if hasattr(self, "wisey"):
            print(self.wisey)

class Puppy(Dog):
    def __init__(self, youth, cutey, dogsname):
        super().__init__(dogsname)
        self.youth = youth
        self.cutey = cutey

class Muzzle(Dog):
    def __init__(self, oldness, wisey, dogsname):
        super().__init__(dogsname)
        self.oldness = oldness
        self.wisey = wisey

Dodge = Dog("Dodgecoin")
print("\n")  
Dodge.display()

Snoopy = Puppy("very young", "very cute", "Snoopy")
print("\n")
Snoopy.display()

Grufel = Muzzle("very old", "very wise", "Grufel")
print("\n")
Grufel.display()

