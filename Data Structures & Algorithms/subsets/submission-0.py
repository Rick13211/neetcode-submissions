class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        taken = [False]*len(nums)

        def createSubset(idx,curr):
            nonlocal n
            if idx==n:
                ans.append(curr[:])
                return
            curr.append(nums[idx])
            createSubset(idx+1, curr)
            curr.pop(-1)
            createSubset(idx+1,curr)
        createSubset(0,[])
        return ans

        