#list
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #allow duplicate

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #list length

#list item-data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list constructur
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#check if items exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #by value

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #by index

#clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)