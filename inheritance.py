class Animal:
    def __init__(self, name, age, no_of_legs):
        self.name = name
        self.age = age
        self.no_of_legs = no_of_legs

    def sleep(self):
        print("Animal ", self.name, "sleeps")

    def walk(self):
        print("Animal", self.name, "walks")
    

class Dog(Animal):
    def __init__(self, name, age, no_of_legs):
        super().__init__(name, age, no_of_legs)
        self.teeth = 'canine'
        self.tail = True
    
    def bark(self):
        print("Dog barks ", self.name)


if __name__ == '__main__':
    # animal = Animal("dog", 15, 4)
    # animal.walk()

    dog = Dog("bruno", 14, 4)
    print(dog.teeth)
    print(dog.name)
    dog.walk()
    dog.bark()