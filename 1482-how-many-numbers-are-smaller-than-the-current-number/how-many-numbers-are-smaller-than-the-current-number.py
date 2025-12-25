class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        mapping ={}
        result =[]

        for i in range(len(sort)):
            if sort[i] not in mapping:
                mapping[sort[i]] = i
            
        for num in nums:
            result.append(mapping[num])
        
        return result