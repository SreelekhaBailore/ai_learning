# all



l1 =[x for x in range(1,11)]
is_positive_list = all(l1)
print(is_positive_list) # True

l2 =[x for x in range(-5,6)]
is_positive_list = all(l2)
print(is_positive_list) # False

#enumerate
numbers = [1, 2, 3, 4, 5]
print(enumerate(numbers)) # <enumerate object at 0x7f8c8c8c8c8>
result = {index: value for index, value in enumerate(numbers, 2)}
print(result)

String = "Hello"
print(list(enumerate(String,2))) 

#filter
def isPositive(num):
    if num >0 : 
        return num

l5 = [1, 2, 3, 4, 5]
print(list())
