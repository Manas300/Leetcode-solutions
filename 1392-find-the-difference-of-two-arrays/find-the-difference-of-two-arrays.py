class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            # Convert both lists to sets to eliminate duplicates
        set1, set2 = set(nums1), set(nums2)

        # Find elements in nums1 but not in nums2
        diff1 = list(set1 - set2)

        # Find elements in nums2 but not in nums1
        diff2 = list(set2 - set1)

        # Return the result as a list of two lists
        return [diff1, diff2]

        