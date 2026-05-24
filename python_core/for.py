fruits=["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit=="banana":
            break
    

for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

#list comprehension
a= [k for k in range(5) if k==3]
print(a) 