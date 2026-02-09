#The Python Match Statement
day = 6
match day:
  case 1:
    print("Senin")
  case 2:
    print("Selasa")
  case 3:
    print("Rabu")
  case 4:
    print("Kamis")
  case 5:
    print("Jumat")
  case 6:
    print("Sabtu")
  case 7:
    print("Minggu")

#defult case
day = 4
match day:
  case 6:
    print("Sabtu")
  case 7:
    print("Minggu")
  case _:
    print("Tidak ditemukan kecocokan!")

#Combine Values
day = 1
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Weekdays")
  case 6 | 7:
    print("Weekend!")

#If Statements as Guards
month = 8
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 8:
    print("A weekday in August")
  case 1 | 2 | 3 | 4 | 5 if month == 9:
    print("A weekday in September")
  case _:
    print("Tidak ditemukan kecocokan!")

