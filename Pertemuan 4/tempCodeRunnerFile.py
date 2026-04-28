try:
    angka_1 = int(input("Masukkan Angka ke-1: "))
    angka_2= int(input("Masukkan Angka ke-2: "))
    print(f"Hasil: {angka_1/angka_2}")
except ValueError:
    print("Harus berupa angka")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")