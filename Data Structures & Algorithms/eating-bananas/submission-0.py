def findHours(piles, k):
    hour = 0
    for banana in piles:
        hour += -(banana // -k)
    return hour

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            hours = findHours(piles, mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
