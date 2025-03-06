class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move i to the next character in s
                i += 1
            j += 1  # Always move j to check next character in t
        
        return i == len(s)  # If we matched all characters in s, return True