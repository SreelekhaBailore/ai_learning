
# def perform_operation(oper_name, oper_set, result_set):
#     if oper_name=="intersection_update":
#         result_set.intersection_update(oper_set)
#     elif oper_name=="update":
#         result_set.update(oper_set)
#     elif oper_name=="symmetric_difference_update":
#         result_set.symmetric_difference_update(oper_set)
#     elif oper_name=="difference_update":
#         result_set.difference_update(oper_set)
#     return result_set

# a=int(input())
# a_set=set(input().split())
# n=int(input())
# result_set=a_set
# for i in range(2*n):
#     if i%2==0:
#         input_string = input().split()
#         oper_name = input_string[0]
#         oper_elem_size = input_string[1]
#     else:
#         oper_set=set(input().split())
#         result_set = perform_operation(oper_name, oper_set, result_set)
# sum=0
# for i in result_set:
#     sum+=int(i)
# print(sum)


# Enter your code here. Read input from STDIN. Print output to STDOUT
# k=int(input())
# room_numbers = input().split()
# no_of_families = (len(room_numbers)-1)/5

# room_numbers_map={}
# for i in room_numbers:
#     if room_numbers_map.get(i)!=None:
#         room_numbers_map[i]= room_numbers_map.get(i)+1
#     else:
#         room_numbers_map[i]=1
# 5

# result = [k for k,v in room_numbers_map.items() if v==1][0]
# print(result)


# Enter your code here. Read input from STDIN. Print output to STDOUT

# t=int(input())
# for i in range(t):
#     a = int(input())
#     a_set = set(input().split())
#     b = int(input())
#     b_set = set(input().split())
#     print(not a_set.issubset(b_set))


# Enter your code here. Read input from STDIN. Print output to STDOUT

# def isPalindrome(n):
#     result=0
#     r=n
#     while r>0:
#        a = r%10
#        result = result * 10 + a
#        r=r//10

#     return result== n
    
    

# n = int(input())
# int_list = [int(x) for x in input().split()]
# print(all([x>0 for x in int_list]) and any([isPalindrome(x) for x in int_list]))


# n = int(input())
# arr = list(map(int, input().split()))
    
# distinct_list = list(sorted(set(arr), reverse=
#                         True))
# print(distinct_list[1])

def get_students_with_score(score):
    result=[]
    for y in students:
        print(f"y[1]: {y[1]}")
        print(f"score: {score}")
        if y[1]==score:
            result.append(y[0])
    return result

students=[]
scores=[]
for _ in range(5):
    l1 = []
    name = input()
    score = float(input())
    scores.append(score)
    l1.append(name)
    l1.append(score)
    students.append(l1)
print(students)
scores = sorted(scores)
scores = list(set(scores))
secons_max_score = scores[1]
result = get_students_with_score(secons_max_score)
[print(x) for x in sorted(result, key=lambda x: x[0])]