class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0  # Pointer for the position of valid elements
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]  # Copy valid element to the j-th position
                j += 1  # Increment the valid element pointer
    
        return j  # Return the count of valid elements
        