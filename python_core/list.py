list1 = []

#Insert element into a list
list1.append(1)
list1.append(2)
list1.append(3)

print(list1)

#Insert element into a list at a specific index
list1.insert(2,4)
print(list1)

# Remove a specific element from the list
list1.remove(2)
print(list1)

# Remove an element at a specific index
list1.pop(2)
print(list1)

list1.append(0)
list1.append(7)
list1.append(1)
print(list1)


list1.sort()
print(list1)

list2 = sorted(list1, reverse=False)
print(f"The sorted list is {list2}")

list1.reverse()
print(f"The reversed list is {list1}")

sum=0
for i in list1:
    sum+=i
print(f"The sum is {sum}")

list4=[]
for i in list1:
        if i>5:
              list4.append(i)

print(f"The list of numbers greater than 5 is {list4}")


names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.sort()
print(f"The sorted names are {names}")
print(f"The reversed sorted names are {sorted(names, reverse= True)}")


# CLear the list
list1.clear()
print(list1)





