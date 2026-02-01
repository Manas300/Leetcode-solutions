class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        path = []

        def dfs(start, nums_needed, remaining_sum):
            if nums_needed == 0:
                if remaining_sum == 0:
                    res.append(path[:])
                return

            for x in range(start, 10):
                if x > remaining_sum:
                    break
                path.append(x)
                dfs(x + 1, nums_needed - 1, remaining_sum - x)
                path.pop()

        dfs(1, k, n)
        return res
