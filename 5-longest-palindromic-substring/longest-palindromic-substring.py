class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:  # Check if palindrome
                    if len(substring) > max_len:
                        max_len = len(substring)
                        result = substring
                        
        return result
