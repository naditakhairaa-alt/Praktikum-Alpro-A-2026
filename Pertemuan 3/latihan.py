class Jam:
    def __init__(self, bentuk, merk, bahan):
     self.bentuk = bentuk
     self.merk = merk
     self.bahan = bahan

def printjam(self):
    print(self.bentuk)

def ubahJam(self, bahanBagus):
    self.bahan = bahanBagus

p1 = Jam("Bulat", "Casio", "Kulit")
p2 = Jam("Persegi", "AC", "Karet")
p3 = Jam("Oval", "Rolex", "Rantai")

print (p1.merk)
print (p2.merk)
print (p3.merk)