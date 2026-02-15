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


p1 = Alpro("Justin", 19, "Teknik Informatika")
p2 = Alpro("James", 18, "Hubungan Internasional")

p1.printname()
p1.printage()
p2.printprodi()