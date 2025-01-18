class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Pointer to track unique elements
        j = 0

        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
    
        # The number of unique elements is j + 1
        return j + 1
        