#menampilkan menu warung
#1. buat list
menu = [["Nasi Goreng", 15000], 
        ["Mie Goreng", 12000], 
        ["Es Teh", 5000], 
        ["Air Mineral", 4000], 
        ["Es Jeruk", 7000]]

#2. tampilkan menu
for i in range (len(menu)):
    print(f"{i+1}. {menu[i][0]}" + f" Rp {menu[i][1]}")


#3. mmemasukkan nomor menu yang dipilih
order = int(input("Masukkan nomor menu: "))

#4. if else untuk validasi input
if order == 1:
    print ("Nasi Goreng", 15000)
elif order == 2:
    print ("Mie Goreng", 12000)
elif order == 3:
    print ("Es Teh", 5000)
elif order == 4:
    print ("Air Mineral", 4000)
elif order == 5:
    print("Es Jeruk", 7000)
else:
    print("Error! Tidak ada pilihan")