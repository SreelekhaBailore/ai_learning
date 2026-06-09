class Solution:
    def myAtoi(self, s: str) -> int:
        result=''
        for c in s:
            if c == " " and result =='':
                continue
            elif c == " " and result !='':
                break
            if (c == '-') and result =='':
                result =c
            elif (c == '+') and result =='':
                result ='+'
            elif c.isdigit():
                result += c
            elif c.isdigit() == False and result !='':
                break
            elif c.isdigit() == False and result =='':
                return  int(result) if result else 0
        if result == '-' or result == '+':
            return 0
        int_result = int(result) if result else 0
        if int_result > (-2 ** 31) and int_result < (2 ** 31 - 1):
            return  int_result
        elif int_result <= (-2 ** 31):
            return  -2 ** 31
        elif int_result >= (2 ** 31 - 1):
            return  2 ** 31 - 1
            
print(Solution().myAtoi("-+12"))

