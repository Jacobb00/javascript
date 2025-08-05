class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass
class dog(animal): ## animali inharitance etti 
    def speak(self):
        return f"{self.name} is barking"
class cat(animal):
    def speak(self):
        return f"{self.name} is meowing"
animal1=animal("animal")
dog1=dog("dog")
cat1=cat("cat")
print(animal1.speak())
print(dog1.speak())
print(cat1.speak())





