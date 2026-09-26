class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        taken = [False]*len(nums)
        def dfs(idx, cur):
            if idx==len(nums):
                ans.append(cur.copy())
                return
            for i in range(len(nums)):
                if taken[i]:
                    continue
                taken[i] = True
                cur.append(nums[i])
                dfs(idx+1,cur)
                cur.pop()
                taken[i] = False
        dfs(0,[])
        return ans
            