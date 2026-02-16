class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Step 1: If string is empty or starts with '0', no valid decoding
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        
        # Step 2: dp[i] will store number of ways to decode substring starting at index i
        dp = [0] * (n + 1)
        
        # Step 3: Base case
        # Reaching the end means we formed 1 valid decoding path
        dp[n] = 1
        
        # Step 4: Fill dp array from right to left
        for i in range(n - 1, -1, -1):
            
            # If current digit is '0', it cannot be decoded alone
            if s[i] == "0":
                dp[i] = 0
            
            else:
                # Option 1: Take one digit
                # If current digit is valid (1–9),
                # number of ways includes ways from next index
                dp[i] = dp[i + 1]
                
                # Option 2: Take two digits
                # Check if two-digit number is valid (10–26)
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        
        # Step 5: Result is number of ways from index 0
        return dp[0]
