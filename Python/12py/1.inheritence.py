# Base class: Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def description(self):
        return f"Name: {self.name}, Age: {self.age}"

# Derived class: Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Mammal sound: Some generic mammal sound!"

    def description(self):
        return super().description() + f", Fur Color: {self.fur_color}"

# Derived class: Bird
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Bird sound: Chirp chirp!"

    def description(self):
        return super().description() + f", Wingspan: {self.wingspan} cm"

# Derived class: Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Reptile sound: Hiss!"

    def description(self):
        return super().description() + f", Scale Color: {self.scale_color}"

# Main function to demonstrate inheritance
def main():
    # Create some animal objects
    animal1 = Animal("Generic Animal", 5)
    mammal1 = Mammal("Dog", 3, "Brown")
    bird1 = Bird("Sparrow", 1, 15)
    reptile1 = Reptile("Snake", 2, "Green")

    # Print descriptions and sounds of each animal
    print(animal1.description())
    print(animal1.make_sound())

    print(mammal1.description())
    print(mammal1.make_sound())

    print(bird1.description())
    print(bird1.make_sound())

    print(reptile1.description())
    print(reptile1.make_sound())

if __name__ == "__main__":
    main()
