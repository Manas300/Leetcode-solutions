class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            total =0
            while num>0:
                digit=num%10
                total+=digit**2
                num=num//10
            return total

        seen=set()
        while n != 1:
            if n in seen:  
                return False
            seen.add(n)
            n = helper(n)  
        return True


        


        