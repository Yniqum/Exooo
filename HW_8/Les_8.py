# Task № 1 (lite)---------------------------------------------------------------
class Human():
    """human properties"""

    def __init__(self, name, age, city):
        """characteristic"""
        self.name = name
        self.age = age
        self.city = city

    def to_go(self):
        """a man can walk"""
        print('human ' + self.name.title() + ' at the age of ' + str(self.age) +
              ' from ' + self.city + ' I can walk'
              )

    def I_like(self):
        """a man can jump"""
        print('human ' + self.name.title() + ' at the age of ' + str(self.age) +
              ' from ' + self.city + 'I can jump'
              )


my_human = Human('Tor', 4, 'Cuba')

my_human.I_like()
my_human.to_go()


# Task № 2 (lite)----------------------------------------------------------
class Robot(Human):
    """robot model"""

    def __init__(self, model, age):
        super().__init__(self.age)
        self.model = model


my_robot = Robot('Toby ', 2)
print(my_robot.model)


# Task № 3 (lite)---------------------------------------------------------
class Car():
    color = red

    def door(self):
        print("four doors")

class truck(Car):
    color = blue
        print('two doors')
