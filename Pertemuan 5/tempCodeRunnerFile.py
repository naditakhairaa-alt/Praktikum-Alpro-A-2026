def kali_skalar(matriks, k):
 hasil = []
 for baris in matriks:
   baris_baru = [elemen * k for elemen in baris]
   hasil.append(baris_baru)
 return hasil

A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]

c_skalar = kali_skalar(A, 4)
for i in c_skalar:
  print(i)