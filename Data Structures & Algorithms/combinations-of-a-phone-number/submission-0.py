class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        if digits == "":
            return []
        res = []
        def dfs(idx, curr):
            if idx == len(digits):
                res.append("".join(curr[:]))
                return
            for char in self.map[int(digits[idx])]:
                curr.append(char)
                dfs(idx+1, curr)
                curr.pop()
        dfs(0,[])
        return res
