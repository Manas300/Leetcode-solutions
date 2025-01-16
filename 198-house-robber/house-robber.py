class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        prev2=0
        prev1=0

        for num in nums:
            curr=max(prev1,num+prev2)
            prev2=prev1
            prev1=curr
        return prev1


            

        