class Solution:
    def isPalindrome(self,s, i, j):
        left = i
        right = j
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i,cur):
            if i==len(s):
                res.append(cur[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j):
                    cur.append(s[i:j+1])  
                    dfs(j+1, cur)
                    cur.pop()
        dfs(0,[])
        return res