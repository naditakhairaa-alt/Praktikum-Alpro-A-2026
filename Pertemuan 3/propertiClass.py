#ubah
class Alpro:
  def __init__(self, name, age):
    self.name = name
    self.age = age

al1 = Alpro("Justin", 19)

al1.age = 5
print(al1.age)

#hapus
class Alpro:
  def __init__(self, name, age):
    self.name = name
    self.age = age

al1 = Alpro("Justin", 19)

del al1.age

print(al1.name)
print(al1.age) #akan error

#akses
class Alpro:
  def __init__(self, name, age):
    self.name = name
    self.age = age

al1 = Alpro("Justin", 19)

print(al1.name)
print(al1.age)

#properti class vs properti objek
class Alpro:
  kelas = "TI-A" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Alpro("Justin")
p2 = Alpro("James")

print(p1.name)
print(p2.name)
print(p1.kelas)
print(p2.kelas)