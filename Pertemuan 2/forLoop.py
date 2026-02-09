hewan = ["ikan", "ayam", "sapi"]
for x in hewan:
  print(x)

#perulangan string 
for x in "ayam":
  print(x)

#break
hewan = ["ikan", "ayam", "sapi"]
for x in hewan:
  print(x)
  if x == "ikan":
    break
  
#continue
hewan = ["ikan", "ayam", "sapi"]
for x in hewan:
  if x == "sapi":
    continue
  print(x)

#range
for x in range(2, 30, 3):
  print(x)