#filter
def isPositive(num):
    if num >0 : 
        return num

l5 = [1, 2, 3, 4, 5]
print(l5)

print(list(filter(isPositive, l5)))