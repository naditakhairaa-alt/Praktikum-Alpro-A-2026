#tanpa init
class Alpro:
  pass

p1 = Alpro()
p1.name = "Justin"
p1.age = 19

print(p1.name)
print(p1.age)

#dengan init
class Alpro:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Alpro("Justin", 19)

print(p1.name)
print(p1.age)