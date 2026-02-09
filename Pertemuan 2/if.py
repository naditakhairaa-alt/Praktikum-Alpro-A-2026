#Python Conditions and If statements
a = 90
b = 30
if b < a:
  print("b lebih kecil dari a")

angka = 99
if angka > 0:
  print("Angka adalah bilangan positif")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#elif
a = 99
b = 99
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b adalah sama")

nilai = 90

if nilai >= 90:
  print("Grade: A")
elif nilai >= 80:
  print("Grade: B")
elif nilai >= 70:
  print("Grade: C")
elif nilai >= 60:
  print("Grade: D")

#else
a = 999
b = 88
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b adalah sama")
else:
  print("a lebih besar dari b")

#shorthand if
a = 56
b = 67
if a < b: print("a lebih kecil dari b")

a = 2
b = 330
print("A") if a > b else print("B")

#operator logika
suhu = 25
hujan = False
weekend = True

if (suhu > 20 and not hujan) or weekend:
  print("Ayo bersepeda!")

#Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200

if b > a:
  pass