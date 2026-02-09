#soal nomor 1
def fizzbuzz_plus(n):
    for x in range (n):
        if x % 3 and 5:
            print ("FizzBuzz")
        elif x % 3:
            print ("Fizz")
        elif x % 5:
            print("Buzz")
        elif x % 7:
            print ("Seven")
        else:
            print (x)
result = fizzbuzz_plus(21) 
print (result)

#soal nomor 3
def hitung_nilai(tugas, uts, uas):
    x = tugas /30
    y = uts /30
    z = uas /40
    nilai = (x + y + z)
    grade
    if nilai >= 85:
        print ("A")
    elif nilai >= 70:
        print ("B")
    elif nilai >= 55:
        print ("C")
    elif nilai >= 40:
        print ("D")
    elif nilai < 40:
        print ("E")
result = hitung_nilai(tugas, uts, uas)
print ("Nilai :" nilai)
print ("Grade :")