class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.map = dict()
        for num in candidates:
            self.map[num] = self.map.get(num,0)+1
        unique_num = list(self.map.keys())
        ans = []
        def dfs(i, cur, total):
            if total == target:
                ans.append(cur[:])
                return

            if i == len(unique_num) or total > target:
                return
            number = unique_num[i]
            freq = self.map[number]
            for count in range(freq+1):
                for _ in range(count):
                    cur.append(number)
                    total+=number
                dfs(i+1, cur, total)
                for _ in range(count):
                    cur.pop()
                    total-=number
            
        dfs(0,[],0)
        return ans
        