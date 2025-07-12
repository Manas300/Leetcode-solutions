class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1  # ways to reach step 1
        second = 2  # ways to reach step 2
        
        for i in range(3, n + 1):
            third = first + second  # total ways to reach step i
            first = second  # shift window
            second = third
        
        return second
