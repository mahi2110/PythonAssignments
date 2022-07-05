print()
Fruitlist = ["Apple", "Grapes", "Mango", "Banana"]
print("List Of Fruits: ", Fruitlist)

print()
# Finding Datatype
print("Type:")
print(type(Fruitlist))

print()
# Adding
Fruitlist.append("Cherry")
print("Added List: ")
print(Fruitlist)

print()
# Removing
Fruitlist.remove("Banana")
print("Removed List: ")
print(Fruitlist)

print()
# Sorting of List
Fruitlist.sort()
print("Sorted List In Ascending: ")
print(Fruitlist)

print()
Fruitlist.sort(reverse=True)
print("Sorted List In Descending: ")
print(Fruitlist)

print()
# Finding Length
length = len(Fruitlist)
print("Length of Fruitlist: ", length)
