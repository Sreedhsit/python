class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

  def myage(self):
      print('MyAge is',self.age)





p1 = Person("John", 36)
p1.myfunc()
p1.myage()
p2=p1
p2=Person('Sreekanth Reddy Kamtam',37)
print(type(p1),id(p1))
print(type(p2),id(p2))
p2.myfunc()
p2.myage()

def my_function(x):
    return x +10

print(my_function(10))
