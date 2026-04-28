#variabel yang disediakan
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

#angka rahasia diambil berurutan sesuai nomor ronde. Apabila ronde melebihi 10, gunakan operasi modulo
# DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]

# === BAGIAN A ===
def tebak_angka(angka_rahasia, maks_percobaan):
    '''
    fungsi menebak angka rahasia. pemain diminta untuk input angka untuk ditebak.
    '''
    angka_rahasia = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
    maks_percobaan = 7
    for j in range (maks_percobaan):
        if maks_percobaan == 0:
            return False
        elif maks_percobaan != 0:
            for i in range (angka_rahasia):
                tebakan = int(input("Masukkan angka: "))
                if tebakan < angka_rahasia:
                    print("Terlalu kecil")
                elif tebakan > angka_rahasia:
                    print("Terlalu besar")
                elif tebakan == angka_rahasia:
                     print("Benar!") 
            return True           

def hitung_skor(berhasil, sisa_percobaan):
    '''
    fungsi menghitung skor. jika berhasil dijalankan maka akan menampilkan hasil skor, 
    jika tidak akan menampilkan 0.
    '''
    if berhasil == True:
        skor = sisa_percobaan * 10
        return skor
    else:
        return 0

def main_satu_ronde(nama, nomor_ronde):
    pemain = []
    
    nama = input("Masukkan nama pemain: ")
    nomor_ronde = DAFTAR_ANGKA
    DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]

    hasil = tebak_angka()
    skor = hitung_skor()

    data = [nama, skor]
    pemain.append(data)

# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    '''
    fungsi menampilkan riwayat permainan.
    '''
    print("Tampilkan riwayat.")
    print(*riwayat, sep='\n')
    format_tabel = []
    riwayat = []
    # for i in range (len(format_tabel)):
    #     for j in range ()

# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    riwayat = []
    salinan = []
    pass

def tampilkan_leaderboard(riwayat):
    pass

#PROGRAM UTAMA
def program_utama():
    nama = input("Masukkan nama pemain: ")
    ronde = main_satu_ronde()
    riwayat = []
    while True:
        hasil_permainan = ronde
        riwayat.append(hasil_permainan)
        sesi_berakhir = tampilkan_riwayat()
        peringkat_akhir = tampilkan_leaderboard
        
        print(nama)
        print(ronde)
        print(riwayat)
        print(sesi_berakhir)
        print(peringkat_akhir)