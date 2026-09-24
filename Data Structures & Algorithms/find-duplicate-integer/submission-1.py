class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [False]*(len(nums)+1)

        for num in nums:
            if seen[num]:
                return num
            seen[num] = True
        return -1
        