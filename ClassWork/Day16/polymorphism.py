#!/usr/bin/python

class Animal:
    def __init__():
        print("Animal Constructor is invoked")

    def name(self):
        pass

    def make_noise(self):
        pass

    def __del__(self):
        print("Animal Destructor is invoked")


class Cat(Animal):
    def __init__(self):
        print("Cat Constructor is invoked")

    def name(self):
        print("My name is cat")

    def make_noise(self):
        print("Mewoooo...")

    def __del__(self):
        print("Cat Destructor is invoked")

class Dog(Animal):
    def __init__(self):
        print("Dog Constructor is invoked")

    def name(self):
        print("My name is dog")

    def make_noise(self):
        print("Barking...")

    def __del__(self):
        print("Dog Destructor is invoked")


class Lion(Animal):
    def __init__(self):
        print("Lion Constructor is invoked")

    def name(self):
        print("My name is lion")

    def make_noise(self):
        print("Roar...")

    def __del__(self):
        print("Lion Destructor is invoked")

class TestAnimal:
    def __init__(self):
        print("TestAnimal Constructor is invoked..")

    def print_name(self, animal):
        animal.name()

    def print_make_noise(self, animal):
        animal.make_noise()

    def __del__(self):
        print("TestAnimal Destructor is invoked")


if __name__=='__main__':
    dog = Dog()
    cat = Cat()
    lion = Lion()
    test_animal = TestAnimal()

    test_animal.print_name(dog)
    test_animal.print_make_noise(dog)

    test_animal.print_name(cat)
    test_animal.print_make_noise(cat)

    test_animal.print_name(lion)
    test_animal.print_make_noise(lion)
