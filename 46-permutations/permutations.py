from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            # Base case: path has all numbers
            if len(path) == len(nums):
                result.append(path[:])  # save a copy
                return

            # Try each number that is not already in path
            for num in nums:
                if num not in path:
                    path.append(num)       # choose
                    backtrack(path)        # explore
                    path.pop()             # undo choice (backtrack)

        backtrack([])
        return result
