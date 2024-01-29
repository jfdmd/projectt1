class Monster:  # Class Definition Here
    def __init__(self, name, given_age):  # Constructor gets called when we "instantiate" an object
        self.name = name
        self.age = given_age

    def speak(self):
        return "Generic Monster Voice"

    def __str__(self):  # to_string
        return f"My name is {self.name}, and I am {self.age}"  # __repr__


class Vampire(Monster):  # Inheritance
    def __init__(self, name, age, amt_blood):
        super().__init__(name, age)  # Calls Super constructor
        self.amt_blood = amt_blood

    def speak(self):  # Method overriding - will look for function definition in child class before
        return "I drink blood."


x = Monster("bob", 10)
y = Vampire("ed", 15, 40)

# monsters = [Monster("bob", 10), Vampire("ed", 10, 40)]
# for m in monsters:
#     print(m.speak())

print(x.name)
print(y.amt_blood)
print(x.speak())
print(y.speak())
print(x.__str__())