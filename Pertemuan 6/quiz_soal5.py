class Menu:
    def __init__(self, namaMenu, harga):
        self.namaMenu = namaMenu
        self.harga = harga
    
    def tampilkan_menu(namaMenu, harga):
        super.__init__(namaMenu, harga)
        print(f"{namaMenu} - Rp {harga}")
    
class Transaksi:
    def __init__(total=0):
        pass
    
    def tambah (menu, jumlah):
        super.__init__(total=0)
        total += jumlah
        print(total)

    def struk(total):
        print(f"Total Belanja: {total}")
    
