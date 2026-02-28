#soal 1
angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

#soal 2
try:
    angka_1 = int(input("Masukkan Angka ke-1: "))
    angka_2= int(input("Masukkan Angka ke-2: "))
    print(f"Hasil: {angka_1/angka_2}")
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")
finally:
    print("Selesai.")