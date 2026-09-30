class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(x,y):
            if visited[x][y]:
                return
            
            visited[x][y] = True

            for dx, dy in direction:
                nx,ny = x+dx, y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == '1':
                    if visited[nx][ny]:
                        continue
                    dfs(nx, ny)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    
                    dfs(i, j)
                    count+=1

        return count

        