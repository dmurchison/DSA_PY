# Class definition
class Animal:
    fur_color = "Gray"
    friends = ['Wolf', 'Giraffe', 'Dog']

    def __init__(self, type="Turtle", height=100, weight=100):
        self.type = type
        self.height = height
        self.weight = weight
        self._private_weight = 50
        self.__very_private_weight = 1000

    def print_height(self):
        print(f"This {self.get_type()}'s height is {self.height} feet")

    def get_type(self):
        return self.type

    def get_fur_color(self):
        return self.fur_color
    
    def get_friends(self):
        return self.friends

    def set_height(self, height):
        self.height = height

    def get_private(self):
        print(self.__very_private_weight)


animal_1 = Animal("Elephant", height=120, weight=80)
animal_2 = Animal(height=70, weight=150)
animal_3 = Animal()


animal_1.print_height()
animal_1.set_height(500)
animal_1.print_height()

print(animal_3.__very_private_weight)
print(animal_2.get_type())
print(animal_3.type)
animal_3.friends.append("Jerry")
print(animal_3.get_friends())

print(animal_3._private_weight)


