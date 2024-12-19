class Solution:
    def modify(self, s):
        # code here
        s=list(s)
        index=[]
        b=[]
        for i in range(len(s)):
            if s[i]=='a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                index.append(i)
                b.append(s[i])
        b.reverse()
        for i in range(len(index)):
            j=index[i]
            s[j]=b[i]
        c="".join(s)
        return c





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)