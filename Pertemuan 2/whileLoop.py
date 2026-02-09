#The while Loop
i = 5
while i <= 8:
  print(i)
  i += 1
  
#The break Statement
i = 3
while i < 6:
  print(i)
  if i == 5:
    break
  i += 1

#The continue Statement
i = 0
while i < 5:
  i += 1
  if i == 2:
    continue
  print(i)

#The else Statement
i = 1
while i <= 3:
  print(i)
  i += 1
else:
  print("i tidak lagi kecil dari sama dengan 3")
