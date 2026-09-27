class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        freq = {"(":n, ')':n}
        ans = []
        def dfs(curr, c, o):
            if len(curr)==2*n:
                ans.append("".join(curr))
                return
            if c>o:
                return
            for char in freq.keys():
                if freq[char]>0:
                    freq[char]-=1
                    curr.append(char)
                    if char=='(':
                        dfs(curr, c, o+1)
                    else:
                        dfs(curr, c+1, o)
                    
                    curr.pop()
                    freq[char]+=1

        dfs([],0,0)
        return ans
        