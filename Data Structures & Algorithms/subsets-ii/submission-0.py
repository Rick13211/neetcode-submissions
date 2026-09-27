class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.map = {}

        for num in nums:
            self.map[num] = self.map.get(num,0)+1
        unique_nums= list(self.map.keys())
        ans = []
        def dfs(i, cur):
            if i==len(unique_nums):
                ans.append(cur[:])
                return
            number = unique_nums[i]
            for count in range(self.map[number]+1):
                for _ in range(count):
                    cur.append(number)
                dfs(i+1, cur)
                for _ in range(count):
                    cur.pop()
        
        dfs(0,[])
        return ans