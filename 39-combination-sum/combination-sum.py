from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:       # found a valid combination
                result.append(path[:])
                return
            if total > target:        # too big, stop
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])           # pick number
                backtrack(i, path, total + candidates[i])  # can reuse same number
                path.pop()                            # backtrack

        backtrack(0, [], 0)
        return result
