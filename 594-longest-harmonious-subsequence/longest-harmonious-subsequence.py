class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the array
        max_len = 0
        start = 0

        for end in range(len(nums)):
            # Keep moving the start forward until the difference is <= 1
            while nums[end] - nums[start] > 1:
                start += 1
            # If the difference is exactly 1, it's a harmonious subsequence
            if nums[end] - nums[start] == 1:
                max_len = max(max_len, end - start + 1)
    
        return max_len