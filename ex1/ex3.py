class Person:
    def __init__(self,name,age,gender):
        self.a = name
        self.b = age
        self.c = gender
    def display(self,friend_name):

        print(f"hey im {self.b} and happy")
        return f"my friend is {friend_name}"
obj1=Person("ahtvin",20,"female")
print(obj1.a)
print(obj1.b)
print(obj1.c)
obj2=obj1.display("jumbo")
print(obj2)

          