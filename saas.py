





















class Dog:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    def sound_method(self):
        return "woof woof"

dog1 = Dog("jek", 3,  "woof" )
dog2 = Dog("rex", 5, "woof")

print(dog1.name,dog1.age, dog1.sound_method())
print(dog2.name,dog2.age,dog2.sound_method())
