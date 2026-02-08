class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, return 0 islands
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])  # dimensions of the grid
        islands = 0  # counter for number of islands

        # DFS function to explore and mark all connected land
        def dfs(r, c):
            # Base case: stop if out of bounds or at water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark the current land cell as visited by changing '1' -> '0'
            grid[r][c] = '0'
            # Explore all 4 directions recursively
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left

        # Loop through every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If the cell is land ('1'), it's a new island
                if grid[i][j] == '1':
                    islands += 1          # count this island
                    dfs(i, j)             # flood-fill all connected land

        # Return the total number of islands
        return islands
