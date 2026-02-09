sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)

#aritmetik
x = 10
y = 5

print(x + y)    #operator tambah
print(x - y)    #operator kurang
print(x * y)    #operator perkalian
print(x / y)    #operator pembagian
print(x % y)    #operator modulis
print(x ** y)   #operator eksponen
print(x // y)   #operator pembulatan

#assingment
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#perbandingan
x = 5
y = 10

print(x == y)   #sama dengan
print(x != y)   #tidak sama dengan
print(x > y)    #x lebih besar dari y
print(x < y)    #x lebih kecil dari y
print(x >= y)   #x lebih besar sama dengan y
print(x <= y)   #x lebih kecil sama dengan y

#logika
x = 5

print(x > 0 and x < 10) #dan
x = 5

print(x < 5 or x > 10) #atau
x = 5

print(not(x > 3 and x < 10)) #not

#identitas
x = ["ikan", "ayam"]
y = ["ikan", "ayam"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

#bitwise
print(6 & 3)
print(6 | 3)

#precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3) #left to right evalution