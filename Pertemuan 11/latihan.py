#1
print("Soal 1")
pasien = [
  "Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
  "Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
  "Irfan Maulana", "Joko Susilo"
]

def cariNamaPasien(arr, targetVal):
  for i in range(len(arr)):
    if arr[i].lower() == targetVal:
      return i
  return -1

nama_pasien = input("Masukkan nama pasien yang dicari: ")

result = cariNamaPasien(pasien, nama_pasien.lower())

if result != -1:
  print(f"{nama_pasien} ditemukan di urutan ke-", result+1)
else:
  print(f"{nama_pasien} tidak ada dalam daftar hari ini.")

#2
print("Soal 2")
id_karyawan = [
  1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
  1378, 1401, 1456, 1502, 1567, 1634, 1700
]

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1
  perbandingan = 0

  while left <= right:
    mid = (left + right) // 2

    perbandingan += 1

    if arr[mid] == targetVal:
      return [mid, perbandingan]
    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return [-1, perbandingan ]

ID_karyawan = int(input("Masukkan ID karyawan yang dicari: "))
result_id = binarySearch(id_karyawan, ID_karyawan)

if result_id[0] != -1:
  print(f"ID {ID_karyawan} ditemukan! Posisi ke-{result_id[0]+1} dalam daftar.")
else:
  print(f"ID {ID_karyawan} tidak terdaftar sebagai karyawan.")

print(f"Proses perbandingan: {result_id[1]} kali.")

#3
print("Soal 3")
rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", 
         "BK-091","BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", 
         "BK-059", "BK-071", "BK-083", "BK-095"]

kode_buku = input("Masukkan kode buku yang dicari: ")

print("Mencari Rak A (Linear Search)...")
resultbuku_linear = cariNamaPasien(rak_a, kode_buku)
if resultbuku_linear != -1:
  print(f"{kode_buku} ditemukan di urutan ke-{resultbuku_linear+1}")
else:
  print(f"{kode_buku} tidak ditemukan di Rak A.")


print("Mencari di Rak B (Binary Search)...")
resultbuku_binary = binarySearch(rak_b, kode_buku)
if resultbuku_binary[0] != -1:
  print(f"{kode_buku} ditemukan di rak B! Posisi ke-{resultbuku_binary[0]+1}di rak B")
else:
  print(f" {kode_buku} tidak ditemukan di Rak B.")