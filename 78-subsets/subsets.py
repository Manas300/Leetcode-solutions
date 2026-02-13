from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            # Base case: we considered all elements
            if index == len(nums):
                result.append(path[:])  # make a copy
                return

            # Decision 1: include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()  # undo choice (backtrack)

            # Decision 2: skip nums[index]
            backtrack(index + 1, path)

        backtrack(0, [])
        return result
