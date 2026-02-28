#custom exception
class NamaError(Exception) :
    def __init__ (self, nama):
        self.nama = nama
        super().__init__("Nama harus mengandung minimal 3 huruf.")

class UmurError(Exception):
    def __init__ (self, nomor):
        self.nomor = nomor
        super().__init__("Umur tidak memenuhi syarat! Harus 17-60 tahun.")

class EmailError(Exception) :
    def __init__ (self, email):
        self.email = email
        super().__init__("Email harus mengandung '@'.")

class NomorHPError(Exception) :
    def __init__ (self, nomor):
        self.nomor = nomor
        super().__init__("Nomor HP tidak valid! Harus 10-13 digit angka.")

#fungsi validasi
def validasi_nama(nama):
        if len(nama) < 3 :
            raise NamaError(nama)
        return True
    
def validasi_umur(umur):
        if umur < 17 or umur > 60 :
            raise UmurError(umur)
        return True

def validasi_email(email):
        if '@' in email :
            pass
        else :
            raise EmailError(email)
        return True
    
def validasi_nomor(nomor):
        if 10 <= len(nomor) <= 13 :
            pass
        else : 
            raise NomorHPError(nomor)
        return True
            
print("=== REGISTRASI PESERTA SEMINAR ===")

#try except
while True :
    try : 
        nama = input("Nama lengkap : ")
        nama_valid = validasi_nama(nama)
    except NamaError as n :
        print (f"Error! {n}") 
    else : 
        break

while True :
    try :
        umur = int(input("Umur : "))
        umur_valid = validasi_umur(umur)
    except ValueError :
        print("Masukkan bilangan bulat")
    except UmurError as u :
        print (f"Error! {u}") 
    else : 
        break

while True :
    try :
        email = input("Email : ")
        email_valid = validasi_email(email)
    except EmailError as e :
        print (f"Error! {e}") 
    else : 
        break

while True :
    try :
        nomor = input("Nomor : ")
        nomor_valid = validasi_nomor(nomor)
    except NomorHPError as o :
        print (f"Error! {o}") 
    else : 
        break

#tampilan akhir
print(f"""
=== DATA PESERTA ===
Nama    : {nama}
Umur    : {umur}
Email   : {email}
No HP   : {nomor}
Status  : TERDAFTAR
""")

print("Terima kasih.")