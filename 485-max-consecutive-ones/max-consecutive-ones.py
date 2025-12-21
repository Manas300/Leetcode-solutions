class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr = 0

        for x in nums:
            if x == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0

        return max_count
