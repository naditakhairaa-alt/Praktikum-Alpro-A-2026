# Matriks 3x3 dengan inisialisasi nilai langsung
matriks_3x3 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
# Matriks 2x4
matriks_2x4 = [[10, 20, 30, 40],
               [50, 60, 70, 80]]
print('Matriks 3x3:', matriks_3x3)
print('Matriks 2x4:', matriks_2x4)

# Matriks 4x4 dengan nilai default 0
N, M = 4, 4
matriks_default = [[0 for j in range(M)] for i in range(N)]
print('Matriks default:', matriks_default)
# Matriks 3x5 dengan nilai default -1
matriks_neg = [[-1 for j in range(5)] for i in range(3)]
print('Matriks -1:', matriks_neg)

matriks = [[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]]

print(matriks[0][0]) # Output: 10 (baris 0, kolom 0)
print(matriks[1][2]) # Output: 60 (baris 1, kolom 2)
print(matriks[2]) # Output: [70, 80, 90] (seluruh baris 2)

# Iterasi semua elemen
for i in range(len(matriks)):
   for j in range(len(matriks[i])):
      print(f'matriks[{i}][{j}] = {matriks[i][j]}')

#menghitung total semua elemen
def total_elemen(matriks):
   total = 0
   for baris in matriks:
      for elemen in baris:
         total += elemen
   return total

matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print('Total manual:', total_elemen(matriks))

# Cara singkat dengan fungsi bawaan Python
total_singkat = sum(sum(baris) for baris in matriks)
print('Total singkat:', total_singkat)
# Output:
# Total manual: 45
# Total singkat: 45

#mengalikan elemen dengan konstanta
def kali_skalar(matriks, k):
   hasil = []
   for baris in matriks:
      baris_baru = [elemen * k for elemen in baris]
      hasil.append(baris_baru)
   return hasil

A = [[1, 2, 3],
[4, 5, 6]]
hasil = kali_skalar(A, 3)
for baris in hasil:
   print(baris)
# Output:
# [3, 6, 9]
# [12, 15, 18]

#transpose matriks
def transpose(matriks):
   baris = len(matriks)
   kolom = len(matriks[0])
   # Buat matriks hasil berukuran kolom x baris (dimensi terbalik)
   hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
   for i in range(baris):
      for j in range(kolom):
         hasil[j][i] = matriks[i][j]
   return hasil

A = [[1, 2, 3],
     [4, 5, 6]] # Ukuran 2x3

print('Matriks A (2x3):')
for baris in A:
   print(baris)

T = transpose(A)
print('Transpose A (3x2):')
for baris in T:
   print(baris)

# Output:
# Matriks A (2x3):
# [1, 2, 3]
# [4, 5, 6]
# Transpose A (3x2):
# [1, 4]
# [2, 5]
# [3, 6]

# Cara ringkas dengan zip
T2 = [list(baris) for baris in zip(*A)]
print(T2) # Output: [[1, 4], [2, 5], [3, 6]]

# Dengan NumPy
import numpy as np
A_np = np.array([[1, 2, 3], [4, 5, 6]])
print(A_np.T)

#determinan matriks
def determinan_2x2(matriks):
   a, b = matriks[0][0], matriks[0][1]
   c, d = matriks[1][0], matriks[1][1]
   return (a * d) - (b * c)

# Contoh 1
A = [[3, 8], [4, 6]]
print('det(A):', determinan_2x2(A))
# Perhitungan: (3x6) - (8x4) = 18 - 32 = -14
# Output: det(A): -14

# Contoh 2: matriks singular (det = 0)
C = [[2, 4], [1, 2]]
print('det(C):', determinan_2x2(C))
# Perhitungan: (2x2) - (4x1) = 4 - 4 = 0
# Output: det(C): 0

def determinan_3x3(M):
# Diagonal utama: dijumlahkan
   d1 = M[0][0] * M[1][1] * M[2][2]
   d2 = M[0][1] * M[1][2] * M[2][0]
   d3 = M[0][2] * M[1][0] * M[2][1]
# Diagonal sekunder: dikurangkan
   d4 = M[0][2] * M[1][1] * M[2][0]
   d5 = M[0][0] * M[1][2] * M[2][1]
   d6 = M[0][1] * M[1][0] * M[2][2]
   return (d1 + d2 + d3) - (d4 + d5 + d6)

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 2, 9]]
print('det(B):', determinan_3x3(B))
# Langkah: (45 + 84 + 24) - (105 + 12 + 72) = 153 - 189 = -36
# Output: det(B): -36

# Verifikasi dengan NumPy
import numpy as np
print('Verifikasi:', round(np.linalg.det(B), 4))
# Output: Verifikasi: -36.0

#inverse matriks
def determinan_2x2(m):
   return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse_2x2(matriks):
   det = determinan_2x2(matriks)
   if det == 0:
      print('Matriks singular: inverse tidak ada (det = 0)')
      return None
   a, b = matriks[0][0], matriks[0][1]
   c, d = matriks[1][0], matriks[1][1]
   return [[ d/det, -b/det],
           [-c/det, a/det]]

A = [[4, 7],
[2, 6]]
inv = inverse_2x2(A)
print('Inverse A:')
for baris in inv:
   print([round(x, 4) for x in baris])
# Output:
# Inverse A:
# [0.6, -0.7]
# [-0.2, 0.4]

# Verifikasi: A x A_inv harus menghasilkan matriks identitas
import numpy as np
A_np = np.array(A, dtype=float)
print('A x A_inv:')
print(np.round(A_np @ np.linalg.inv(A_np), 4))
# Output:
# [[1. 0.]
# [0. 1.]]

import numpy as np
A = np.array([[2.0, 1.0, 0.0],
              [1.0, 3.0, 1.0],
              [0.0, 1.0, 2.0]])

det = np.linalg.det(A)
print('Determinan:', round(det, 4)) # Output: 8.0

A_inv = np.linalg.inv(A)
print('Inverse A:')
print(np.round(A_inv, 4))

# Verifikasi
print('A x A_inv:')
print(np.round(A @ A_inv, 4))
# Output: matriks identitas 3x3

#operasi pada dua matriks
#penjumlahan matriks
def tambah_matriks(A, B):
   if len(A) != len(B) or len(A[0]) != len(B[0]):
      print('Error: ukuran matriks tidak sama')
      return None
   baris, kolom = len(A), len(A[0])
   hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
   return hasil

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [1, 2, 3]]

C = tambah_matriks(A, B)
for baris in C:
   print(baris)
# Output:
# [8, 10, 12]
# [5, 7, 9]

#pengurangan matriks
def kurang_matriks(A, B):
   baris, kolom = len(A), len(A[0])
   hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
   return hasil

A = [[10, 8, 6], [4, 2, 0]]
B = [[1, 3, 5], [7, 9, 11]]

D = kurang_matriks(A, B)
for baris in D:
   print(baris)
# Output:
# [9, 5, 1]
# [-3, -7, -11]

#perkalian dua matriks
def kali_matriks(A, B):
   baris_A, kolom_A = len(A), len(A[0])
   baris_B, kolom_B = len(B), len(B[0])
   if kolom_A != baris_B:
      print('Error: kolom A harus sama dengan baris B')
      return None
   hasil = [[0]*kolom_B for _ in range(baris_A)]
   for i in range(baris_A):
      for j in range(kolom_B):
         for k in range(kolom_A):
            hasil[i][j] += A[i][k] * B[k][j]
   return hasil

A = [[1, 2], [3, 4], [5, 6]] # Ukuran 3x2
B = [[7, 8, 9], [10, 11, 12]] # Ukuran 2x3

C = kali_matriks(A, B) # Hasil ukuran 3x3
for baris in C:
   print(baris)

# Output:
# [27, 30, 33]
# [61, 68, 75]
# [95, 106, 117]

#pembagian matriks (elemen per elemen)
def bagi_matriks_elementwise(A, B):
   baris, kolom = len(A), len(A[0])
   hasil = [[0.0]*kolom for _ in range(baris)]
   for i in range(baris):
      for j in range(kolom):
         if B[i][j] == 0:
            print(f'Error: pembagi 0 pada posisi [{i}][{j}]')
            return None
         hasil[i][j] = A[i][j] / B[i][j]
   return hasil
A = [[10, 20, 30], [40, 50, 60]]
B = [[2, 4, 5], [8, 10, 12]]

E = bagi_matriks_elementwise(A, B)
for baris in E:
   print(baris)
# Output:
# [5.0, 5.0, 6.0]
# [5.0, 5.0, 5.0]

#implementasi dengan library numpy

import numpy as np

# Membuat matriks
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matriks identitas dan nol
I = np.eye(3)
Z = np.zeros((3, 3))

# Operasi dasar
print('A + B:')
print(A + B)
print('A - B:')
print(A - B)

# Perkalian elemen per elemen (Hadamard product)
print('A * B (element-wise):')
print(A * B)

# Perkalian matriks sejati (dot product)
print('A @ B (dot product):')
print(A @ B)

# Transpose
print('Transpose A:')
print(A.T)

# Determinan
M = np.array([[1, 2, 3], [4, 5, 6], [7, 2, 9]])
print('Determinan M:', round(np.linalg.det(M), 4))
# Output: -36.0

# Inverse
N = np.array([[4.0, 7.0], [2.0, 6.0]])
print('Inverse N:')
print(np.round(np.linalg.inv(N), 4))
# Output:
# [[ 0.6 -0.7]
# [-0.2 0.4]]

# Program membaca matriks dari keyboard
baris = int(input('Masukkan jumlah baris: '))
kolom = int(input('Masukkan jumlah kolom: '))

# Inisialisasi matriks kosong
matriks = []
print(f'Masukkan elemen matriks {baris}x{kolom}:')
for i in range(baris): # untuk setiap baris
   baris_baru = []
   for j in range(kolom): # untuk setiap kolom dalam baris
      nilai = int(input(f' Elemen [{i}][{j}]: '))
      baris_baru.append(nilai) # tambahkan elemen yang dimasukkan ke baris baru
   matriks.append(baris_baru)
print('Matriks berhasil dibaca!')

# Input tiap baris sekaligus, dipisah spasi
baris = int(input('Jumlah baris: '))
kolom = int(input('Jumlah kolom: '))
matriks = []
for i in range(baris):
   print(f'Masukkan baris ke-{i+1} ({kolom} angka, pisah spasi):')
   data = list(map(int, input().split()))
   matriks.append(data)