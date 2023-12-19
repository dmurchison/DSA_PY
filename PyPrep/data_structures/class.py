# Class
    # A class is a blueprint for creating objects. Objects have properties and methods(functions) associated with them.
    # Almost everything in Python is an object, with its properties and methods.


# This is an example of a simple class in Python,
    # What this is doing is creating a class called Animal, and then creating a constructor for the class.
    # The constructor is the __init__ function.
    # The constructor is called when the class is instantiated.
    # The constructor takes in two parameters, height and weight.
    # The constructor then sets the height and weight of the class to the parameters passed in.
    # The constructor also sets two private variables, _private_weight and __very_private_weight.
    # The constructor also sets a class variable called friends.
    # This class variable is shared by all instances of the class.
    # The constructor also sets a method called get_friends.
    # This method returns the class variable friends.
    # The constructor also sets a method called set_height.
    # This method takes in a parameter called height and sets the height of the class to the parameter passed in.
    # The constructor also sets a method called get_height. This method returns the height of the class.
    # The constructor also sets a method called get_private. This method prints out the __very_private_weight variable.
    # The constructor also sets a method called greet. This method prints out "This animal makes no sound".
    # This is a simple class in Python.

class Animal:
    friends = ['Clark', 'Frank', 'Jessica']

    def __init__(self, height=100, weight=100):
        self.height = height
        self.weight = weight
        self._private_weight = 50
        self.__very_private_weight = 1000

    def get_friends(self):
        return self.friends

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def get_private(self):
        print(self.__very_private_weight)

    def greet(self):
        print("This animal makes no sound")


# This is an example of a class that inherits from another class.
    # What this is doing is creating a class called Dog, and then creating a constructor for the class.
    # The constructor is the __init__ function. The constructor takes in three parameters, height, weight, and fur_color.
    # The constructor then sets the height and weight of the class to the parameters passed in.
    # The constructor also sets a private variable called fur_color.
    # The constructor also calls the constructor of the Animal class.
    # The constructor also sets a method called get_fur_color.
    # This method returns the fur_color of the class.
    # The constructor also sets a class method called greet.
    # This method prints out "Woof woof".
    # The constructor also sets a class variable called friends.
    # This class variable is shared by all instances of the class.

class Dog(Animal):
    def __init__(self, height, weight, fur_color):
        self.fur_color = fur_color
        super().__init__(height=height, weight=weight)

    def get_fur_color(self):
        return self.fur_color

    @classmethod
    def greet(cls):
        print("Woof woof")


sample_dog = Dog(50, 25, "Brown")
print(sample_dog.get_fur_color(), sample_dog.get_height())
sample_dog.greet()

Dog.greet()
print("A dog's starting friends are:", Dog.friends)

sample_dog.friends.append("Jerry")

print(sample_dog.get_friends())

