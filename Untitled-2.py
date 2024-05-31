class Dog:
    # Class-level attributes
    sound = "bark"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound_method(self):
        return "woof woof"
dog1 = Dog(name="Buddy", age=3)
dog2 = Dog(name="Max", age=5)

print(f"Dog 1: Name = {dog1.name}, Age = {dog1.age}, Sound = {dog1.sound}, Custom Sound = {dog1.sound_method()}")
print(f"Dog 2: Name = {dog2.name}, Age = {dog2.age}, Sound = {dog2.sound}, Custom Sound = {dog2.sound_method()}")
