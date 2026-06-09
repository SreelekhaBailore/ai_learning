class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numCols = int(len(s)/numRows) +1
        a = [[None for _ in range(numCols)] for _ in range(numRows)]
        j=0
        k=0
        while(j<numCols and k<len(s)):
                i=0
                while(i<numRows and k<len(s)):
                    a[i][j]=s[k]
                    k+=1
                    i+=1
                i-=2
                while(i>0 and numCols>1 and k<len(s)):
                    a[i][j]=a[i][j]+s[k]
                    k+=1
                    i-=1
                j+=1
        result=""
        for i in range(numRows):
            for j in range(numCols):
                if a[i][j] is not None:
                    result = result + a[i][j]
        return result

print(Solution().convert("ABCD", 3))


        