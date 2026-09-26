class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def createSubset(idx, curr, Sum):
            if idx==n:return
            if Sum==target:
                ans.append(curr[:])
                return
            if Sum>target:
                return
            curr.append(nums[idx])
            createSubset(idx, curr, Sum+nums[idx])
            curr.pop()
            createSubset(idx+1, curr, Sum)
        createSubset(0,[],0)
        return ans

        