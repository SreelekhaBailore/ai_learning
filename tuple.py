
t1 = (1,9,7,3,0,6)
print(f"First Tuple is {t1}")

t2 = sorted(t1,reverse=False)
print(f"Sorted Tuple is {t2}")

t3 = sorted(t1,reverse=True)
print(f"Reverse Sorted Tuple is {t3}")

t2 = (2,9,0,5,4)
print(f"Second Tuple is {t2}")


print(f"Elemenst from Second element in t1: {t1[:5]}")

l1 = list(t1)
l1.append(10)
t1 = tuple(l1)
print(f"Elemenst in t1 after insertion: {t1}")

l1 = list(t1)
l1.remove(0)
t1= tuple(l1)
print(f"Elemenst in t1 after deletion: {t1}")





fruits=("apple","banana","cherry")
print("----Excersise---")
print(f"The tuple is {fruits}")
print(f"Second item in the tuple is {fruits[1]}")
print(f"Size of the tuple is{len(fruits)}")

(a,b,c) = fruits
print(f"After unpacking, b is {b}")



