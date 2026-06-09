class Solution:
    def findOddMaxPalindrome(self,i:int, s:str):
        l=i
        r=i
        palin=""
        while(l>=0 and r<len(s) and s[l]==s[r] ):
            palin=s[l:r+1]
            l=l-1
            r=r+1
            if(self.isPalindrome(s[l:r+1]) and len(s[l:r+1])>len(palin)):
                palin=s[l:r+1]
        return len(palin)

    def findEvenMaxPalindrome(self,i:int, s:str):
        l=i
        r=i+1
        palin=""
        while( l>=0 and r<len(s) and s[l]==s[r] ):
            palin=s[l:r+1]
            l=l-1
            r=r+1
            if(self.isPalindrome(s[l:r+1]) and len(s[l:r+1])>len(palin)):
                palin=s[l:r+1]
        return len(palin)
        
    def isPalindrome(self,s:str):
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        elif n==1:
            return s
        elif n==2:
            if s== s[::-1]:
                return len(s)
            else:
                return 1
        longest = 0
        for i in range(0,len(s)-1):
            odd_length= self.findOddMaxPalindrome(i,s)
            even_length = self.findEvenMaxPalindrome(i,s)
            if(odd_length>even_length and odd_length>longest):
                longest = odd_length
            elif(even_length>longest):
                longest = even_length
        return longest

print(Solution().longestPalindrome("babad"))
        



                 