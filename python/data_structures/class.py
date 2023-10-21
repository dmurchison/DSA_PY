# Class

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

