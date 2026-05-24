import string

def print_underscors(n):
    k=1
    while k<=n:
        print("-",end="")
        k+=1
def print_pattern(n):
    k=1
    while k<=n:
        print(pattern[0]+pattern[1]+pattern[2],end="")
        k+=1

n,m = map(int, input().split())
if(n<=5 or n>=101 or m<=15 or m>=303):
    print("Input out of range")
else:
    pattern = [".","|",".","-"]
    for j in range(n):
        if j<(n-1)/2:
            no_of_pattern = ((2*j)+1)
            no_of_dots = ((m) -(3*no_of_pattern))/2
            print_underscors(no_of_dots)
            print_pattern(no_of_pattern)
            print_underscors(no_of_dots)
            print()
        elif j==(n-1)/2:
            k=1;
            no_of_dots = ((m) -(7))/2
            print_underscors(no_of_dots)
            print("WELCOME",end="")
            print_underscors(no_of_dots)
            print()
        else:
            no_of_pattern = ((2*(n-j))-1)
            no_of_dots = ((m) -(3*no_of_pattern))/2
            print_underscors(no_of_dots)
            print_pattern(no_of_pattern)
            print_underscors(no_of_dots)
            print()
    
    

