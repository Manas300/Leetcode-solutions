class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)  

        
        result = []
        for num, freq in count.items():
            if freq == 1:
                result.append(num)

        # Step 3: Return the result
        return result