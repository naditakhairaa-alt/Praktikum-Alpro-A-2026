class Alpro:
  def __init__(self, name):
    self.name = name

  def salam(self):
    print("Hai, nama saya " + self.name)

p1 = Alpro("Justin")
p1.salam()

class Calculator:
  def tambah(self, a, b):
    return a + b

  def kali(self, a, b):
    return a * b

calc = Calculator()
print(calc.tambah(90, 9))
print(calc.kali(11, 9))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Justin", 19)
p1.celebrate_birthday()
p1.celebrate_birthday()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Justin", 19)
print(p1)

class Alpro:
    def __init__(self, name, age, prodi):
        self.name = name
        self.age = age
        self.prodi = prodi

    def printname(self):
        print(self.name)
    
    def printage(self):
        print(self.age)
    
    def printprodi(self):
        print(self.prodi)

    def introduce(self):
        print(f"Nama saya {self.name}, umur saya {self.age}, saya dari prodi {self.prodi}")

p1 = Alpro("Justin", 19, "Teknik Informatika")
p2 = Alpro("James", 18, "Hubungan Internasional")
p3 = Alpro("Emily", 20, "Kedokteran")

p1.introduce()
p2.introduce()
p3.introduce()